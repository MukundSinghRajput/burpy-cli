import sys
import asyncio
import inspect
from ..context import Context
from ..flag import Flag
from ..text import TextFormat, format_text
from typing import List, Dict, Callable, Union, Awaitable


class Burpy:
    def __init__(
        self,
        name: str,
        description: str,
        version: str = "1.0.1",
        long_description: str = "",
    ):
        self.name = name
        self.description = description
        self.version = version
        self.long_description = long_description
        self.commands: Dict[
            str, Dict[str, Union[Callable, Callable[..., Awaitable]]]
        ] = {}
        self.command_flags: Dict[str, List[Flag]] = {}

        self.global_flags: List[Flag] = [
            Flag(
                help="Show help for {name} CLI",
                long="help",
                short="h",
                is_bool=True,
                is_special=True,
            ),
            Flag(
                help="Get the current version of {name} CLI",
                long="version",
                short="V",
                is_bool=True,
                is_special=True,
            ),
        ]

    def command(self, func=None, *, name=None, help: str = ""):
        def decorator(f):
            cmd_name = name or f.__name__
            self.commands[cmd_name] = {
                "func": f,
                "original_name": f.__name__,
                "help": help,
            }
            return f

        if func is None:
            return decorator
        return decorator(func)

    def flag(self, help: str, long: str, short: str = "", is_bool: bool = False):
        def decorator(func):
            cmd_name = func.__name__
            if cmd_name not in self.command_flags:
                self.command_flags[cmd_name] = []

            existing_flags = [f for f in self.command_flags[cmd_name] if f.long == long]
            if not existing_flags:
                self.command_flags[cmd_name].append(Flag(help, long, short, is_bool))

            return func

        return decorator

    def parse_arguments(self, command_name: str, args: List[str]) -> Context:
        ctx = Context()
        i = 0

        original_func_name = self.commands[command_name].get(
            "original_name", command_name
        )

        while i < len(args):
            arg = args[i]
            matched_flag = None

            for flag in self.global_flags:
                if arg in [f"--{flag.long}", f"-{flag.short}"]:
                    matched_flag = flag
                    break

            if not matched_flag and original_func_name in self.command_flags:
                for flag in self.command_flags[original_func_name]:
                    if arg in [f"--{flag.long}", f"-{flag.short}"]:
                        matched_flag = flag
                        break

            if matched_flag:
                if matched_flag.is_bool:
                    ctx.set_flag(matched_flag.long, True)
                    args.pop(i)
                else:
                    if i + 1 < len(args) and not args[i + 1].startswith("-"):
                        ctx.set_flag(matched_flag.long, args[i + 1])
                        args.pop(i)
                        args.pop(i)
                    else:
                        print(f"Error: flag needs an argument: --{matched_flag.long}")
                        sys.exit(1)
            else:
                i += 1

        return ctx

    def _is_async_function(self, func):
        return inspect.iscoroutinefunction(func)

    def show_help(self, command_name: str = None):
        title = format_text(self.name, TextFormat.BOLD, TextFormat.RED)
        version = format_text(self.version, TextFormat.ITALIC, TextFormat.YELLOW)

        print(f"{title} CLI {version}")
        print()
        print(self.description)
        print("\nUsage:")
        print(f"  {self.name.lower()} [flags]")
        print()

        print("Available commands:")
        for cmd, details in self.commands.items():
            if cmd != "main":
                print(f"  {cmd}: {details['help']}")
        print()

        print("Flags:")
        for flag in self.global_flags:
            formatted_help = flag.help.format(name=self.name)
            if flag.short:
                print(f"  -{flag.short},--{flag.long} {formatted_help}")
            else:
                print(f"  --{flag.long} {formatted_help}")

    def show_version(self):
        print(f"{self.name} CLI version {self.version}")

    def run(self):
        if len(sys.argv) >= 2:
            if sys.argv[1] in ["-h", "--help"]:
                self.show_help()
                return
            elif sys.argv[1] in ["-V", "--version"]:
                self.show_version()
                return

        if len(sys.argv) < 2:
            self.show_help()
            return

        command_name = sys.argv[1]

        if command_name not in self.commands:
            print(f"Unknown command: {command_name}")
            print("\nAvailable commands:")
            for cmd in self.commands:
                if cmd != "main":
                    print(f"  {cmd}")
            return

        ctx = self.parse_arguments(command_name, sys.argv[2:])

        if len(sys.argv) > 2 and sys.argv[2] in ["-h", "--help"]:
            self._show_command_help(command_name)
            return

        cmd_details = self.commands[command_name]
        cmd = cmd_details["func"]

        if self._is_async_function(cmd):
            asyncio.run(cmd(ctx, sys.argv[2:]))
        else:
            cmd(ctx, sys.argv[2:])

    def _show_command_help(self, command_name: str):
        if command_name not in self.commands:
            print(f"Unknown command: {command_name}")
            return

        cmd_details = self.commands[command_name]
        print("\nUsage:")
        print(f"  {self.name.lower()} {command_name} [argument]")
        print()
        helpp = cmd_details.get("help", "")
        if helpp != "":
            print("Help:")
            print(f"  {helpp}")
        print()

        original_func_name = cmd_details.get("original_name", command_name)

        if (
            original_func_name in self.command_flags
            and self.command_flags[original_func_name]
        ):
            print("Flags:")
            for flag in self.command_flags[original_func_name]:
                if flag.short:
                    print(f"  -{flag.short},--{flag.long} {flag.help}")
                else:
                    print(f"  --{flag.long} {flag.help}")
        print()

<div align="center">
  <img src="assets/wtr.png" alt="example" />
</div>

# Burpy CLI Framework

## 🚀 Burpy: Pythonic CLI Framework

Burpy is a lightweight, flexible, and powerful Command Line Interface (CLI) framework for Python that makes building command-line applications a breeze.

## ✨ Features

- 🔧 Easy command registration
- 🚩 Flexible flag support
- 🔄 Async and sync command support
- 🎨 Rich text formatting
- 🧪 Comprehensive testing
- 📦 Cross-platform compatibility

## 📦 Installation

### Using pip

```bash
pip install burpy-cli
```

### From Source

```bash
git clone https://github.com/MukundSinghRajput/burpy-cli
cd burpy-cli
pip install .
```

## 🚀 Quick Start

### Basic Example

```python
from burpy import Burpy, Context

cli = Burpy("myapp", "A sample CLI application")

@cli.command(help="Greet a user")
@cli.flag(help="Name to greet", long="name", short="n")
def greet(ctx: Context, args: list):
    name = ctx.get_flag("name", "World")
    print(f"Hello, {name}!")

if __name__ == "__main__":
    cli.run()
```

### Advanced Example with Async Support

```python
import asyncio
from burpy import Burpy, Context

cli = Burpy("weather", "Get weather information")

@cli.command(help="Fetch weather for a location")
@cli.flag(help="City name", long="city", short="c")
@cli.flag(help="Verbose output", long="verbose", is_bool=True)
async def weather(ctx: Context, args: list):
    city = ctx.get_flag("city", "Lucknow")
    verbose = ctx.get_flag("verbose", False)
    
    # Simulated async weather fetch
    await asyncio.sleep(1)
    print(f"Weather in {city}: Sunny 🌞")
    
    if verbose:
        print("Detailed weather information...")

if __name__ == "__main__":
    cli.run()
```

## 📋 Command Usage

Create an executable using pyinstaller and start using your CLI tool

```bash
# Basic command
myapp greet --name Alice

# Help for entire CLI
myapp -h

# Help for a specific command
myapp greet -h

# Version information
myapp -V
```

## 🌟 Key Concepts

### Commands

- Register commands using @cli.command
- Optional custom command names
- Support for help descriptions

### Flags

- Add flags with @cli.flag
- Support short and long flag formats
- Boolean and value-based flags

### Context

- Access flag values via ctx.get_flag()
- Default values supported
- Works with both sync and async commands

## 📦 Supported Platforms
- Linux
- macOS
- Windows
- Python >=3.9


## 🔧 Development

```bash
git clone https://github.com/MukundSinghRajput/burpy-cli
cd burpy-cli

# Create virtual environment
poetry shell

# Install development dependencies 
poetry install
```

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/MukundSinghRajput/burpy-cli/blob/MukunD/LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](https://github.com/MukundSinghRajput/burpy-cli/blob/MukunD/CONTRIBUTING.md) for details.

## 📞 Support

- Open an [issue](https://github.com/MukundSinghRajput/burpy-cli/issuess)
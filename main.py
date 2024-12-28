import asyncio
from burpy import Burpy, Context, TextFormat, format_text

cli = Burpy("wtr", description="A CLI tool to show you the weather details.")

@cli.command
@cli.flag("name of the city you want weather report for", "name", "n")
async def wtr(ctx: Context, arg: list):
    city = ctx.get_flag("name", "Lucknow")
    print(f"Fetching the details for the ciyt: {format_text(city, TextFormat.BOLD, TextFormat.RED)}")
    await asyncio.sleep(2)
    print(f"Here is the weather report for the city {format_text(city, TextFormat.BOLD, TextFormat.RED)}")

if __name__ == "__main__":
    cli.run()
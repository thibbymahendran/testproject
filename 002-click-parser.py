
import click

@click.command( context_settings={"token_normalize_func":str.lower} )
@click.argument("location")
@click.option("--apikey", "-a", help="your API key")
@click.option("--humidity", is_flag=True)
@click.option("--numbers", default=1, help="numbers of result")
@click.option("--range", nargs=2, type=(int, int), default=[0]*2 ) # [0,0]
@click.option("--units", type=click.Choice(["METRIC","IMPERIAL"]), default="METRIC"   )
@click.option("--verbose", "-v", count=True)
def main(location, apikey, humidity, units, numbers, range, verbose):
    print(f"Location = {location}")
    print(f"apikey = {apikey}")
    print(f"humidity = {humidity}")
    print(f"units = {units}")
    print(f"numbers = {numbers}")
    print(f"range = {range}")
    print(f"verbose = {verbose}")


main()
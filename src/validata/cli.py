import typer
import yaml

app = typer.Typer()


@app.command()
def validate(contract: str = typer.Option(..., "--contract")):
    with open(contract, "r") as f:
        data = yaml.safe_load(f)

    print("Loaded contract:")
    print(data)


if __name__ == "__main__":
    app()

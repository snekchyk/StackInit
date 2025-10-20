import typer
from rich import print

app = typer.Typer()

@app.command()
def init(project_name: str,
        is_new: bool = typer.Option(False, "--new", "-n"),
        template: str = typer.Option("unknown", "--template", "-t"), 
        pkgmgr: str = typer.Option("unknown", "--pkgmgr", "-p")):
    

    print(f"{"" if not is_new else "new"} project {project_name} has created with template: {template}, package manager: {pkgmgr}")

@app.command()
def add():
    pass

@app.command()
def list():
    pass

@app.command()
def help():
    pass
    
if __name__ == "__main__":
    app()

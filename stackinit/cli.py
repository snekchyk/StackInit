import typer
from .parsers import InitParser

app = typer.Typer()

@app.command()
def init(
    project_name: str,
    is_new: bool = typer.Option(False, "--new", "-n"),
    template: str = typer.Option("unknown", "--template", "-t"), 
    pkgmgr: str = typer.Option("unknown", "--pkgmgr", "-p")
):
    
    # cli.py init -> init_parser.py 
    # #project_name 
    # #is_new #template 
    # #pkgmgr
    
    parser = InitParser(project_name=project_name, is_new=is_new, template=template, pkgmgr=pkgmgr)
    parser.run()

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

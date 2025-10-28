import typer
from .parsers import InitParser
from .parsers import AddParser

app = typer.Typer()

@app.command()
def init(
    project_name: str,
    is_new: bool = typer.Option(False, "--new", "-n"),
    type: str = typer.Option("unknown", "--type", "-t"), 
    pkgmgr: str = typer.Option("unknown", "--pkgmgr", "-p")
):
    
    #cli.py init -> init_parser.py 
    #project_name 
    #is_new 
    #type 
    #pkgmgr
    
    parser = InitParser(project_name=project_name, is_new=is_new, type=type, pkgmgr=pkgmgr)
    parser.run()

@app.command()
def add(
    deps: str = typer.Option("", "--deps", "-d"),
    devdeps: str = typer.Option("", "--devdeps", "-dp"),
    scripts: str = typer.Option("", "--scripts", "-s")
):
    
    #cli.py -> add_parser.py
    #deps
    #devdeps
    #scripts
    
    parser = AddParser(deps=deps, devdeps=devdeps)
    parser.run()

@app.command()
def list():
    pass

@app.command()
def help():
    pass

if __name__ == "__main__":
    app()

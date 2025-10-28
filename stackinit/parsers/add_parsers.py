import os
import json
from rich import print
import requests
from ..executors.add_exec import AddExec

class AddParser():
    def __init__(self, deps, devdeps):
        self.deps = deps
        self.devdeps = devdeps

    def run(self):
        self.check()
        
    def is_package_available(self, package_name):
        print(package_name)
        for pkg in package_name:
            response = requests.get(f"https://pypi.org/pypi/{pkg}/json")
            if response.status_code != 200:
                return False
        return True
            
    def check(self):
        if not os.path.exists('stackinit.json'):
            print("[red]Error:[/red] [bold red]stackinit.json[/bold red] file not found in the current directory.")
            return
        
        with open('stackinit.json', 'r') as f:
            content = json.load(f)
        
        deps = content.get('dependencies', [])
        devdeps = content.get('devDependencies', [])
        self.deps = self.deps.split(" ")
        self.devdeps = self.devdeps.split(" ")
        
        for el in self.deps:
            if el in deps:
                print("[yellow]Warning:[/yellow] Dependency already exists in stackinit.json.")
                return
        for el in self.devdeps:
            if el in devdeps:
                print("[yellow]Warning:[/yellow] Dev dependency already exists in stackinit.json.")
                return
            
        if self.is_package_available(self.deps):
            exec = AddExec(self.deps, self.devdeps)
            exec.run()
            
        else:
            print("[red]Error:[/red] [bold red]One or more packages[/bold red] are not available in the package registry.")            
        

        
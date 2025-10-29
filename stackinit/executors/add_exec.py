import json
import os
from rich import print


class AddExec():
    def __init__(self, deps, devdeps):
        self.deps = deps
        self.devdeps = devdeps

    def run(self):
        self.write_to_stackinit()
        #self.installing_dependencies()
        
    def write_to_stackinit(self):
        with open('stackinit.json', 'r') as f:
            content = json.load(f)
        
        deps = content.get('dependencies', []) + self.deps
        devdeps = content.get('devDependencies', []) + self.devdeps
        
        content['dependencies'] = deps
        if self.devdeps == ['']:
            pass
        else:
            content['devDependencies'] = devdeps
        
        with open('stackinit.json', 'w') as f:
            json.dump(content, f, indent=4)
        
        print("[green]Success:[/green] Dependencies added to stackinit.json.")  
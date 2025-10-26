import json
from rich import print
import os

class InitExec():
    def __init__(self, project_name, is_new, type, pkgmgr):
        self.project_name = project_name
        self.is_new = is_new
        self.type = type
        self.pkgmgr = pkgmgr

    def run(self):
        if self.is_new:
            self.create_project()

        self.write_json_file()
        

    def create_project(self):
            os.system(f"mkdir {self.project_name}")
            os.chdir(self.project_name)
        
    def write_json_file(self):

        config = {
            "project": {
                "project_name": f"{self.project_name}"
            },
            "settings": {
                "type": f"{self.type}",
                "pkgmgr": f"{self.pkgmgr}"
            },
            "dependencies": {

            },
            "devDependencies": {
                
            }
        }

        with open('stackinit.json', 'w', encoding='utf-8') as file:
            json.dump(config, file, indent=2)

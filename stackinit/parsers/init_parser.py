from rich import print
import os
import json

class InitParser():
    def __init__(self, project_name, is_new, template, pkgmgr):
        self.project_name = project_name
        self.is_new = is_new
        self.template = template
        self.pkgmgr = pkgmgr

        self.data_path = os.path.join(os.path.dirname(__file__), "..", "data", "templates_list.json")


    def run(self):
        print(f"\n{"" if not self.is_new else "New "}{"Project" if not self.is_new else "project"} [bold]{self.project_name}[/bold] will create with\ntemplate: [bold]{self.template}[/bold],\npackage manager: [bold]{self.pkgmgr}[/bold]\n")
        self.check()


    def check(self):
        with open(self.data_path, 'r', encoding='utf-8') as file:
            content = json.load(file)
        
        templates = content.get("templates")


        if self.template not in templates:
            print("There isn`t the same template")
        else:
            print("Succesfuly set template")
            package_manager = templates.get(self.template)
            if self.pkgmgr == "unknown":
                print("Package manager is default")
                self.run_exec()
            else:

                if self.pkgmgr not in package_manager["available_pkgmgr"]:
                    print("There isn`t the same package manager in base")
                else:
                    print("Succesfuly set package manager")
                    self.run_exec()


    def run_exec(self):
        print("run exec has started")
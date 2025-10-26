from rich import print
from ..executors.init_exec import InitExec
import os
import json

class InitParser():
    def __init__(self, project_name, is_new, type, pkgmgr):
        self.project_name = project_name
        self.is_new = is_new
        self.type = type
        self.pkgmgr = pkgmgr

        self.data_path = os.path.join(os.path.dirname(__file__), "..", "data", "types_list.json")


    def run(self):
        self.check()


    def check(self):
        with open(self.data_path, 'r', encoding='utf-8') as file:
            content = json.load(file)
        
        types = content.get("types")


        if self.type not in types:
            print("There isn`t the same type")
        else:
            package_manager = types.get(self.type)
            if self.pkgmgr == "unknown":
                if self.is_new:
                    if os.path.exists(self.project_name):
                        print(f"[red]Directory[/red] [bold red]{self.project_name}[/bold red] [red]is already exists[/red]")
                    else:
                        print(f"\n{"" if not self.is_new else "New "}{"Project" if not self.is_new else "project"} [bold]{self.project_name}[/bold] will create with\ntype: [bold]{self.type}[/bold],\npackage manager: [bold]{self.pkgmgr}[/bold]\n")
                
                        self.run_exec()
                else:
                    print(f"\n{"" if not self.is_new else "New "}{"Project" if not self.is_new else "project"} [bold]{self.project_name}[/bold] will create with\ntype: [bold]{self.type}[/bold],\npackage manager: [bold]{self.pkgmgr}[/bold]\n")

                    self.run_exec()
            else:
                if self.pkgmgr not in package_manager["available_pkgmgr"]:
                    print("There isn`t the same package manager")
                else:
                    if self.is_new:
                        if os.path.exists(self.project_name):
                            print(f"[red]Directory[/red] [bold red]{self.project_name}[/bold red] [red]is already exists[/red]")
                        else:
                            print(f"\n{"" if not self.is_new else "New "}{"Project" if not self.is_new else "project"} [bold]{self.project_name}[/bold] will create with\ntype: [bold]{self.type}[/bold],\npackage manager: [bold]{self.pkgmgr}[/bold]\n")
                            self.run_exec()
                    else:
                        print(f"\n{"" if not self.is_new else "New "}{"Project" if not self.is_new else "project"} [bold]{self.project_name}[/bold] will create with\ntype: [bold]{self.type}[/bold],\npackage manager: [bold]{self.pkgmgr}[/bold]\n")
                        self.run_exec()


    def run_exec(self):
        exec = InitExec(self.project_name, self.is_new, self.type, self.pkgmgr)
        exec.run()
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

    def show_info(self):
        print(f"\n{"" if not self.is_new else "New "}{"Project" if not self.is_new else "project"} [bold]{self.project_name}[/bold] will create with\ntype: [bold]{self.type}[/bold],\npackage manager: [bold]{self.pkgmgr}[/bold]\n")
        
    def check(self):
        with open(self.data_path, 'r', encoding='utf-8') as file:
            content = json.load(file)
            
            
        # types = content.get("types")
        # if self.type not in types:
        #     return print("[red]Error:[/red] [bold red]Project type[/bold red] is not available.")

        # package_info = types[self.type]
        # available_pkgmgr = package_info["available_pkgmgr"]

        # if self.pkgmgr == "unknown":
        #     self.pkgmgr = package_info["default_pkgmgr"]

        # if self.pkgmgr not in available_pkgmgr:
        #     return print("[red]Error:[/red] [bold red]Package manager[/bold red] is not available for this project type.")

        # if self.is_new and os.path.exists(self.project_name):
        #     return print(f"[red]Error:[/red] [bold red]Directory {self.project_name}[/bold red] already exists!")

        self.show_info()
        self.run_exec()


    def run_exec(self):
        exec = InitExec(self.project_name, self.is_new, self.type, self.pkgmgr)
        exec.run()
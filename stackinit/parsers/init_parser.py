from rich import print

class InitParser():
    def __init__(self, project_name, is_new, template, pkgmgr):
        self.project_name = project_name
        self.is_new = is_new
        self.template = template
        self.pkgmgr = pkgmgr

    def run(self):
        print(f"\n{"" if not self.is_new else "New "}{"Project" if not self.is_new else "project"} [bold]{self.project_name}[/bold] will create with\ntemplate: [bold]{self.template}[/bold],\npackage manager: [bold]{self.pkgmgr}[/bold]\n")
        self.check()


    def check(self):
        print("debugger")

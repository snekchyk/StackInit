class AddExec():
    def __init__(self, deps, devdeps):
        self.deps = deps
        self.devdeps = devdeps

    def run(self):
        print("Executing add operation...")
        # Here would be the logic to add dependencies to stackinit.json
        # For example, updating the JSON file with new dependencies
        print(f"Added dependencies: {self.deps}")
        print(f"Added dev dependencies: {self.devdeps}")
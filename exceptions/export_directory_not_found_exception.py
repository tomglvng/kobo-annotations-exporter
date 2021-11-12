class ExportDirectoryNotFound(Exception):
    def __init__(self, message="Export directory not found"):
        self.message = message
        super().__init__(self.message)


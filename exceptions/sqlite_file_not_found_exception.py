class SqliteFileNotFoundException(Exception):
    def __init__(self, message="sqlite file not found"):
        self.message = message
        super().__init__(self.message)


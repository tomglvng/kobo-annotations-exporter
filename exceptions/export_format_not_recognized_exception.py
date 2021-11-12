class ExportFormatNotRecognized(Exception):
    def __init__(self, message="Export format not recognized"):
        self.message = message
        super().__init__(self.message)


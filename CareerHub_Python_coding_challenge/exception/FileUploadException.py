class FileUploadException(Exception):
    """Exception raised for errors in file uploads."""
    def __init__(self, message="Error uploading file. Please check the file and try again."):
        self.message = message
        super().__init__(self.message)

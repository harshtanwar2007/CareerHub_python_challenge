class ApplicationDeadlineException(Exception):
    """Exception raised when an application is submitted after the deadline."""
    def __init__(self, message="Application deadline has passed."):
        self.message = message
        super().__init__(self.message)

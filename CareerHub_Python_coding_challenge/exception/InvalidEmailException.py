class InvalidEmailFormatException(Exception):
    """Exception raised for errors in the input email format."""
    def __init__(self, message="Invalid email format. Please enter a valid email address."):
        self.message = message
        super().__init__(self.message)

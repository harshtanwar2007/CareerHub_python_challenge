class DatabaseConnectionException(Exception):
    """Exception raised for database connection errors."""
    def __init__(self, message="Could not connect to the database. Please try again later."):
        self.message = message
        super().__init__(self.message)

class NegativeSalaryException(Exception):
    """Exception raised for errors in salary calculations."""
    def __init__(self, message="Salary cannot be negative."):
        self.message = message
        super().__init__(self.message)

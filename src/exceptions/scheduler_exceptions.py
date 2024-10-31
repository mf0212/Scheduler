# exceptions/scheduler_exceptions.py

class SchedulerException(Exception):
    """Base exception class for all scheduler-related errors.
    
    This exception serves as the parent class for more specific scheduler exceptions.
    It provides basic functionality for all scheduler errors.
    
    Attributes:
        message (str): Human readable string describing the error
        code (int): Optional error code for categorizing errors
    """
    
    def __init__(self, message: str, code: int = None):
        """Initialize the scheduler exception.
        
        Args:
            message (str): Error message describing what went wrong
            code (int, optional): Error code for categorizing the error
        """
        self.message = message
        self.code = code
        super().__init__(self.message)

class AnalysisError(SchedulerException):
    """Exception raised when availability analysis fails.
    
    This exception is raised when the system fails to analyze user availability
    messages, either due to API failures or invalid message formats.
    
    Attributes:
        message (str): Human readable string describing the error
        original_message (str): The original message that failed analysis
        code (int): Optional error code
    """
    
    def __init__(self, message: str, original_message: str = None, code: int = None):
        """Initialize the analysis error.
        
        Args:
            message (str): Error message describing what went wrong
            original_message (str, optional): The original message that failed analysis
            code (int, optional): Error code for categorizing the error
        """
        self.original_message = original_message
        super().__init__(message, code)
        
    def __str__(self):
        """Return a string representation of the error."""
        base_message = super().__str__()
        if self.original_message:
            return f"{base_message} (Original message: {self.original_message})"
        return base_message

class TimeSuggestionError(SchedulerException):
    """Exception raised when time suggestion generation fails.
    
    This exception is raised when the system fails to generate suitable
    meeting time suggestions based on user availabilities.
    
    Attributes:
        message (str): Human readable string describing the error
        user_count (int): Number of users involved in the scheduling
        code (int): Optional error code
    """
    
    def __init__(self, message: str, user_count: int = None, code: int = None):
        """Initialize the time suggestion error.
        
        Args:
            message (str): Error message describing what went wrong
            user_count (int, optional): Number of users involved in the scheduling
            code (int, optional): Error code for categorizing the error
        """
        self.user_count = user_count
        super().__init__(message, code)
        
    def __str__(self):
        """Return a string representation of the error."""
        base_message = super().__str__()
        if self.user_count is not None:
            return f"{base_message} (Users involved: {self.user_count})"
        return base_message

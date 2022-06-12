class ValueTooSmall(ValueError):
    """Raised when the input value is too small"""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class ValueTooLarge(ValueError):
    """Raised when the input value is too large"""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ComicNotFoundError(Exception):
    def __init__(self, message):
        super().__init__(message)

class NegativeInventoryError(Exception):
    def __init__(self, message):
        super().__init__(message)

class DuplicateISBNError(Exception):
    def __init__(self, message):
        super().__init__(message)

class InvalidDiscountError(Exception):
    def __init__(self, message):
        super().__init__(message)

class ComicNotInStockError(Exception):
    def __init__(self, message):
        super().__init__(message)
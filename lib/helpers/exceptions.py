# Here are all custom exceptions


class InvalidKey(Exception):
    """
    Exception for invalid user input keys values
    """
    def __init__(self, *args):
        self.message = "" + str(args[0]) if args else "Wrong key value."

    def __str__(self):
        return f"{self.message}"

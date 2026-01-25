
from .. import module1  # Relative import: .. means parent package

def subfunc():
    return f"Subfunction calling func1: {module1.func1()}"

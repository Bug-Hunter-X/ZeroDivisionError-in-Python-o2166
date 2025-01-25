def function_with_uncommon_error(x):
    try:
        if x == 0:
            return 1 / x # ZeroDivisionError
        else:
            return x + 1
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
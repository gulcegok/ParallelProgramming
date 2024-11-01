custom_power = lambda x=0, e=1: x ** e

def custom_equation(x: int = 0, y: int = 0, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Calculate the result of the equation (x**a + y**b) / c.
    
    :param x: Integer, positional-only with default value 0
    :param y: Integer, positional-only with default value 0
    :param a: Integer, positional-or-keyword with default value 1
    :param b: Integer, positional-or-keyword with default value 1
    :param c: Integer, keyword-only with default value 1
    :return: Result as a float
    """
    return (x**a + y**b) / c

def fn_w_counter():
    call_count = 0
    caller_count = {}

    def counter():
        nonlocal call_count
        call_count += 1
        caller = "__main__"  
        if caller in caller_count:
            caller_count[caller] += 1
        else:
            caller_count[caller] = 1
        return call_count, caller_count

    return counter


counter_instance = fn_w_counter()
for _ in range(11):
    print(counter_instance())

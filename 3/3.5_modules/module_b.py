# module_b.py
def function_b():
    print("Function B")
    from module_a import function_a
    function_a()

def outer():
    print("Outer function started")

    def inner():
        print("Inner function is executing")

    print("Outer is calling inner function")

    inner()
outer()
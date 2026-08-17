GREETING = "Hey"

def greet(name):
    if not name:
        name = "there"
    return f"{GREETING}, {name}!"
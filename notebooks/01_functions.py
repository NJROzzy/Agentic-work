# default arguments 

def greet(name, excited=False):
    if excited:
        return f"Hey {name} !!"
    return f"Hello,    {name}."

print(greet("John"))
print(greet("John", excited=True))

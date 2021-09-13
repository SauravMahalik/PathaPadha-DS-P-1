class Original():
    def __init__(name):
        name.str1 = ""

    def get_String(name):
        name.str1 = input()

    def print_String(name):
        print(name.str1.upper())

str1 = Original()
str1.get_String()
str1.print_String()

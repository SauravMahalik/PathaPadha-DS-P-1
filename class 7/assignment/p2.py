def function1(): # outer function
    print ("Hello, Outer function")
    def function2(): # inner function
        print ("Hello, Inner function")
    function2()

function1()
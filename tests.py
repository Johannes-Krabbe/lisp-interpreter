from main import interpret

# Helpers
def print_green(s):
    print('\033[92m' + s + '\033[0m')


# Tests
def runTests(): 
    # add test
    assert(interpret("(+ 1 2)") == "3")
    assert(interpret("(+ 10 2)") == "12")
    assert(interpret("(+ (+ 1 1) 1)") == "3")
    assert(interpret("(+ 1 (+ 1 1))") == "3")
    print_green("Tests passed: +")
    
    # bool test
    assert(interpret("(= 1 1)") == True)
    assert(interpret("(= 1 2)") == [])
    print_green("Tests passed: =")

    # print test
    assert(interpret("(print 1)") == True)
    assert(interpret("(print (+ 1 1))") == True)
    print_green("Tests passed: print")

    # list test
    assert(interpret("(list 1 2)") == ["1", "2"])
    print_green("Tests passed: list")

    # first test
    assert(interpret("(first (list 1 2))") == "1")
    print_green("Tests passed: first")

    # last test
    assert(interpret("(last (list 1 2 3))") == ["2", "3"])
    print_green("Tests passed: last")

    # append test
    assert(interpret("(append (list 1 2 3) 4)") == ["1", "2", "3", "4"])
    print_green("Tests passed: append")





if __name__ == "__main__":
    runTests()


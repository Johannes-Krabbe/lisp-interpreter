from main import arrToString, interpret, stringToArr

# Helpers
def print_green(s):
    print('\033[92m' + s + '\033[0m')


# Tests
def runTests(): 
    # add test
    assert(arrToString(["1", "2", "3"]) == "(1 2 3)")
    assert(stringToArr("(1 2 3)") == ["1", "2", "3"])
    print_green("Tests passed: helper functions")

    # add test
    assert(interpret("(+ 1 2)") == "3")
    assert(interpret("(+ 1 2)\n(+ 1 2)") == "3")
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
    assert(interpret("(list 1 2)") == "(1 2)")
    print_green("Tests passed: list")

    # first test
    assert(interpret("(first (list 1 2))") == "1")
    print_green("Tests passed: first")

    # last test
    assert(interpret("(last (list 1 2 3))") == "(2 3)")
    print_green("Tests passed: last")

    # append test
    assert(interpret("(append (list 1 2 3) 4)") == "(1 2 3 4)")
    print_green("Tests passed: append")

    # test define
    assert(interpret("(define a 1)\n(= a 1)") == True)
    assert(interpret("(define b (+ 1 2))\n(= b 3)") == True)
    assert(interpret("(define c (+ 1 2))\n(+ c c)") == "6")
    print_green("Tests passed: define")




if __name__ == "__main__":

    # assert(interpret("(define a (+ 1 2))\n(= a 3)") == True)
    runTests()


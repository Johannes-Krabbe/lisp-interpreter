from main import interpret

# Helpers
def print_green(s):
    print('\033[92m' + s + '\033[0m')


# Tests
def runTests(): 
    # add test
    assert(interpret("(+ 1 2)") == 3)
    assert(interpret("(+ (+ 1 1) 1)") == 3)
    # assert(interpret("(+ 1 (+ 1 1))") == 3)
    print_green("Tests passed: +")
    
    # bool test
    assert(interpret("(= 1 1)") == True)
    assert(interpret("(= 1 2)") == [])
    print_green("Tests passed: =")


    assert(interpret("(print 1)") == True)
    print_green("Tests passed: print")



if __name__ == "__main__":
    runTests()


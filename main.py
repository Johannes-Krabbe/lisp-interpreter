from ast import operator


def interpret(input):
    if input[0] != "(":
        raise Exception("missing '(' at beginning of statement")
        return
    
    input_arr = input.split(" ")
    for s in input_arr:
        s = s.replace("", " ")
    
    out = t(input_arr)
    return out

    
def t(input_arr):    
    in_operator = input_arr.pop(0)
    in_operator = in_operator.replace("(", "")

    oper = None

    for o in operators:
        if o["ident"] == in_operator:
            oper = o

    if(oper == None):
        raise Exception("operator does not exist: " + in_operator)
        return

    params = []
    
    for _ in range(len(input_arr)):
        if(input_arr[0][0] == "("):
            params.append(t(input_arr))
        else:
            tmp = None
            if(input_arr[0][-1] == ")"):
                tmp = input_arr.pop(0).replace(")", "")
                params.append(tmp)
                break
            else:
                tmp = input_arr.pop(0)
                params.append(tmp)


    out = oper["function"](params)
    print(out)
    return out

# functions
def add(inp):
    return int(inp[0]) + int(inp[1])

def comp(inp):
    if(inp[0] == inp[1]):
        return True
    else:
        return []

def consoleLog(s):
    print(s[0])
    return True

# constants

operators = [
    {
        "ident" : "+",
        "varCount": 2,
        "function": add 
    },
    {
        "ident" : "=",
        "varCount": 2,
        "function": comp
    },
    {
        "ident": "print",
        "varCount": 1,
        "function": consoleLog
    },
    {
        "ident": "list",
        "varCount": 1,
        "function": consoleLog
    }
]

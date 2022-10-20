from ast import operator

definitions = {}

def interpret(input):
    if input[0] != "(":
        raise Exception("missing '(' at beginning of statement")
        return
    

    lines = input.split("\n")
    
    out = []

    for l in lines:
        input_arr = l.split(" ")
    
        out.append(t(input_arr))

    return out[-1]

    
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
    
    while(len(input_arr) != 0):
        if(input_arr[0][0] == "("):
            params.append(t(input_arr))
        else:
            tmp = None
            if(input_arr[0][-1] == ")"):
                tmp = input_arr.pop(0)
                if(tmp.count(")") > 1):
                    input_arr.insert(0, tmp[tmp.find(")")+1:])                      
                params.append(tmp.replace(")", ""))
                break
            else:
                tmp = input_arr.pop(0)
                params.append(tmp)


    for i in range(len(params)):
        if params[i] in definitions.keys():
            params[i] = definitions[params[i]]

    out = oper["function"](params)
    return out

# helpers
def arrToString(inp):
    out = "(" + inp.pop(0) 

    for item in inp:
        out = out + " " + item

    out =  out + ")"

    return out

def stringToArr(inp):
    return inp.replace(")", "").replace("(", "").split(" ")

# functions
def add(inp):
    return str(int(inp[0]) + int(inp[1]))

def comp(inp):
    if(inp[0] == inp[1]):
        return True
    else:
        return []

def consoleLog(inp):
    print(inp[0])
    return True

def createList(inp):
    return arrToString(inp) 

def first(inp):
    return stringToArr(inp[0])[0]

def last(inp):
    tmp = stringToArr(inp[0])
    tmp.pop(0)
    return arrToString(tmp)

def listAppend(inp):
    tmp = stringToArr(inp[0])
    tmp.append(inp[1])
    return arrToString(tmp)

def define(inp):
    definitions[inp[0]] = inp[1]

# constants

operators = [
    {
        "ident" : "+",
        "function": add 
    },
    {
        "ident" : "=",
        "function": comp
    },
    {
        "ident": "print",
        "function": consoleLog
    },
    {
        "ident": "list",
        "function": createList
    },
    {
        "ident": "first",
        "function": first
    },
    {
        "ident": "last",
        "function": last
    },
    {
        "ident": "append",
        "function": listAppend
    },
    {
        "ident": "define",
        "function": define 
    },
]

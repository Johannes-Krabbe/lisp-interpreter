definitions = {}

def interpret(input):
    if input[0] != "(":
        raise Exception("missing '(' at beginning of statement")

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

    if(oper["ident"] == "lambda"):
        inParams = []
        while(input_arr[0].count(")") == 0):
            inParams.append(input_arr.pop(0).replace("(", ""))            
        inParams.append(input_arr.pop(0).replace(")", ""))            

        params.append(inParams)

        closeBrCount = -1

        funcContent = []
        
        while closeBrCount != 0:
            funcContent.append(input_arr.pop(0))            
            closeBrCount = closeBrCount + funcContent[-1].count(")")
            closeBrCount = closeBrCount - funcContent[-1].count("(")

        funcContent[-1] = funcContent[-1][:-1]

        params.append(funcContent)    
        out = oper["function"](params)
        return out

    
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
        return "()"

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

def ifFunc(inp):
    if(inp[0] == True):
        return inp[1]
    return inp[2]

def lambdaFunc(inp):
    print(inp)

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
    {
        "ident": "if",
        "function": ifFunc
    },
    {
        "ident": "lambda",
        "function": lambdaFunc
    },
]

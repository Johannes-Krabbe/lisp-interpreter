from ast import operator


def interpret(input):
    if input[0] != "(":
        raise Exception("missing '(' at beginning of statement")
        return
    
    input_arr = input.split(" ")
    in_operator = input_arr[0][1:]
    
    oper = None

    for o in operators:
        if o["ident"] == in_operator:
            oper = o

    if(oper == None):
        raise Exception("operator does not exist: " + in_operator)
        return

    out = oper["function"](int(input_arr[1]), int(input_arr[2][:1]))

    return out


def add(in1, in2):
    return in1 + in2

def comp(in1, in2):
    if(in1 == in2):
        return True
    else:
        return []


# constants

operators = [
    {
        "name" : "add",
        "ident" : "+",
        "function": add 
    },
    {
        "name" : "comp",
        "ident" : "=",
        "function": comp
    }
]

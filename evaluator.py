def isbasic(string):
    for i in string:
        if (not i.isdigit() and i not in ["+", "-", "/", "*", "^", ".", "(", ")", "e"]):
            return False
    return True

def firstPr(string):
    k, j= 0, 0
    arr = []
    for i in string:
        if i == "(" and j == 0:k = 1
        if i == "(": j+=1
        if i == ")": j-=1
        if k == 1:
            arr.append(i)
        if j == 0 and k == 1:
            arr.pop(0);arr.pop(-1)
            return "".join(arr)
    return ""
def num(string):
    point = 0
    num_arr = [str(i) for i in range(0, 10)]
    num_arr.append("j")
    j = -1
    for i in string:
        j += 1
        if i not in num_arr:
            if i == ".": point += 1
            elif i == "-" and j != 0: return 0
            elif i == "-" : continue
            else: return 0
    if point > 1 : return 0
    return 1
def isspec(c):
    if 33<=ord(c)<=47 and ord(c) not in [40, 41]:
        return 1
    if ord(c) == 94:
        return 1
    if c == "_":
        return 1
    return 0
def isnumber(c):
    if 48<=ord(c)<=57:
        return 1
    return 0

def ins_star(string):
    new_string = string[:]
    k = len(new_string) - 1
    i = 0
    while i < k:
        if isnumber(new_string[i]) + isnumber(new_string[i+1]) == 1:
            if new_string[i+1] != ")" and new_string[i] != "(" :
                if isspec(new_string[i]) + isspec(new_string[i+1]) == 0:
                    new_string = new_string[:i+1] + "*" + new_string[i+1:]
                    k+=1
        if new_string[i] == ")" and 97<=ord(new_string[i+1])<=122:
            new_string = new_string[:i+1] + "*" + new_string[i+1:]
            k+=1
        i += 1
    return new_string

def evaluate(string):
    nstr = ins_star(string)
    nstr2 = nstr.replace("^", "**")
    text = '''
from math import *
result=%s
    '''%nstr2
    with open("script.py", "w") as file:
        file.write("".join(text))
        file.close()
    
    import script
    res = script.result
    del script

    return res

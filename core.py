import math
import random
import latexify


class num:
    def __init__(self, n):
        self.num = n 
    
    def __add__(self, other):
        return num(self.num + other.num)

    def __mul__(self, other):
        return num(self.num * other.num)

    def __div__(self, other):
        return num(self.num / other.num)

    def __neg__(self, other):
        return num(-self.num)

    def __pow__(self, other):
        return num(self.num ** other.num)
    
    def __call__(self):
        return self.num
    
    def __int__(self):
        return int(self.num)
    
    def __float__(self):
        return float(self.num)
    
    def __str__(self):
        return str(self.num)
    
    def zero(self):
        return num(0)
    
    def diff(self):
        return num(0)

class defaultInp:
    def __init__(self):
          self.sym = "x"
    def __call__(self, x):
        return x
    def __str__(self):
        return self.sym
    
    def __add__(self, other):
        return polyexpr([self, other])
    
    def __mul__(self, other):
        return mixedmulexpr([self, other])
    
    def __neg__(self):
        return mixedmulexpr([self, poly([-1])])
    
    def __sub__(self, other):
        return self + (-other)
    
    
    def diff(self):
        return 1
    
class poly:
    def __init__(self, array, inp=defaultInp()):
        self.array = array
        self.normalize()
        self.deg = len(self.array) - 1
        self.inp = inp

    def __str__(self):
        string = []
        for i in range(self.deg + 1):
            if i < self.deg:
                if i > 1:
                    if self.array[i] == 0:
                        continue;
                    elif self.array[i] == 1 or self.array[i] == -1:
                        string += ["%s%s^%d"%("+" if self.array[i] == 1 else "-", str(self.inp), i)]
                    else:
                        string += ["%s%s%s^%d"%("+" , str(self.array[i]), str(self.inp), i)]
                elif i == 1:
                    if self.array[i] == 0:
                        continue;
                    elif self.array[i] in [1, -1]:
                        string += ["%s%s"%("+" , str(self.inp))]
                    else:
                        string += ["%s%s%s"%("+" ,str(self.array[i]), str(self.inp))]
                elif i == 0:
                    if self.array[i] == 0:
                        continue;
                    string += ["%s%s"%("+" , str(self.array[i]))]
            
            else:
                if i > 1:
                    if self.array[i] == 0:
                        continue;
                    elif self.array[i] in [1, -1]:
                        string += ["%s%s^%d"%("+" ,str(self.inp), i)]
                    else:
                        string += ["%s%s%s^%d"%("+", str(self.array[i]), str(self.inp), i)]
                elif i == 1:
                    if self.array[i] == 0:
                        continue;
                    elif self.array[i] in [1, -1]:
                        string += ["%s%s"%("+", str(self.inp))]
                    else:
                        string += ["%s%s%s"%("+",str(self.array[i]), str(self.inp))]
                elif i == 0:
                    if self.array[i] == 0:
                        continue;
                    string += ["%s%s "%("+", str(self.array[i]))]

        string.reverse()
        return "".join(string)

    def __add__(self, other):
        if isinstance(other, poly):
            res = []
            if self.deg < other.deg :
                new_self =  self.array[:]+[0 for i in range(other.deg - self.deg)]
                new_other = other.array[:]
            
            else:
                new_other = other.array[:] + [0 for i in range(self.deg - other.deg)]
                new_self = self.array[:]
            
            for i in range(len(new_other)):
                res.append(new_other[i] + new_self[i])
            
            return poly(res[:])
        
        else:
            return self + poly([other])

    def __sub__(self, other):
        return self + (-other)
    
    def __mul__(self, other):
        if isinstance(other, poly):
            res = [0 for i in range(self.deg + other.deg + 1)]
            for i in range(self.deg + 1):
                for j in range(other.deg + 1):
                    res[i + j] += self.array[i] * other.array[j]
            
            return poly(res[:])
        
        if isinstance(other, (num, int, float)):
            return poly([i * float(other) for i in self.array])
        
        else:
            return other * self

    def __pow__(self, other):
        if isinstance(other, (num, int, float)):
            if float(other) - int(other) == 0:
                prod = poly([1])
                for i in range(int(other)):
                    prod *= self
                return prod 
               
    def __call__(self, x):
        #s = x.zero() if not isinstance(x, (int, float)) else 0
        s = 0
        for i in range(self.deg + 1):
            if isinstance(self.array[i], (int, float)):
                s += self.inp(x) ** i * self.array[i] 
            
            else:
                s += self.inp(x) ** i * (self.array[i](x)) 
        
        return s
    def __neg__(self):
        return self * (-1)
    def __eq__(self, other):
        return self.array == other.array

    def zero(self):
        return poly([0])
    
    def diff(self):
        return poly([self.inp.diff() * self.array[i+1] * poly([i+1]) for i in range(self.deg)], inp=self.inp)
    
    def normalize(self):
        for i in range(len(self.array)):
            if self.array[i:] == [0 for i in range(len(self.array) - i)]:
                new_array = self.array[:i]
                self.array[:] = new_array[:]
                return

class ratio:
    """ratio = p(x)/q(x) -> self.p / self.q"""
    def __init__(self, p, q):
        self.p = p
        self.q = q
    
    def __add__(self, other):
        if isinstance(other, ratio):
            return ratio(self.p * other.q + other.p * self.q, self.q * other.q)

        else:
            return ratio(self.p + self.q * other, self.q)
    
    def __mul__(self, other):
        if isinstance(other, ratio):
            return ratio(self.p * other.p, self.q * other.q)

        else:
            return ratio(self.p * other, self.q)
    
    def __div__(self, other):
        if isinstance(other, ratio):
            return ratio(self.p * other.q, self.q * other.p)

        else:
            return ratio(self.p, self.q * other)
    
    def __neg__(self):
        return ratio(-self.p, self.q)
    
    def __sub__(self, other):
        return self + (-other)
    
    def __call__(self, x):
        return self.p(x) / self.q(x)
    
    def __pow__(self, other):
        if isinstance(self, int):
            prod = ratio(poly([1]), poly([1]))
            for i in range(other):
                prod *= self
            
            return prod
        
        else:
            return monoexpr(self, other)
    
    def __eq__(self, other):
        return self.p*other.q == self.q*other.p
    
    def __str__(self):
        return "(" + str(self.p) + ")/(" + str(self.q) + ")"
    
    def diff(self):
        return ratio(self.p.diff() * self.q - self.p * self.q.diff(), self.q ** 2)

class exp:
    def __init__(self, inp):
        self.inp = inp 
    
    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            return exp(self.inp + other.inp)
        
        else:
            return mixedmulexpr([self, poly([other])])
    
    def __str__(self):
        return "exp(%s)"%str(self.inp)
    
    def __call__(self, x):
        return math.exp(self.inp(x))
    
    def __pow__(self, other):
        return exp(self.inp * other)
    
    def __add__(self, other):
        return polyexpr([self, other])
    
    def __neg__(self):
        return mixedmulexpr([self, poly([-1])])
    
    def __sub__(self, other):
        return self + (-other)
        

    def diff(self):
        return exp(self.inp) * self.inp.diff() 


class log:
    def __init__(self, inp):
        self.inp = inp 

    def __add__(self, other):
        if isinstance(other, log):
            return log(self.arg * other.arg)

        else:
            return log(self.arg * exp(other))

    def __mul__(self, other):
        return log(self.arg ** other)

    def __neg__(self):
        return log(self.arg) * (-1)
    
    def __sub__(self, other):
        return self + (-other)
    
    def __str__(self):
        return "log(%s)"%str(self.inp)
    
    def __call__(self, x):
        return math.log(self.inp(x))  

    def __pow__(self, other):
        return monoexpr(self, other)    
    
    def diff(self):
        return  monoexpr(self.inp, -1) * self.inp.diff()



class monoexpr:
    def __init__(self, expr, pow):
        self.expr = expr
        self.pow = pow
    
    def __mul__(self, other):
        if isinstance(other, monoexpr):
            if other.pow == self.pow:
                return monoexpr(self.expr * other.expr, self.pow)
            
            elif other.expr == self.expr:
                return monoexpr(self.expr, self.pow + other.pow)
            
            else:
                return mixedmulexpr([self, other])
        
        #elif isinstance(other, (int, float)):
        #    return monoexpr(self.expr * other ** (1/self.pow), self.pow)
        elif isinstance(other, (int, float)):
            return mixedmulexpr([self, poly([other])])
        
        else:
            return mixedmulexpr([self, other])

    def __add__(self, other):
        return polyexpr([self, other])
    
    def __div__(self, other):
        return self * monoexpr(other.expr, -other.pow)
    
    def __str__(self):
        return "(" + str(self.expr) + ")^" + str(self.pow)
    
    def __pow__(self, other):
        return monoexpr(self.expr, self.pow * other)
    
    def __call__(self, x):
        return self.expr(x) ** self.pow
    
    def diff(self):
        return monoexpr(self.expr, self.pow - 1) * self.expr.diff() * self.pow
    
class mixedmulexpr:
    def __init__(self, expr_array):
        for i in expr_array:
            if i is None:
                self.expr_arr[:] = [poly([0])]
                break
        else:
            self.expr_arr = expr_array[:]


    def __neg__(self):
        narr = self.expr_arr[:]
        narr[0] = -narr[0]
        return polyexpr(narr)
    
    def __mul__(self, other):  
        if isinstance(other, mixedmulexpr):
            return mixedmulexpr(self.expr_arr[:] + other.expr_arr[:])

        elif isinstance(other, (int, float)):
            return mixedmulexpr(self.expr_arr[:] + [poly([other])])
        
        else:
            return mixedmulexpr(self.expr_arr[:] + [other])
    
    def __pow__(self, other):
        new_arr = [i ** other for i in self.expr_arr]
        return mixedmulexpr(new_arr[:])
    
    def __add__(self, other):
        return polyexpr([self, other])
    
    def __call__(self, x):
        prod = 1
        for i in self.expr_arr:
            if isinstance(i, (int, float)):
                prod = i * prod
            
            else:
                prod = i(x) * prod
        return prod
    
    def __str__(self):
        string = []
        for i in self.expr_arr:
            string.append("("+str(i)+")")
            if string[-1] == "()":
                return ""
        
        return "".join(string)
    
    def diff(self):
        return polyexpr([mixedmulexpr(self.expr_arr[:i]+[self.expr_arr[i].diff()]+self.expr_arr[i+1:]) for i in range(len(self.expr_arr))])


class polyexpr:
    def __init__(self, expr_array):
        self.expr_arr = expr_array[:]
    
    def __add__(self, other):
        if isinstance(other, polyexpr):
            return polyexpr(self.expr_arr[:] + other.expr_arr[:])

        else:
            new_arr = self.expr_arr[:]
            new_arr.append(other)
            return polyexpr(new_arr[:])

    def __neg__(self):
        return polyexpr([-i for i in self.expr_arr])
    
    def __mul__(self, other):
        if isinstance(other, polyexpr):
            arr = []
            for i in range(len(self.expr_arr)):
                for j in range(len(other.expr_arr)):
                    arr.append(self.expr_arr[i] * other.expr_arr[j])
            
            return polyexpr(arr[:])
        
        else:
            arr = []
            for i in self.expr_arr:
                arr.append(other * i)
            
            return polyexpr(arr[:])
    
    def __sub__(self, other):
        return self + (-other)
    
    def __call__(self, x):
        s = 0
        for i in self.expr_arr:
            s = i(x) + s
        #return sum([i(x) for i in self.expr_arr])
        return s
    def __str__(self):
        string = []
        for i in self.expr_arr:
            string.append(str(i))
        
        return "+".join(string)
    
    def diff(self):
        return polyexpr([i.diff() for i in self.expr_arr])
    
        
        
class sin:
    def __init__(self, inp):
        self.inp = inp
    def __call__(self, x):
        return math.sin(self.inp(x))
    
    def __str__(self):
        return "sin(%s)"%str(self.inp)
    
    def __add__(self, other):
        return polyexpr([self, other])
    
    def __mul__(self, other):
        return mixedmulexpr([self, other])
    
    def __pow__(self, other):
        return monoexpr(self, other)
    
    def __neg__(self):
        return mixedmulexpr([self, poly([-1])])
    
    def __sub__(self, other):
        return self + (-other)
    
    def diff(self):
        return  cos(self.inp) * self.inp.diff() 

class cos:
    def __init__(self, inp):
        self.inp = inp
    def __call__(self, x):
        return math.cos(self.inp(x))
    
    def __str__(self):
        return "cos(%s)"%str(self.inp)
    
    def __add__(self, other):
        return polyexpr([self, other])
    
    def __mul__(self, other):
        return mixedmulexpr([self, other])
    
    def __pow__(self, other):
        return monoexpr(self, other)
    
    def __neg__(self):
        return mixedmulexpr([self, poly([-1])])
    
    def __sub__(self, other):
        return self + (-other)
    
    def diff(self):
        return  -sin(self.inp) * self.inp.diff()
    
class tan:
    def __init__(self, inp):
        self.inp = inp
    def __call__(self, x):
        return math.tan(self.inp(x))
    
    def __str__(self):
        return "tan(%s)"%str(self.inp)
    
    def __add__(self, other):
        return polyexpr([self, other])
    
    def __mul__(self, other):
        return mixedmulexpr([self, other])
    
    def __pow__(self, other):
        return monoexpr(self, other)
    
    def __neg__(self):
        return mixedmulexpr([self, poly([-1])])
    
    def __sub__(self, other):
        return self + (-other)
    
    def diff(self):
        return  monoexpr(cos(self.inp), -2) * self.inp.diff() 

class cot:
    def __init__(self, inp):
        self.inp = inp
    def __call__(self, x):
        return 1 / math.tan(self.inp(x))
    
    def __str__(self):
        return "cot(%s)"%str(self.inp)
    
    def __add__(self, other):
        return polyexpr([self, other])
    
    def __mul__(self, other):
        return mixedmulexpr([self, other])
    
    def __pow__(self, other):
        return monoexpr(self, other)
    
    def __neg__(self):
        return mixedmulexpr([self, poly([-1])])
    
    def __sub__(self, other):
        return self + (-other)
    
    def diff(self):
        return  monoexpr(sin(self.inp), -2) * -self.inp.diff()

class asin:
    def __init__(self, inp):
        self.inp = inp
    def __call__(self, x):
        return math.asin(self.inp(x))
    
    def __str__(self):
        return "arcsin(%s)"%str(self.inp)
    
    def __add__(self, other):
        return polyexpr([self, other])
    
    def __mul__(self, other):
        return mixedmulexpr([self, other])
    
    def __pow__(self, other):
        return monoexpr(self, other)
    
    def __neg__(self):
        return mixedmulexpr([self, poly([-1])])
    
    def __sub__(self, other):
        return self + (-other)
    
    def diff(self):
        return monoexpr(poly([1, 0, -1]), -1/2) * self.inp.diff()

class acos:
    def __init__(self, inp):
        self.inp = inp
    def __call__(self, x):
        return math.acos(self.inp(x))
    
    def __str__(self):
        return "arcsin(%s)"%str(self.inp)
    
    def __add__(self, other):
        return polyexpr([self, other])
    
    def __mul__(self, other):
        return mixedmulexpr([self, other])
    
    def __pow__(self, other):
        return monoexpr(self, other)
    
    def __neg__(self):
        return mixedmulexpr([self, poly([-1])])
    
    def __sub__(self, other):
        return self + (-other)
    
    def diff(self):
        return  monoexpr(poly([1, 0, -1]), -1/2) * -self.inp.diff() 

class atan:
    def __init__(self, inp):
        self.inp = inp
    def __call__(self, x):
        return math.atan(self.inp(x))
    
    def __str__(self):
        return "arctan(%s)"%str(self.inp)
    
    def __add__(self, other):
        return polyexpr([self, other])
    
    def __mul__(self, other):
        return mixedmulexpr([self, other])
    
    def __pow__(self, other):
        return monoexpr(self, other)
    
    def __neg__(self):
        return mixedmulexpr([self, poly([-1])])
    
    def __sub__(self, other):
        return self + (-other)
    
    def diff(self):
        return  monoexpr(poly([1, 0, 1]), 1) * self.inp.diff()

class acot:
    def __init__(self, inp):
        self.inp = inp
    def __call__(self, x):
        return math.atan(1 / self.inp(x))
    
    def __str__(self):
        return "arccot(%s)"%str(self.inp)
    
    def __add__(self, other):
        return polyexpr([self, other])
    
    def __mul__(self, other):
        return mixedmulexpr([self, other])
    
    def __pow__(self, other):
        return monoexpr(self, other)
    
    def __neg__(self):
        return mixedmulexpr([self, poly([-1])])
    
    def __sub__(self, other):
        return self + (-other)
    
    def diff(self):
        return  mixedmulexpr([monoexpr(poly([1, 0, 1]), -1), monoexpr(poly([0, 0, 1]), 1)]) * self.inp.diff()
class sinh:
    def __init__(self, inp):
        self.inp = inp
    def __call__(self, x):
        return math.sinh(self.inp(x))
    
    def __str__(self):
        return "sinh(%s)"%str(self.inp)
    
    def __add__(self, other):
        return polyexpr([self, other])
    
    def __mul__(self, other):
        return mixedmulexpr([self, other])
    
    def __pow__(self, other):
        return monoexpr(self, other)
    
    def __neg__(self):
        return mixedmulexpr([self, poly([-1])])
    
    def __sub__(self, other):
        return self + (-other)
    
    def diff(self):
        return  cosh(self.inp) * self.inp.diff() 
class cosh:
    def __init__(self, inp):
        self.inp = inp
    def __call__(self, x):
        return math.cosh(self.inp(x))
    
    def __str__(self):
        return "cosh(%s)"%str(self.inp)
    
    def __add__(self, other):
        return polyexpr([self, other])
    
    def __mul__(self, other):
        return mixedmulexpr([self, other])
    
    def __pow__(self, other):
        return monoexpr(self, other)
    
    def __neg__(self):
        return mixedmulexpr([self, poly([-1])])
    
    def __sub__(self, other):
        return self + (-other)
    
    def diff(self):
        return  sinh(self.inp) * self.inp.diff()
class tanh:
    def __init__(self, inp):
        self.inp = inp
    def __call__(self, x):
        return math.tanh(self.inp(x))
    
    def __str__(self):
        return "tanh(%s)"%str(self.inp)
    
    def __add__(self, other):
        return polyexpr([self, other])
    
    def __mul__(self, other):
        return mixedmulexpr([self, other])
    
    def __pow__(self, other):
        return monoexpr(self, other)
    
    def __neg__(self):
        return mixedmulexpr([self, poly([-1])])
    
    def __sub__(self, other):
        return self + (-other)
    
    def diff(self):
        return  monoexpr(cosh(self.inp), -2) * self.inp.diff()

class asinh:
    def __init__(self, inp):
        self.inp = inp
    def __call__(self, x):
        return math.asinh(self.inp(x))
    
    def __str__(self):
        return "asinh(%s)"%str(self.inp)
    
    def __add__(self, other):
        return polyexpr([self, other])
    
    def __mul__(self, other):
        return mixedmulexpr([self, other])
    
    def __pow__(self, other):
        return monoexpr(self, other)
    
    def __neg__(self):
        return mixedmulexpr([self, poly([-1])])
    
    def __sub__(self, other):
        return self + (-other)
    
    def diff(self):
        return  monoexpr(poly([1, 0, 1]), -1/2) * self.inp.diff() 

class acosh:
    def __init__(self, inp):
        self.inp = inp
    def __call__(self, x):
        return math.acosh(self.inp(x))
    
    def __str__(self):
        return "acosh(%s)"%str(self.inp)
    
    def __add__(self, other):
        return polyexpr([self, other])
    
    def __mul__(self, other):
        return mixedmulexpr([self, other])
    
    def __pow__(self, other):
        return monoexpr(self, other)
    
    def __neg__(self):
        return mixedmulexpr([self, poly([-1])])
    
    def __sub__(self, other):
        return self + (-other)
    
    def diff(self):
        return  monoexpr(poly([-1, 0, 1]), -1/2) * self.inp.diff() 

class atanh:
    def __init__(self, inp):
        self.inp = inp
    def __call__(self, x):
        return math.atanh(self.inp(x))
    
    def __str__(self):
        return "atanh(%s)"%str(self.inp)
    
    def __add__(self, other):
        return polyexpr([self, other])
    
    def __mul__(self, other):
        return mixedmulexpr([self, other])
    
    def __pow__(self, other):
        return monoexpr(self, other)
    
    def __neg__(self):
        return mixedmulexpr([self, poly([-1])])
    
    def __sub__(self, other):
        return self + (-other)
    
    def diff(self):
        return  monoexpr(poly([1, 0, -1]), -1) * self.inp.diff() 

FUNCTION_ID_ARRAY = {
    1 : exp,
    2 : log,
    3 : sin,
    4 : cos,
    5 : tan,
    6 : cot,
    7 : asin,
    8 : acos,
    9 : atan,
    10 : acot,
    11 : sinh,
    12 : cosh,
    13 : tanh,
    14 : asinh,
    15 : acosh,
    16 : atanh,
}
def multdiff(function, n):
    if n == 0:
        return function
    if n == 1:
        return function.diff()
    else:
        return multdiff(function.diff(), n-1)

def generate_random_poly(ranges=[1,9], deg=5, inp=defaultInp()):
    return poly([random.randint(ranges[0], ranges[1]) * (-1)**(random.randint(1, 2)) for i in range(deg + 1)], inp=inp)

def generate_random_term(current_term, depth=3):
    if depth == 1:
        x = current_term(generate_random_poly(ranges=[1,9], deg=random.randint(0, 2), inp=FUNCTION_ID_ARRAY[random.randint(1, 10)](defaultInp())))
    if depth == 2:
        x = current_term(generate_random_poly(ranges=[1,9], deg=random.randint(0, 2), inp=FUNCTION_ID_ARRAY[random.randint(1, 16)](generate_random_poly(ranges=[1,9], deg=3, inp=FUNCTION_ID_ARRAY[random.randint(1, 16)](defaultInp())))))
    if depth == 3:
        dp = random.random(1, 10) % 2 + 1
        return generate_random_term(current_term, depth=dp)
    return x

def generate_random_mixedmulexpr(n=2, depth=1):
    return mixedmulexpr([generate_random_term(defaultInp(), depth=depth) for i in range(n)])

def generate_random_function(n=2, m=2, depth=1):
    return polyexpr([generate_random_mixedmulexpr(n=m, depth=depth) for i in range(n)])

def generate_differential_equation(degree, n=2, m=2, depth=1):
    solution = generate_random_function(n=n, m=m, depth=depth)

    coeffs = [generate_random_function(n=n, m=m, depth=depth) for i in range(degree + 1)]
    answer = []
    for i in range(len(coeffs)):
        answer.append(multdiff(solution, i) * coeffs[i])
    
    ans = polyexpr(answer[:])
    
    string = []

    for i in range(len(coeffs)):
        subs = ""
        for j in range(i):
            subs += "'"
        string.append( " + (%s)y%s"%(str(coeffs[i]), subs))
    string.reverse()
    string.append( " = %s"%(str(ans)))
    #print(string)
    #print("####################################")
    #print("solution : %s"%str(solution))
    #print("####################################")
    return ["".join(string), str(solution), solution]

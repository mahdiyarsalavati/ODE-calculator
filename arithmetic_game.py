import core
import random 
import time
import os
import evaluator
import texrender
import latexify

def multiplicationGame(start, end, n=5):
	score = 0
	for i in range(n):
		n1 = random.randint(start, end)
		n2 = random.randint(start, end)
		n3 = int(input("%s * %s = "%(n1, n2)))
		if n3 == n1 * n2:
			print("Correct.")
			score += 1
		else :
			print("Incorrect. The answer was ", n1*n2)
	return score

def generate_random_matrix(start, end, dim):
	arr = []
	for i in range(dim):
		row = []
		for j in range(dim):
			row.append(random.randint(start, end))
		arr.append(row)
	return arr
def generate_random_matrix_poly(start, end, max_deg, dim):
	arr = []
	for i in range(dim):
		row = []
		for j in range(dim):
			row.append(core.generate_random_poly(ranges=[start, end], deg=random.randint(0, max_deg)))#(random.randint(start, end))
		arr.append(row)
	return arr
def printMatrix(array):
	new_arr = []
	longest_length = 0
	for i in array:
		z = []
		for j in i:
			s = str(j)
			if len(s) > longest_length:
				longest_length = len(s)
			z.append(s)

		new_arr.append(z)
	for i in new_arr:
		for j in range(len(i)):
			x = ""
			for k in range(int((longest_length - len(i[j]))/2)):
				x += " "
			print(x, i[j], x, " " if longest_length - len(i[j]) % 2 == 1 else "",  ", " if j != len(i) - 1 else "", end="")
		print("\n")
			
	return
def minor(array, pos):
	new_arr = []
	for i in range(len(array)):
		col = []
		if i == pos[0]:
			continue

		for j in range(len(array[i])):
			if j != pos[1]:
				col.append(array[i][j])

		new_arr.append(col)

	return new_arr

def det(array):
	if len(array) == 1:
		return array[0][0]

	else:
		a = []
		for i in range(len(array)):
			a.append(array[0][i] * det(minor(array, [0, i])) * (-1)**(i))
		
		z = a[0]
		for i in range(1, len(a)):
			z+=a[i]
		return z
		
def matrixGame(start, end, dim, n=5):
	score = 0
	for i in range(n):
		b=generate_random_matrix(start, end, dim)
		n1 = det(b)
		printMatrix(b)
		n2 = int(input("det = "))
		if n1 == n2:
			print("Correct.")
			score += 1
		else:
			print("Incorrect. The answer was : ", n1)
	return score 
def polyMatrixGame(start, end, max_deg, inp_rng,  dim, n=5):
	score = 0
	for i in range(n):
		b=generate_random_matrix_poly(start, end, max_deg, dim)
		n1 = det(b)
		printMatrix(b)
		z = random.randint(inp_rng[0], inp_rng[1])
		n2 = int(input("What is the value of the determinant at x = %d ?\n"% z))
		if n1(z) == n2:
			print("Correct. The polynomial was : ", str(n1))
			score += 1
		
		else:
			print("Incorrect. The polynomial was : \n %s \n The answer was %d\n"%(str(n1), n1(z)))
	return score 
def numberGame():
	score = 0
	i = 1
	while True:
		n = random.randint(10 ** (i-1), 10 ** (i) - 1)
		os.system("clear")
		print(n)
		time.sleep(2+0.8*(i-1))
		os.system("clear")
		n1 = int(input("Enter the number : "))
		if n1 != n:
			break
		score += 1
		i += 1
	
	return score

def definiteIntegralGame(n=5, depth=1):
	score = 0
	answers = []
	def generate_term():
		try:
			anti_derivative = core.generate_random_function(n=1, m=1, depth=depth)
			function = anti_derivative.diff()
			a, b = random.randint(0, 9), random.randint(0, 9)
			res = anti_derivative(max(a,b)) - anti_derivative(min(a,b))
			answers.append(round(res, 2))
		except:
			return generate_term()
		return [anti_derivative, function, a, b, res]
	for i in range(n):
		'''
		anti_derivative = core.generate_random_function(n=2, m=2)
		function = anti_derivative.diff()
		a, b = random.randint(0, 9), random.randint(0, 9)
		res = anti_derivative(max(a,b)) - anti_derivative(min(a,b))
		'''
		anti_derivative, function, a, b, res = generate_term()
		print("Find the integral of the following from %d to %d : "%(min(a,b), max(a,b)))
		print(str(function))
		texrender.render_tex_image(r'\int_%d^%d'%(min(a,b), max(a,b)) + latexify.convert_to_latex(str(function))+r'dx')
		
		if round(res, 2) == round(evaluator.evaluate(input()), 2):
			score += 1
	
	return [score, answers]

def differentialEquationGame(n=5, depth=1):
	score = 0
	answers = []
	for i in range(n):
		eq, sol_str, sol = core.generate_differential_equation(2, n=1, m=1, depth=depth)
		a = round(random.random(), 1)
		print("Evaluate the answer of the following equation at x = %f"%a)
		print(str(eq))
		texrender.render_tex_image(latexify.convert_to_latex(str(eq)))
		print("The solution is : %s"%sol_str)
		x = round(sol(evaluator.evaluate(input())), 2)
		if round(sol(a), 2) == x:
			score += 1
		
		answers.append(round(sol(a), 2))
	
	return [score, answers]




while True:
	n = int(input("1-Mul    2-Det   3-Det Poly 4-num   5-Int   6-DE\n"))
	os.system("clear")
	if n == 4:
		print("score : ", numberGame())
	
	else:
		if n == 5:
			y = int(input("Enter the number of rounds : "))
			z = int(input("Enter depth (1 or 2): "))
			start = time.time()
			score, answers = definiteIntegralGame(n=y, depth=z)
			end = time.time()
			print("score : ", score, "/%d"%y)
			print("The answer(s) were : ", answers)
			print("Total time spent : ", end - start)
			print("Avg. time spent per item : ", (end - start) / y)

			continue
		
		if n == 6:
			y = int(input("Enter the number of rounds : "))
			z = int(input("Enter depth (1 or 2): "))
			start = time.time()
			score, answers = differentialEquationGame(n=y, depth=z)
			end = time.time()
			print("score : ", score, "/%d"%y)
			print("The answer(s) were : ", answers)
			print("Total time spent : ", end - start)
			print("Avg. time spent per item : ", (end - start) / y)

			continue
		
		x = input("Enter the range of numbers (e.g. 10 100): ")
		x0, x1 = int(x.split(" ")[0]), int(x.split(" ")[1])
		y = int(input("Enter the number of rounds : "))
		if n == 1:
			start = time.time()
			print("score : ", multiplicationGame(x0, x1, n=y), "/%d"%y)
			end = time.time()
			print("Total time spent : ", end - start)
			print("Avg. time spent per item : ", (end - start) / y)
		
		elif n == 2:
			z = int(input("Enter the number of dimensions : "))
			start = time.time()
			print("score : ", matrixGame(x0, x1, z, y), "/%d"%y);end = time.time()
			print("Total time spent : ", end - start)
			print("Avg. time spent per item : ", (end - start) / y)
		
		elif n == 3:
			z = int(input("Enter the number of dimensions : "))
			w = int(input("Enter the maximum degree of each entry : "))
			start = time.time()
			print("score : ", polyMatrixGame(x0, x1, w, [0, 5], z, y), "/%d"%y)
			end = time.time()
			print("Total time spent : ", end - start)
			print("Avg. time spent per item : ", (end - start) / y)
		
		

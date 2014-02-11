import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import sympy as sym 
from scipy.optimize import curve_fit  

def data_input(file_location):
	# Inputs the data from the file location into the specifiec file location
	df = pd.read_csv(file)
	return df 

def f (x, p0):
	# The equation to be fitted, however with the parameters stored in p0
	
	c, b1, m1, a, b2, m2 = p0
	return (c / (1 + np.exp((-1 * b1)) * (x - m1))) * (a + (c * np.exp(-np.exp((-1 * b2 * (x - m2))))))

def f_fit (x, c, b1, m1, a, b2, m2):
	#The equation to be fitted using the curve_fit protocol, in contrast with f, the parameters
	# are not packed, and are available in a form that curve_fit can manipulate
	return (c / (1 + np.exp((-1 * b1)) * (x - m1))) * (a + (c * np.exp(-np.exp((-1 * b2 * (x - m2))))))

def residual_calculator(tt, y, p0):
	#This function calculates the residual
	y_est = []
	res2 = []
	#For each a in thermal time list:
	for a in tt:
		temp = f(a, p0[0], p0[1], p0[2], p0[3], p0[4], p0[5])
		#Calculate the function with the assigned parameters
		y_est.append(temp)
		#Add the calculated value to the list
		temp_res = np.power((y[a] - temp), 2)
		#Calculate the residual by squaring the difference between the 
		# calculated value and the observed value
		res2.append(temp_res)
		#Add the residual to the list of residuals
	return y_est, res2

def marquardt(f, x, y, p0):
	# This modules fits the curve, giving parameter values
	try:
		p, cov = curve_fit(f, x, y, p0, maxfev = 1000)
		# Fits the curve, f is the equation specified above, x is the 
		# thermal time and y is the observed values for this plot
		out = [p[0], p[1], p[2], p[3], p[4], p[5]]
		# Adds each fitted parameter to the output list
	except RuntimeError:
		#If the attempted curve_fit throws a runtime error then this 
		# will not cause a crash, as the program includes an exception 
		# for this specific type of error
		out = ["NaN", "NaN", "NaN", "NaN", "NaN", "NaN"]
		# If the curve can't be fit then "NaN" will be used instead
	return out


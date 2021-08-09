from scipy.optimize import linprog
x = [-2,-3] # define benefit cost per unit, 2 for vanila icecream, 3 for strawberry icecream (-: means find to maximize profit)
A = [[0.5,0.2],[1,1]] # define liter of milk is required 0.5 for vanila icecream, 0.2 for strawberry icecream and 1 is required 1 doll per 1 box of icecream 
b = [10,30] #define daily order of fresh milk, 10 for vanila icecream, 30 for strawberry icecream
x0_bnds = (0, None) ## bounds is defined more than or equal to 0
x1_bnds = (0, None) ## bounds is defined more than or equal to 0
res = linprog(x,A,b, bounds=[x0_bnds, x1_bnds], method = 'revised simplex') ## solve with linear programming
print(res)

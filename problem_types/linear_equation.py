# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 18:26:15 2026

@author: Admin
"""

import random
import sympy as sp
from core.registry import register_problem
from .base_problem import BaseProblem

#-----Dạng 1: Phương trình bậc nhất cơ bản 
class LinearEquation(BaseProblem):
    
    problem_type = "Phương trình bậc nhất cơ bản"
    
    def generate(self):
        a = random.randint(1, 5)
        x = random.randint(1, 10)
        b = random.randint(1, 10)
        c = a*x + b
        
        return f"{a}*x+{b}={c}"
    
    def solve(self, problem):
        x = sp.symbols('x')
        left, right = problem.split("=")
        eq = sp.Eq(sp.sympify(left), sp.sympify(right))
        return sp.solve(eq, x)
    

    
    
# Đăng ký
register_problem("Phương trình bậc nhất cơ bản", LinearEquation())


#------Dạng 2: Phương trình bậc nhất cần rút gọn trước
class SimplifyLinearEquation(BaseProblem):
    problem_type = "Phương trình bậc nhất cần rút gọn trước"
    
    def generate(self):
        a1 = random.randint(1, 5)
        a2 = random.randint(1, 5)
        b1 = random.randint(-10, 10)
        b2 = random.randint(-10, 10)
        c = random.randint(-10, 10)
        return f"{a1}*x + {b1} + {b2} = {a2}*x + {c}"
    
    def solve(self, problem):
        x = sp.symbols('x')
        left, right = problem.split("=")
        eq = sp.Eq(sp.sympify(left), sp.sympify(right))
        return sp.solve(eq, x)

    
    
# Đăng ký
register_problem("Phương trình bậc nhất cần rút gọn trước", SimplifyLinearEquation())

#------Dạng 3: Phương trình bậc nhất chứa phân thức
class FractionLinearEquation(BaseProblem):
    problem_type = "Phương trình bậc nhất chứa phân thức"
    
    def generate(self):
        x_coeff = random.randint(1, 5)
        num1 = random.randint(-5, 5)
        num2 = random.randint(-5, 5)
        return f"({x_coeff}*x + {num1})/2 + 3 = (x + {num2})/3 + 5"
    
    def solve(self, problem):
        x = sp.symbols('x')
        left, right = problem.split("=")
        eq = sp.Eq(sp.sympify(left), sp.sympify(right))
        return sp.solve(eq, x)
    
    
# Đăng ký
register_problem("Phương trình bậc nhất chứa phân thức", FractionLinearEquation())

#------Dạng 4: Phương trình bậc nhất có nhiều ngoặc
class ParenthesesLinearEquation(BaseProblem):
    problem_type = "Phương trình bậc nhất có nhiều ngoặc"
    
    def generate(self):
        a = random.randint(1, 5)
        b = random.randint(1, 5)
        c = random.randint(1, 5)
        d = random.randint(-5, 5)
        rhs = random.randint(-5, 5)
        return f"{a}*(x+{b}) - {c}*(x+{d}) = {rhs}"
    
    def solve(self, problem):
        x = sp.symbols('x')
        left, right = problem.split("=")
        eq = sp.Eq(sp.sympify(left), sp.sympify(right))
        return sp.solve(eq, x)
    
    
# Đăng ký
register_problem("Phương trình bậc nhất có nhiều ngoặc", ParenthesesLinearEquation())
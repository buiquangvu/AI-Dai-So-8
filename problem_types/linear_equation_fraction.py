# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 19:44:13 2026

@author: Admin
"""

import random
import sympy as sp
from core.registry import register_problem
from .base_problem import BaseProblem


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
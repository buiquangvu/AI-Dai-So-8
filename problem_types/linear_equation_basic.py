# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 19:44:13 2026

@author: Admin
"""

import random
import sympy as sp
from core.registry import register_problem
from .base_problem import BaseProblem


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
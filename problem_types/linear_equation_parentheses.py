# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 19:44:13 2026

@author: Admin
"""

import random
import sympy as sp
from core.registry import register_problem
from .base_problem import BaseProblem


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
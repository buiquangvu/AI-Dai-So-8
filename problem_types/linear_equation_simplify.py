# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 19:44:13 2026

@author: Admin
"""

import random
import sympy as sp
from core.registry import register_problem
from .base_problem import BaseProblem


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
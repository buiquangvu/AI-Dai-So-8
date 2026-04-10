# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 22:47:08 2026

@author: Admin
"""

# Phân tích bằng HĐT

import random
import sympy as sp
from .base_problem import BaseProblem
from core.registry import register_problem


class IdentityRecognize(BaseProblem):

    problem_type = "Nhận dạng HĐT"


    def generate(self):
        a = random.randint(1,5)
        b = random.randint(1,5)
        pattern = random.choice(["(a+b)**2", "(a-b)**2", "a**2 - b**2"])
        if pattern == "(a+b)**2":
            return f"({a}*x+{b}*y)**2"
        elif pattern == "(a-b)**2":
            return f"({a}*x-{b}*y)**2"
        else:
            return f"{a}*x**2 - {b}*y**2"
    
    def solve(self, problem):
        x = sp.symbols('x')
        y = sp.symbols('y')
        return sp.expand(sp.sympify(problem))



# Đăng ký
register_problem("Nhận dạng HĐT", IdentityRecognize())
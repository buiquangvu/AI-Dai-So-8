# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 22:47:08 2026

@author: Admin
"""
import random
import sympy as sp
from core.registry import register_problem
from .base_problem import BaseProblem

# =====================
# Dạng 1: Nhận dạng và áp dụng trực tiếp hằng đẳng thức
# =====================
class ApplyIdentity(BaseProblem):
    problem_type = "Nhận dạng và áp dụng trực tiếp hằng đẳng thức"

    def generate(self):
        a = random.randint(1,5)
        b = random.randint(1,5)
       
        pattern = random.choice(["(a+b)**2", "(a-b)**2", "a**2 - b**2"])
        if pattern == "(a+b)**2":
            return f"({a}+{b})**2"
        elif pattern == "(a-b)**2":
            return f"({a}-{b})**2"
        else:
            return f"{a}**2 - {b}**2"
    
    def solve(self, problem):
        return sp.expand(sp.sympify(problem))

register_problem("Nhận dạng và áp dụng trực tiếp hằng đẳng thức", ApplyIdentity())

# =====================
# Dạng 2: Khai triển hằng đẳng thức
# =====================
class ExpandIdentity(BaseProblem):
    problem_type = "Khai triển hằng đẳng thức"

    def generate(self):
        a = sp.symbols('a')
        b = sp.symbols('b')
        pattern = random.choice(["(a+b)**2", "(a-b)**2", "a**2 - b**2"])
        if pattern == "(a+b)**2":
            return "(a+b)**2"
        elif pattern == "(a-b)**2":
            return "(a-b)**2"
        else:
            return "a**2 - b**2"
    
    def solve(self, problem):
        return sp.expand(sp.sympify(problem))

register_problem("Khai triển hằng đẳng thức", ExpandIdentity())

# =====================
# Dạng 3: Phân tích đa thức bằng đặt nhân tử chung
# =====================
class FactorCommon(BaseProblem):
    problem_type = "Phân tích đa thức bằng đặt nhân tử chung"

    def generate(self):
        x = sp.symbols('x')
        a = random.randint(2,5)
        b = random.randint(1,5)
        return f"{a}*x + {a}*{b}"
    
    def solve(self, problem):
        return sp.factor(sp.sympify(problem))

register_problem("Phân tích đa thức bằng đặt nhân tử chung", FactorCommon())

# =====================
# Dạng 4: Phân tích bằng hằng đẳng thức
# =====================
class FactorIdentity(BaseProblem):
    problem_type = "Phân tích bằng hằng đẳng thức"

    def generate(self):
        a = sp.symbols('a')
        b = sp.symbols('b')
        pattern = random.choice(["a**2 - b**2", "(a+b)**2 - (a-b)**2"])
        return pattern
    
    def solve(self, problem):
        return sp.factor(sp.sympify(problem))

register_problem("Phân tích bằng hằng đẳng thức", FactorIdentity())

# =====================
# Dạng 5: Phân tích bằng nhóm hạng tử
# =====================
class FactorGroup(BaseProblem):
    problem_type = "Phân tích bằng nhóm hạng tử"

    def generate(self):
        x = sp.symbols('x')
        a = random.randint(1,5)
        b = random.randint(1,5)
        c = random.randint(1,5)
        d = random.randint(1,5)
        return f"{a}*x + {b}*x + {c} + {d}"
    
    def solve(self, problem):
        return sp.factor(sp.sympify(problem))

register_problem("Phân tích bằng nhóm hạng tử", FactorGroup())
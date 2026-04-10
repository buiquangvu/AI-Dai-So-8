# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 19:38:57 2026

@author: Admin
"""

from ai.ai_explainer import explain_with_ai
from ontology.ontology_prompt_builder import fallback_from_ontology

class BaseProblem:

    problem_type = "Generic"

    def generate(self):
        raise NotImplementedError

    def solve(self, problem):
        raise NotImplementedError

    def explain(self, problem, solution, use_ai=False):

        if use_ai:
            return explain_with_ai(problem, solution, self.problem_type)

        return fallback_from_ontology(problem, solution, self.problem_type)
       

    def check(self, student, solution):
        import sympy as sp
        try:
            return sp.simplify(student - solution) == 0
        except:
            return False
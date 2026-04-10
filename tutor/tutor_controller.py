# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 20:43:11 2026

@author: Admin
"""

from utils.ai_explainer import explain_with_ai
from tutor.student_model import update_student_model
from tutor.strategy import decide_next_step

class Tutor:

    def __init__(self, problem_obj):
        self.problem_obj = problem_obj

    def start(self, problem):
        return f"Chúng ta cùng giải bài: {problem}\nEm thử bước đầu nhé?"

    def respond(self, problem, student_input, solution, student_model):
        
        # 1. Kiểm tra đúng/sai
        correct = self.problem_obj.check(student_input, solution)

        # 2. Cập nhật học sinh
        update_student_model(student_model, correct)

        # 3. Quyết định chiến lược
        action = decide_next_step(student_model, correct)

        # 4. Sinh phản hồi
        if action == "hint":
            return self.hint(problem)
        
        elif action == "explain":
            return explain_with_ai(problem, solution, "Toán lớp 8")
        
        elif action == "ask_step":
            return "Em thử làm tiếp bước tiếp theo?"
        
        elif action == "correct":
            return "Chính xác! Rất tốt 👍"

    def hint(self, problem):
        return f"Gợi ý: Hãy chuyển vế các số sang bên phải."
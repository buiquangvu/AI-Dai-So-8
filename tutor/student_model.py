# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 20:43:48 2026

@author: Admin
"""

def update_student_model(model, correct):
    
    if "attempts" not in model:
        model["attempts"] = 0
    
    model["attempts"] += 1
    
    if correct:
        model["level"] = "medium"
    else:
        model["level"] = "easy"
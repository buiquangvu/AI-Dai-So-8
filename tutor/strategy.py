# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 20:44:21 2026

@author: Admin
"""

def decide_next_step(student_model, correct):
    
    if correct:
        return "correct"
    
    if student_model["attempts"] < 2:
        return "ask_step"
    
    if student_model["attempts"] < 4:
        return "hint"
    
    return "explain"
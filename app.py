# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 10:25:46 2026

@author: Admin
"""

import streamlit as st
from core.registry import list_problems, get_problem
#from tutor.tutor_controller import Tutor

# IMPORT tất cả dạng bài (QUAN TRỌNG)
# Các bài taons liên quan đến PT bậc nhất
import problem_types.linear_equation_basic
import problem_types.linear_equation_simplify
import problem_types.linear_equation_fraction
import problem_types.linear_equation_parentheses

# Các bài toán liên quan đến Hằng đẳng thức
import problem_types.identity_recognize


#import problem_types.identity_recognize
# import problem_types.simplify_expression
# import problem_types.factor_polynomial
# import problem_types.inequality
# import problem_types.expand_identity
# import problem_types.compare_function

st.title("🤖 Hệ thống AI học Toán")

# Chọn dạng bài
problem_type = st.selectbox("Chọn dạng bài:", list_problems())

problem_obj = get_problem(problem_type)

use_ai = st.checkbox("🤖 Dùng AI để giải thích", value=True)

# Sinh bài
if st.button("Sinh bài"):
    st.session_state.problem = problem_obj.generate()

if "problem" in st.session_state:
    st.write("### 📝 Bài toán:")
    st.code(st.session_state.problem)

    # Giải
    if st.button("Giải"):
        sol = problem_obj.solve(st.session_state.problem)
        st.write("Đáp án:", sol)

        if isinstance(sol, list):
            #solution = ", ".join(map(str, sol))
            sol = ", ".join(map(str, sol))

        #st.markdown(f"### ✅ Đáp án: **{solution}**")
        st.markdown(f"### ✅ Đáp án: **{sol}**")
       
        explanation = problem_obj.explain(
        st.session_state.problem,
        sol,
        use_ai=use_ai
    )
        st.write("Giải thích:", explanation)



# # Kiểm tra
#     student = st.text_input("Nhập đáp án của bạn:")
    
#     if st.button("Chấm bài"):
#         sol = problem_obj.solve(st.session_state.problem)
#         result = problem_obj.check(student, sol)
#         st.write("Kết quả:", "✅ Đúng" if result else "❌ Sai")
        
        
        


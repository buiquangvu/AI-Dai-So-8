# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 21:18:36 2026

@author: Admin
"""

from ontology.math_ontology import ONTOLOGY

def fallback_from_ontology(problem, solution, problem_type):

    data = ONTOLOGY.get(problem_type, {})
    steps = data.get("steps", [])
    rules = data.get("rules", [])
    
    print("steps", steps )
    print("problem_type:", problem_type)
    text = "Giải theo các bước:\n"

    for i, step in enumerate(steps, 1):
        text += f"B{i}: {step}\n"

    if rules:
        text += "\nCông thức áp dụng:\n"
        for r in rules:
            text += f"- {r}\n"

    text += f"\n→ Đáp án: {solution}"

    return text

def build_prompt_from_ontology(problem, solution, problem_type, mode="full"):
    
    data = ONTOLOGY.get(problem_type, {})
    
    steps = data.get("steps", [])
    mistakes = data.get("common_mistakes", [])
    pedagogy = data.get("pedagogy", {})

    print("steps", steps )
    print("problem_type:", problem_type)
    # =========================
    # XÂY PROMPT
    # =========================
    prompt = f"""
    Bạn là giáo viên Toán lớp 8.

    Dạng toán: {problem_type}
    Khái niệm: {data.get("concepts")}
    Kỹ năng: {data.get("skills")}

    Các bước chuẩn:
    {data.get("steps")}

    Các lỗi học sinh hay mắc:
    {data.get("common_mistakes")}

    Bài toán: {problem}
    Đáp án: {solution}

    Yêu cầu:
    - Giải từng bước rõ ràng
    - Giải thích vì sao làm như vậy
    - Ngôn ngữ đơn giản, dễ hiểu
    - Trình bày bằng LaTeX (dùng $$...$$ cho mỗi bước)

    Hãy giải chi tiết, dễ hiểu, có giải thích.
    """

    # =========================
    # CHÈN CÁC BƯỚC TỪ ONTOLOGY
    # =========================
    if steps:
        prompt += "\nHướng dẫn theo các bước:\n"
        for i, step in enumerate(steps, 1):
            prompt += f"Bước {i}: {step}\n"

    # =========================
    # THÊM LỖI THƯỜNG GẶP
    # =========================
    if mistakes:
        prompt += "\nLưu ý lỗi thường gặp:\n"
        for m in mistakes:
            prompt += f"- {m}\n"

    # =========================
    # STYLE SƯ PHẠM
    # =========================
    if pedagogy.get("ask_questions"):
        prompt += "\nHãy đặt câu hỏi gợi mở cho học sinh."

    if pedagogy.get("use_simple_language"):
        prompt += "\nSử dụng ngôn ngữ đơn giản."

    # =========================
    # MODE
    # =========================
    if mode == "hint":
        prompt += "\nChỉ đưa gợi ý, không giải hoàn chỉnh."

    elif mode == "step":
        prompt += "\nChỉ giải bước đầu tiên."

    return prompt





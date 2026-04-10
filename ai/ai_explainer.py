# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 16:40:43 2026

@author: Admin
"""

from openai import OpenAI
import os
import streamlit as st
from dotenv import load_dotenv
from ontology.ontology_prompt_builder import build_prompt_from_ontology

#load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) or st.secrets.get("OPENAI_API_KEY")


def explain_with_ai(problem, solution, problem_type,mode="full"):
    try:
        prompt = build_prompt_from_ontology(
            problem,
            solution,
            problem_type,
            mode
        )

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"(Lỗi AI) → {e}"




# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 19:38:17 2026

@author: Admin
"""

# from problem_types.identity_recognize import IdentityRecognize
# from problem_types.identity_expand import IdentityExpand
# from problem_types.factor_common import FactorCommon
# from problem_types.factor_identity import FactorIdentity
# from problem_types.factor_grouping import FactorGrouping


# PROBLEM_REGISTRY = {
#     "Nhận dạng HĐT": IdentityRecognize(),
#     "Khai triển HĐT": IdentityExpand(),
#     "Đặt nhân tử chung": FactorCommon(),
#     "Phân tích bằng HĐT": FactorIdentity(),
#     "Nhóm hạng tử": FactorGrouping(),
# }

PROBLEM_REGISTRY = {}

def register_problem(name, problem_obj):
    PROBLEM_REGISTRY[name] = problem_obj

def get_problem(name):
    return PROBLEM_REGISTRY.get(name)

def list_problems():
    return list(PROBLEM_REGISTRY.keys())
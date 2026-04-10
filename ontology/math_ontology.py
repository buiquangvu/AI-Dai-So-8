# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 21:17:58 2026

@author: Admin
"""

ONTOLOGY = {

    # =========================================
    # DẠNG 1: NHẬN DẠNG & ÁP DỤNG HẰNG ĐẲNG THỨC
    # =========================================
    "Nhận dạng HĐT": {
        "domain": "Algebra",
        "subdomain": "identity_application",

        "concepts": ["hằng đẳng thức", "biểu thức", "nhận dạng"],

        "steps": [
            "Nhận dạng dạng hằng đẳng thức (ví dụ: (a+b)^2, a^2-b^2, (a-b)^2)",
       "Áp dụng công thức hằng đẳng thức để rút gọn biểu thức",
       "Thực hiện phép tính để đưa về dạng đơn giản hoặc nghiệm"
        ],

        "rules": [
            "(a + b)^2 = a^2 + 2ab + b^2",
            "(a - b)^2 = a^2 - 2ab + b^2",
            "a^2 - b^2 = (a - b)(a + b)"
        ],

        "skills": ["nhận dạng", "so sánh", "áp dụng công thức"],

        "common_mistakes": [
            "Nhận dạng sai dạng hằng đẳng thức",
            "Xác định sai a, b",
            "Nhầm dấu trong công thức"
        ],

        "pedagogy": {
            "style": "từng bước",
            "ask_questions": True,
            "hint_first": True
        }
    },

    # =========================================
    # DẠNG 2: KHAI TRIỂN HẰNG ĐẲNG THỨC
    # =========================================
    "Khai triển HĐT": {
        "domain": "Algebra",

        "concepts": ["khai triển", "hằng đẳng thức", "đa thức"],

        "steps": [
            "Xác định dạng hằng đẳng thức",
            "Áp dụng công thức khai triển",
            "Nhân các hạng tử",
            "Thu gọn biểu thức"
        ],

        "rules": [
            "(a + b)^2 → a^2 + 2ab + b^2",
            "(a - b)^2 → a^2 - 2ab + b^2",
            "(a + b)(a - b) → a^2 - b^2"
        ],

        "skills": ["khai triển", "nhân đa thức", "thu gọn"],

        "common_mistakes": [
            "Quên nhân 2ab",
            "Sai dấu khi khai triển",
            "Không thu gọn biểu thức"
        ],

        "pedagogy": {
            "style": "từng bước",
            "ask_questions": True,
            "hint_first": True
        }
    },

    # =========================================
    # DẠNG 3: ĐẶT NHÂN TỬ CHUNG
    # =========================================
    "Đặt nhân tử chung": {
        "domain": "Algebra",

        "concepts": ["nhân tử chung", "đa thức", "phân tích"],

        "steps": [
            "Tìm nhân tử chung của các hạng tử",
            "Đặt nhân tử chung ra ngoài",
            "Viết phần còn lại trong ngoặc",
            "Kiểm tra lại bằng phép nhân"
        ],

        "rules": [
            "ax + ay = a(x + y)",
            "2x^2 + 4x = 2x(x + 2)"
        ],

        "skills": ["tìm nhân tử", "phân tích", "biến đổi"],

        "common_mistakes": [
            "Không tìm hết nhân tử chung",
            "Đặt sai nhân tử",
            "Sai dấu trong ngoặc"
        ],

        "pedagogy": {
            "style": "từng bước",
            "ask_questions": True,
            "hint_first": True
        }
    },

    # =========================================
    # DẠNG 4: PHÂN TÍCH BẰNG HẰNG ĐẲNG THỨC
    # =========================================
    "Phân tích HĐT": {
        "domain": "Algebra",

        "concepts": ["phân tích", "hằng đẳng thức", "đa thức"],

        "steps": [
            "Quan sát biểu thức",
            "Nhận dạng dạng hằng đẳng thức",
            "Xác định a, b",
            "Viết lại dưới dạng tích"
        ],

        "rules": [
            "a^2 + 2ab + b^2 = (a + b)^2",
            "a^2 - 2ab + b^2 = (a - b)^2",
            "a^2 - b^2 = (a - b)(a + b)"
        ],

        "skills": ["nhận dạng", "phân tích", "áp dụng công thức"],

        "common_mistakes": [
            "Không nhận ra dạng hằng đẳng thức",
            "Nhầm dấu",
            "Viết sai dạng tích"
        ],

        "pedagogy": {
            "style": "từng bước",
            "ask_questions": True,
            "hint_first": True
        }
    },

    # =========================================
    # DẠNG 5: NHÓM HẠNG TỬ
    # =========================================
    "Nhóm hạng tử": {
        "domain": "Algebra",

        "concepts": ["nhóm hạng tử", "đa thức", "phân tích"],

        "steps": [
            "Nhóm các hạng tử hợp lý",
            "Đặt nhân tử chung trong từng nhóm",
            "Xuất hiện nhân tử chung mới",
            "Tiếp tục phân tích nếu có thể"
        ],

        "rules": [
            "ax + ay + bx + by = (a + b)(x + y)"
        ],

        "skills": ["nhóm", "phân tích", "tư duy biến đổi"],

        "common_mistakes": [
            "Nhóm sai hạng tử",
            "Không tạo được nhân tử chung",
            "Dừng quá sớm"
        ],

        "pedagogy": {
            "style": "từng bước",
            "ask_questions": True,
            "hint_first": True
        }
    }, 
    
    # DẠNG II.1: Phương trình bậc nhất cơ bản (basic_equation)
    # =====================================
    "Phương trình bậc nhất cơ bản": {
        "domain": "Equations",
        "subdomain": "basic_equation",
        
        "concepts": ["ẩn", "phương trình"],
        
        "steps": [
            "Chuyển vế",
            "Thu gọn",
            "Chia hệ số"
        ],
        
        "rules": [
            "a + b = c → a = c - b",
            "ax = b → x = b/a"
        ],
        
        "skills": ["chuyển vế", "thu gọn", "chia"],
        
        "common_mistakes": [
            "Không đổi dấu khi chuyển vế",
            "Chia sai"
        ],
        
        "pedagogy": {
            "style": "từng bước",
            "ask_questions": True,
            "hint_first": True
        }
    },
    # DẠNG II.2: Phương trình bậc nhất cần rút gọn trước
    "Phương trình bậc nhất cần rút gọn trước": {
    "domain": "Equations",
    "subdomain": "simplify_equation",
    
    "concepts": ["ẩn", "phương trình", "rút gọn"],
    
    "steps": [
        "Rút gọn các hằng số giống nhau",
        "Chuyển vế các biến và hằng số",
        "Thu gọn biểu thức",
        "Chia hệ số biến để tìm nghiệm"
    ],
    
    "rules": [
        "a + b + c = d → a + (b + c) = d → a = d - (b + c)",
        "ax + b = cx + d → (a - c)x = d - b → x = (d - b)/(a - c)"
    ],
    
    "skills": ["rút gọn", "chuyển vế", "thu gọn", "chia"],
    
    "common_mistakes": [
        "Không rút gọn đúng các hằng số",
        "Quên đổi dấu khi chuyển vế",
        "Chia sai hệ số biến"
    ],
    
    "pedagogy": {
        "style": "từng bước",
        "ask_questions": True,
        "hint_first": True
    }
    },
    
    # DẠNG II.3: Phương trình bậc nhất chứa phân thức
    
    "Phương trình bậc nhất chứa phân thức": {
    "domain": "Equations",
    "subdomain": "fraction_equation",
    
    "concepts": ["ẩn", "phương trình", "phân thức"],
    
    "steps": [
        "Quy đồng mẫu số nếu cần",
        "Nhân cả hai vế với mẫu chung để loại bỏ phân thức",
        "Thu gọn các hằng số và biến",
        "Chuyển vế các biến và hằng số",
        "Chia hệ số biến để tìm nghiệm"
    ],
    
    "rules": [
        "(a*x + b)/m + c = (d*x + e)/n + f → Nhân cả hai vế với mẫu chung (m*n)",
        "ax + b = c → x = (c - b)/a"
    ],
    
    "skills": ["quy đồng mẫu", "loại bỏ phân thức", "thu gọn", "chuyển vế", "chia"],
    
    "common_mistakes": [
        "Quên nhân cả hai vế với mẫu chung",
        "Nhầm tử số và mẫu số",
        "Không rút gọn đúng các hằng số sau khi loại bỏ phân thức",
        "Chia sai hệ số biến"
    ],
    
    "pedagogy": {
        "style": "từng bước",
        "ask_questions": True,
        "hint_first": True
    } 
    },
    
    # DẠNG II.4: Phương trình bậc nhất có nhiều ngoặc
    "Phương trình bậc nhất có nhiều ngoặc": {
    "domain": "Equations",
    "subdomain": "parentheses_equation",
    
    "concepts": ["ẩn", "phương trình", "ngoặc"],
    
    "steps": [
        "Mở ngoặc bằng cách nhân phân phối",
        "Thu gọn các hằng số và hệ số biến",
        "Chuyển vế các biến và hằng số",
        "Chia hệ số biến để tìm nghiệm"
    ],
    
    "rules": [
        "a*(x + b) - c*(x + d) = e → a*x + a*b - c*x - c*d = e",
        "ax + b = c → x = (c - b)/a"
    ],
    
    "skills": ["mở ngoặc", "thu gọn", "chuyển vế", "chia"],
    
    "common_mistakes": [
        "Nhầm dấu khi mở ngoặc",
        "Không rút gọn đủ các hạng tử",
        "Quên đổi dấu khi chuyển vế",
        "Chia sai hệ số biến"
    ],
    
    "pedagogy": {
        "style": "từng bước",
        "ask_questions": True,
        "hint_first": True
    }
    }
}


    





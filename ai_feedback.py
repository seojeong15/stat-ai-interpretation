# -*- coding: utf-8 -*-
"""
Created on Wed Dec 31 23:53:09 2025

@author: tjdwn
"""

def analyze_answer(user_answer: str, correct_answer: str):
    """
    통계 해석 답변을 분석하여
    (1) 오류 유형
    (2) 생성형 AI 스타일 피드백
    을 반환
    """

    user = user_answer.lower()
    correct = correct_answer.lower()

    error_types = []

    # 1. 상관관계 vs 인과관계
    if "인과" in user and "인과" not in correct:
        error_types.append("상관관계와 인과관계 혼동")

    # 2. p-value 해석 오류
    if "유의" in user and "유의하지" in correct:
        error_types.append("p-value 해석 오류")

    # 3. 설명력 과대 해석
    if "설명" in user or "r²" in user:
        error_types.append("설명력(R²) 과대 해석")

    # 오류 없음 → 긍정 피드백
    if not error_types:
        feedback = (
            "✅ AI 판단 결과, 통계적으로 타당한 해석입니다.\n\n"
            "분석 결과의 한계와 통계적 유의성을 적절히 고려하였으며, "
            "통계적 사실을 과도하게 일반화하지 않았습니다."
        )
        return error_types, feedback

    # 오류 있음 → 생성형 AI 피드백
    feedback = "❌ AI가 다음과 같은 통계 해석 오류를 감지했습니다:\n\n"

    explanations = {
        "상관관계와 인과관계 혼동":
            "상관관계가 높더라도 한 변수가 다른 변수를 직접적으로 "
            "원인이라고 단정할 수는 없습니다.",

        "p-value 해석 오류":
            "p-value는 귀무가설 하에서 관측 결과가 나올 확률을 의미하며, "
            "효과의 크기나 중요도를 직접적으로 나타내지는 않습니다.",

        "설명력(R²) 과대 해석":
            "R² 값은 모델의 설명력을 나타내지만, "
            "모델의 인과적 타당성을 보장하지는 않습니다."
    }

    for e in error_types:
        feedback += f"- {e}: {explanations[e]}\n"

    feedback += (
        "\n🤖 AI 개선 제안:\n"
        "통계 결과를 해석할 때는 (1) 통계적 유의성, "
        "(2) 인과관계 여부, (3) 분석의 한계를 함께 고려하여 "
        "보다 신중하게 결론을 도출하는 것이 바람직합니다."
    )

    return error_types, feedback

# -*- coding: utf-8 -*-
"""
Created on Wed Dec 31 23:44:34 2025

@author: tjdwn
"""

import streamlit as st
from stats_questions import QUESTIONS
from ai_feedback import analyze_answer

st.set_page_config(page_title="통계 해석 오류 감소 시스템", layout="centered")

st.title("📊 생성형 AI 기반 통계 해석 오류 감소 시스템")
st.write("통계 결과를 보고 올바른 해석을 선택해보세요.")

# 문제 선택
question_ids = [q["id"] for q in QUESTIONS]
selected_id = st.selectbox("문제 선택", question_ids)

question = next(q for q in QUESTIONS if q["id"] == selected_id)

st.subheader("📄 통계 분석 결과")
st.code(question["result"])

user_answer = st.text_area("✍️ 당신의 해석을 입력하세요")

if st.button("정답 확인"):
    st.subheader("✅ 모범 해석")
    st.success(question["correct"])

    if user_answer.strip() == "":
        st.warning("해석을 입력하지 않았습니다.")
    else:
        errors, feedback = analyze_answer(user_answer, question["correct"])

        if not errors:
            st.info("🎉 AI 판단: 올바른 통계 해석입니다.")
        else:
            st.error("⚠️ AI 판단: 통계 해석 오류 가능성")

        st.subheader("🤖 AI 피드백")
        st.write(feedback)


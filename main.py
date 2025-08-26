# from dotenv import load_dotenv
from langchain_openai import OpenAI, ChatOpenAI
import sys
import io
import streamlit as st


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")

# .env 파일에서 OPENAI_API_KEY 불러오기
# load_dotenv()


# 챗 모델
chat_model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

st.title("인공지능 시인")
content = st.text_input("시제를 제시해 주세요.")

if st.button("시 생성하기"):
    with st.spinner("시 생성 중...", show_time=True):
        result = chat_model.invoke(content + "에 대한 시를 써줘") 
        st.write(result.content)

# # 실행 예시
# print("ChatModel 응답:", chat_model.invoke("안녕"))

# # 단일 텍스트 기반 모델
# llm = OpenAI(model="gpt-3.5-turbo-instruct")

# # 실행 예시
# print("LLM 응답:", llm.invoke("안녕"))
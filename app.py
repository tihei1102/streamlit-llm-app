import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = st.secrets['app.py']['app_APIKey']

import streamlit as st

st.title("課題アプリ: 専門家チャットボット")

st.write("##### 動作モード1: リサーチ手法専門家")
st.write("リサーチ手法関連を聞くことで、専門家としてアドバイスしてくれます")
st.write("##### 動作モード2: 分析手法専門家")
st.write("分析手法関連を聞くことで、専門家としてアドバイスしてくれます")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["リサーチ手法専門家", "分析手法専門家"]
)

st.divider()

if selected_item == "リサーチ手法専門家":
    input_message = st.text_input(label="リサーチの専門家に聞きたいことを入力してください。")

else:
    input_message = st.text_input(label="分析手法の専門家に聞きたいことを入力してください。")

if st.button("実行"):
    st.divider()
    import os

    if selected_item == "リサーチ手法専門家":
        if input_message:
            from langchain_openai import ChatOpenAI
            from langchain.schema import SystemMessage, HumanMessage
            llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0, api_key=open_ai_api_key)

            messages = [
            SystemMessage(content="あなたはリサーチ手法の専門家です"),
            HumanMessage(content=input_message),
            ]
            result = llm(messages)
            st.write(result)

        else:
            st.error("対象となるテキストを入力してから「実行」ボタンを押してください。")

    else:
        if input_message:
            from langchain_openai import ChatOpenAI
            from langchain.schema import SystemMessage, HumanMessage
            llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0, api_key=open_ai_api_key)

            messages = [
            SystemMessage(content="あなたは分析手法の専門家です"),
            HumanMessage(content=input_message),
            ]
            result = llm(messages)
            st.write(result)

        else:
            st.error("対象となるテキストを入力してから「実行」ボタンを押してください。")
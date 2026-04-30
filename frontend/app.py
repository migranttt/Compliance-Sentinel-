
import streamlit as st
import requests

st.set_page_config(
    page_title="Compliance Sentinel",
    layout="wide"
)

st.title("🛡️ 合规哨兵")

uploaded = st.file_uploader(
    "上传合同或宣传文档",
    type=["pdf", "docx", "txt"]
)

if uploaded:

    if st.button("开始审查"):

        with st.spinner("AI 正在进行多Agent推理..."):

            files = {
                "file": (
                    uploaded.name,
                    uploaded.getvalue()
                )
            }

            response = requests.post(
                "http://127.0.0.1:8000/audit",
                files=files
            )

            result = response.json()

            st.success("审查完成")

            st.subheader("审查结果")

            st.json(result)

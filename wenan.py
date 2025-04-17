import streamlit as st
from a import ok
with st.sidebar:
    password = st.text_input("输入你的API", type="password")

st.header("小红书文案生成")
subject = st.text_input("请输入主题：")
submit = st.button("提交")
if submit:
    if not password:
        st.info("请输入API")
        st.stop()
    if not subject:
        st.info("请输入主题")
        st.stop()
    with st.spinner("文本正在生成中"):
        result=ok(subject,password)
    column1, column2 = st.columns([1, 2])
    with column1:
        st.write("## 标题")
        st.write(result.titles[0])
        st.write(result.titles[1])
        st.write(result.titles[2])
        st.write(result.titles[3])
        st.write(result.titles[4])
    with column2:
        st.write("## 正文")
        st.write(result.content)

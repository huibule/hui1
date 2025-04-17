import streamlit as st
import pandas as pd

#字符串显示
st.write("早上好")
st.write("# 早上好")
"中午好"

#图片显示
st.image("./桌面.jpg",width=300)

#表格显示
df = pd.DataFrame({"学号":["01","02"],
                   "分数":[92,93]})
st.dataframe(df)

#输入组件
name = st.text_input("请输入你的名字：")
if name:
    st.write(f"{name}，你好")

#分隔线
st.divider()
#输入密码
password = st.text_input("请输入你的密码：",type="password")

#输入长句
st.divider()
paragraph = st.text_area("请输入一段文字：")

#输入数字
st.divider()
age = st.number_input("请输入你的年龄：")

#勾选框
st.divider()
check = st.checkbox("同意以上条款")
if check:
    st.write("展示信息")

#按钮
st.divider()
submit = st.button("提交")
if submit:
    st.write("提交成功")

#单选按钮
gender1 = st.radio("请选择你的性别：",
                ["男性","女性","跨性别"],
                index=None)
if gender1:
    st.write(f"你选择的性别是{gender1}")

#单选下拉框
gender2 = st.selectbox("请选择你的性别：",
                   ["男性","女性","跨性别"])

#多选下拉框
contacts = st.multiselect("你希望通过什么方式联系",
                     ["电话","邮箱","微信","其他"])
for contact in contacts:
    st.write(f"你选择的联系方式是{contact}")

#滑块
height = st.slider("你的身高是多少？", value=170,
               min_value=140, max_value=200, step=1)

#文件上传器
uploaded_file = st.file_uploader("上传文件", type=[".py"])
if uploaded_file:
    st.write(f"你上传的文件名是{uploaded_file.name}")
    st.write(f"文件内容如下{uploaded_file.read()}")

#侧边栏
with st.sidebar:
    school = st.text_input("请输入你的学校：")
    if school:
        st.write(f"你在{school}就读")

#多列布局
column1, column2 = st.columns([1,2])
with column1:
    st.button("优秀")
with column2:
    st.button("及格")

#选项卡
tab1, tab2 = st.tabs(["年龄","性别"])
with tab1:
    st.write(age)
with tab2:
    st.write(gender1)

#折叠展开组件
with st.expander("信息"):
    st.write("个人信息")

#会话状态帮助保留变量的值
if "a" not in st.session_state:
    st.session_state.a = 0

clicked = st.button("加1")
if clicked:
    st.session_state.a += 1
st.write(st.session_state.a)
print(st.session_state)


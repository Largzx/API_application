import streamlit as st
from utils import generate_script

st.title("🎤脱口秀文本生成器")

with st.sidebar:
    deep_seek_key = st.text_input("请输入Deepseek密钥", type="password")
    model_kind = st.selectbox("选择模型, 默认为V3（Chat为V3模型 | reasoner为R1模型)",
                              ["deepseek-chat", "deepseek-reasoner"],
                              index=0)

    st.markdown("[获取Deepseek API密钥](https://platform.deepseek.com/)")

subject = st.text_input("请输入脱口秀的主题")
talk_length = st.number_input("请输入脱口秀演讲的大致时长（单位：分钟）", min_value=1.0, step=1.0)
creativity = st.slider("输入脱口秀文本的创造力（数字小更严谨，数字大更加具有多样性）", min_value=0.0,
                       max_value=1.5, value=0.2, step=0.1)

submit = st.button("生成脚本")

if submit and not deep_seek_key:
    st.info("请输入你的deepseek API密钥")
    st.stop()
if submit and not subject:
    st.info("请输入脱口秀主题")
    st.stop()
if submit:
    with st.spinner("🙍‍♂️AI正在思考中，请稍后..."):
        script = generate_script(subject, talk_length, creativity, model_kind, deep_seek_key)
    st.success("🎉文本已生成！")
    st.subheader("📄脱口秀文本")
    st.write(script)

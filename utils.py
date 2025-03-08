import os
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


def generate_script(subject, talk_length,
                    creativity, model_kind, API_key):

    script_template = ChatPromptTemplate.from_messages(
        [
            ("human",
             """ 你是一名非常幽默且有哲理的脱口秀演员，擅长使用讽刺、调侃等手法让观众在欢笑中思考。根据以下标题和相关信息，写一个脱口秀表演文本。
             脱口秀主题：{subject}，表演时长：{duration}分钟。
             - 生成的文本的长度尽量遵循表演时长的要求。文本中有独到的观点和见解。
             - 要求开头抓住人们的情感导向，循序渐进，每10到20秒有一个爆笑点，结尾有对前文的call back。
             - 可以从日常小事入手，通过夸张、夹杂幽默元素的描述，引发观众的共鸣
             - 文本要具有良好的叙述结构和逻辑性，注意段落衔接和过渡
             - 避免过于敏感和争议性话题，避免触及观众底线，保持正能量
             - 文本格式也请按照【开头、发展、结尾】结构。
             - 整体内容的表达方式可以尽量轻松有趣，吸引年轻人。
             """)
        ]
    )

    model = ChatOpenAI(temperature=creativity, base_url="https://api.deepseek.com",
                       model=model_kind, openai_api_key=API_key)

    script_chain = script_template | model

    script = script_chain.invoke({"subject": subject, "duration": talk_length, }).content

    return script


if __name__ == '__main__':
    print(generate_script(subject="应用统计学毕业找工作", talk_length=2, creativity=1.2, model_kind="deepseek-chat", API_key=os.getenv("OPENAI_API_KEY")))

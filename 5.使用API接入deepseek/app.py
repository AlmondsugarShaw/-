# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI

client = OpenAI(api_key="sk-99602c9f1d2d4374a9fdde59d5ca5278", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一名程序员"},
        {"role": "user", "content": "如何将deepseek使用API接入QQ聊天？请给我一个完整的解决方案"},
    ],
    stream=False
)

print(response.choices[0].message.content)
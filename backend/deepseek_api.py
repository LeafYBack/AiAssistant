# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI

client = OpenAI(api_key="sk-b0086759de82476c82563da40c1354db", base_url="https://api.deepseek.com")

#提问的问题
text="你的数据库截止于何时"

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": text},
    ],
    #stream=False
)

print(response.choices[0].message.content)
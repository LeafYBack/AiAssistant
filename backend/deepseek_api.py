import requests

DEEPSEEK_API_URL = "https://api.deepseek.ai/v1/analyze"  # 替换为实际 DeepSeek API URL
DEEPSEEK_API_KEY = "YOUR_DEEPSEEK_API_KEY"  # 替换为实际 API 密钥

def analyze_text(text):
    # 调用 DeepSeek API 进行文本分析
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "text": text
    }

    response = requests.post(DEEPSEEK_API_URL, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()  # 返回分析结果
    else:
        print(f"Error: {response.status_code}")
        return None

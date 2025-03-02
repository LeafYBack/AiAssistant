import requests

ONENOTE_API_URL = "https://graph.microsoft.com/v1.0/me/onenote/pages"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"  # 替换为实际的 access_token

def get_onenote_pages():
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    response = requests.get(ONENOTE_API_URL, headers=headers)

    if response.status_code == 200:
        return response.json()  # 返回页面列表
    else:
        print(f"Error: {response.status_code}")
        return None

def update_onenote_page(page_id, content):
    update_url = f"{ONENOTE_API_URL}/{page_id}/content"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "content": content  # 需要插入的新的 HTML 内容
    }
    response = requests.patch(update_url, headers=headers, json=data)

    if response.status_code == 200:
        print("Page updated successfully.")
    else:
        print(f"Error: {response.status_code}")

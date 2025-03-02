from flask import Flask, request, jsonify
from deepseek_api import analyze_text
from onenote_api import update_onenote_page

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text')

    if not text:
        return jsonify({"error": "No text provided"}), 400

    # 调用 DeepSeek API 分析文本
    analysis_result = analyze_text(text)

    if analysis_result:
        return jsonify(analysis_result)
    else:
        return jsonify({"error": "DeepSeek analysis failed"}), 500

@app.route('/update_onenote', methods=['POST'])
def update_onenote():
    data = request.get_json()
    page_id = data.get('page_id')
    content = data.get('content')

    if not page_id or not content:
        return jsonify({"error": "Missing page_id or content"}), 400

    # 更新 OneNote 页面
    update_onenote_page(page_id, content)
    return jsonify({"message": "Page updated successfully"})

if __name__ == '__main__':
    app.run(debug=True)

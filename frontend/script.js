function triggerAnalysis() {
    const pageContent = "这是一个模拟的笔记内容"; // 实际情况需要从 OneNote 获取页面内容

    // 调用后端的分析接口
    fetch('http://127.0.0.1:5000/analyze', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: pageContent })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Analysis result:', data);
        // 假设分析结果中返回的就是更新内容
        const updatedContent = "分析后生成的学习计划：\n" + data.summary;

        // 调用更新 OneNote 页面接口
        updateOneNotePage('samplePageId', updatedContent);
    })
    .catch(error => console.error('Error:', error));
}

function updateOneNotePage(pageId, content) {
    fetch('http://127.0.0.1:5000/update_onenote', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ page_id: pageId, content: content })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message);
    })
    .catch(error => console.error('Error:', error));
}


# Compliance Sentinel（合规哨兵）

基于 Multi-Agent + 长链推理 的企业合同/宣传物料合规审查系统。

## 功能特性
- PDF / DOCX 文档上传
- 多 Agent 协同分析
- 法规规则检索
- 企业内控规则检查
- 跨文档冲突检测
- 长链推理解释
- 风险报告生成

## 技术栈
- FastAPI
- LangGraph
- Qdrant（可替换）
- OpenAI / Qwen
- Streamlit

## 项目结构
```
compliance_sentinel/
├── backend/
├── frontend/
├── data/
├── prompts/
└── requirements.txt
```

## 启动方式

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 启动后端
```bash
cd backend
uvicorn main:app --reload
```

### 3. 启动前端
```bash
cd frontend
streamlit run app.py
```

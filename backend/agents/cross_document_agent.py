
def cross_document_agent(text: str):

    conflicts = []

    if "一次性交货" in text:
        conflicts.append({
            "history_doc": "供应商框架协议V3",
            "conflict": "历史协议允许分批交货"
        })

    return conflicts

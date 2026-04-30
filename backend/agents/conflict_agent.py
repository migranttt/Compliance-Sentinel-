
def conflict_agent(regulations, internal_rules, cross_conflicts):

    results = []

    for item in regulations:
        results.append({
            "type": "法规风险",
            "detail": item
        })

    for item in internal_rules:
        results.append({
            "type": "内控风险",
            "detail": item
        })

    for item in cross_conflicts:
        results.append({
            "type": "跨文档冲突",
            "detail": item
        })

    return results


def internal_rule_agent(text: str):

    rules = []

    if "加州法律" in text:
        rules.append({
            "policy": "境外合同必须指定中国争议解决地",
            "level": "中风险"
        })

    return rules

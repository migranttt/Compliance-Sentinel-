
def reasoning_agent(conflicts, original_text):

    reasoning_steps = []

    for c in conflicts:

        if c["type"] == "法规风险":
            reasoning_steps.append({
                "step": (
                    "检测到账期超过30天，"
                    "依据加州统一商法典，"
                    "需要明确逾期利率条款，"
                    "否则可能导致履约争议。"
                ),
                "risk": "高风险"
            })

        elif c["type"] == "内控风险":
            reasoning_steps.append({
                "step": (
                    "检测到适用加州法律，"
                    "但未指定中国争议解决地，"
                    "违反企业内控规则。"
                ),
                "risk": "中风险"
            })

    return reasoning_steps


def regulation_agent(text: str):

    findings = []

    if "60日内付款" in text:
        findings.append({
            "risk": "高风险",
            "law": "加州统一商法典",
            "issue": "超30天账期未明确逾期利率"
        })

    return findings

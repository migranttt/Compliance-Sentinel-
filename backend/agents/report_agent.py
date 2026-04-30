
def report_agent(reasoning):

    report = {
        "summary": [],
        "suggestions": []
    }

    for r in reasoning:

        report["summary"].append({
            "risk": r["risk"],
            "analysis": r["step"]
        })

    report["suggestions"].append(
        "补充逾期利率条款"
    )

    report["suggestions"].append(
        "统一使用企业标准争议解决模板"
    )

    return report

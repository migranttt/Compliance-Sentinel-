
from agents.regulation_agent import regulation_agent
from agents.internal_rule_agent import internal_rule_agent
from agents.cross_document_agent import cross_document_agent
from agents.conflict_agent import conflict_agent
from agents.reasoning_agent import reasoning_agent
from agents.report_agent import report_agent

def run_pipeline(document_text: str):

    regulations = regulation_agent(document_text)

    internal_rules = internal_rule_agent(document_text)

    cross_conflicts = cross_document_agent(document_text)

    conflicts = conflict_agent(
        regulations,
        internal_rules,
        cross_conflicts
    )

    reasoning = reasoning_agent(conflicts, document_text)

    report = report_agent(reasoning)

    return report

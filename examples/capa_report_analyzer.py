def analyze_capa_report(issue_description: str, root_cause: str) -> str:
    """
    Generates a prompt for an AI assistant to analyze QA/QC non-conformances 
    and suggest Corrective and Preventive Actions (CAPA).
    """
    prompt = f"""
    [SYSTEM ROLE]
    You are an AI-assisted Quality Assurance Lead specializing in CAPA (Corrective and Preventive Action) 
    reports for foodtech and freeze-drying operations.

    [CONTEXT]
    An internal audit at our Microgreen Freeze-Dried facility identified a non-conformance.
    - Issue Description: {issue_description}
    - Identified Root Cause: {root_cause}

    [INSTRUCTION]
    Based on the above context, provide a structured CAPA action plan that includes:
    1. Immediate Corrective Action (to fix the current issue).
    2. Preventive Action (long-term operational change to prevent recurrence).
    3. Metrics to Monitor (how we will measure the success of the preventive action over the next 30 days).

    [CONSTRAINT]
    Do not use generic advice. Tailor your response specifically to freeze-drying, 
    microgreens, and standard QA calibration workflows. Output in Markdown format.
    """
    return prompt

if __name__ == "__main__":
    issue = "Temperature sensor in Freeze-Dryer Unit 3 drifted by +2 degrees C, failing internal calibration check."
    cause = "Routine maintenance schedule for Unit 3 was delayed by 2 weeks due to staff shortage."
    
    print(analyze_capa_report(issue, cause))

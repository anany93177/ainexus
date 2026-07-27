import json

def generate_haccp_validation_prompt(ccp_data: dict) -> str:
    """
    Generates a prompt to validate Hazard Analysis and Critical Control Points (HACCP) 
    monitoring records for Microgreen Freeze-Drying.
    """
    template = """
    You are an expert QA/QC Lead auditor for a Microgreen Freeze-Dried production facility.
    Review the following Critical Control Point (CCP) data and validate if it meets our 
    safety thresholds. 

    HACCP Data:
    - CCP Name: {{ccp_name}}
    - Recorded Value: {{recorded_value}}
    - Critical Limit: {{critical_limit}}
    - Action Taken: {{action_taken}}

    Task:
    1. Check if the recorded value violates the critical limit.
    2. If there is a violation, verify if the "Action Taken" was appropriate.
    3. Return ONLY a valid JSON object with the following schema:
    {
        "is_compliant": boolean,
        "violation_found": boolean,
        "recommendation": "string"
    }
    """
    
    # Inject runtime context
    prompt = template
    for key, value in ccp_data.items():
        prompt = prompt.replace(f"{{{{{key}}}}}", str(value))
        
    return prompt

if __name__ == "__main__":
    sample_ccp_data = {
        "ccp_name": "Freeze-Dryer Moisture Content (CCP-2)",
        "recorded_value": "4.5%",
        "critical_limit": "Max 5.0%",
        "action_taken": "None required, within limit"
    }
    print("Generated Prompt:\n", generate_haccp_validation_prompt(sample_ccp_data))

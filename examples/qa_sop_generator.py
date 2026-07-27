def generate_sop_prompt(sop_topic: str, facility_area: str, requirements: list) -> str:
    """
    Generates a structured prompt to draft Standard Operating Procedures (SOPs) 
    for the AgeWise Microgreen facility.
    """
    reqs_bulleted = "\n".join([f"- {req}" for req in requirements])
    
    prompt = f"""
    You are a Quality Management System (QMS) specialist writing documentation for 
    the AgeWise Microgreen Freeze-Drying plant.

    Please draft a formal Standard Operating Procedure (SOP) for the following topic:
    Topic: {sop_topic}
    Facility Area: {facility_area}

    The SOP MUST include the following key requirements and compliance checks:
    {reqs_bulleted}

    Format the SOP with the following strict sections:
    1. Purpose
    2. Scope
    3. Responsibilities
    4. Equipment/Materials Needed
    5. Step-by-Step Procedure (in imperative mood)
    6. Documentation & Records
    
    Ensure the tone is highly professional, compliant with food safety standards, 
    and leaves no room for ambiguity.
    """
    return prompt

if __name__ == "__main__":
    topic = "Sanitation and Allergen Management"
    area = "Freeze-Drying Trays & Processing Zone"
    reqs = [
        "Must use food-safe ethanol for wiping.",
        "Ensure zero cross-contamination with non-microgreen items.",
        "Log the time and initials of the sanitation operator."
    ]
    
    print("--- SOP Generation Prompt ---")
    print(generate_sop_prompt(topic, area, reqs))

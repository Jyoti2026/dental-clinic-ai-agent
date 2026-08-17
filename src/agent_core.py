from clinic_tools import check_appointment_availability, screen_patient_severity

class ArchitectureAgentEngine:
    """Orchestrates incoming messages to determine context execution paths."""
    def __init__(self, clinic_name: str):
        self.clinic_name = clinic_name

    def process_incoming_request(self, user_prompt: str, contextual_date: str = "2026-08-18") -> dict:
        print(f"\n⚡ Processing user request for {self.clinic_name}...")
        
        # Phase 1: Assess emergency triage constraints first
        triage_report = screen_patient_severity(user_prompt)
        
        # Structure conditional routing architecture matching agentic thought processing
        if "🚨 CRITICAL TRIAGE ALERT" in triage_report:
            return {
                "intent_classification": "EMERGENCY_FORWARD",
                "execution_summary": triage_report,
                "recommended_action": "Halt automatic systems. Trigger human receptionist phone patch immediately."
            }
        
        # Phase 2: Handle schedule inquiries if triage clears safely
        lower_prompt = user_prompt.lower()
        if "appointment" in lower_prompt or "schedule" in lower_prompt or "free" in lower_prompt or "open" in lower_prompt:
            calendar_status = check_appointment_availability(contextual_date)
            return {
                "intent_classification": "CALENDAR_LOOKUP",
                "execution_summary": f"{triage_report} | {calendar_status}",
                "recommended_action": "Display remaining open times directly to the patient interface interaction engine."
            }
            
        # Default fallback route loop configuration
        return {
            "intent_classification": "GENERAL_INQUIRY",
            "execution_summary": f"{triage_report} | Patient request: '{user_prompt}' did not trigger specific tool criteria.",
            "recommended_action": "Route to baseline LLM conversation block using the clinic informational knowledge database."
        }

if __name__ == "__main__":
    # Simulating standard agent operational environment execution
    agent = ArchitectureAgentEngine(clinic_name="Apex Dental Care")
    
    # Execution Test Run 1: Routine scheduling request
    case_1 = agent.process_incoming_request("Hi, are there any open appointments available for tomorrow?", "2026-08-18")
    print(f"Agent Engine Decision Matrix Output:\n{case_1}")
    
    # Execution Test Run 2: High-risk patient triage emergency
    case_2 = agent.process_incoming_request("Help, my tooth fell out and my gums are bleeding heavily!", "2026-08-18")
    print(f"\nAgent Engine Decision Matrix Output:\n{case_2}")

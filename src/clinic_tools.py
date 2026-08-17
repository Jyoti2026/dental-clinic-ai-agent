import datetime

# Mocking a live clinical scheduling ledger
DENTAL_CALENDAR_DB = {
    "2026-08-18": ["09:00", "10:00", "14:00"],  # Booked slots
    "2026-08-19": ["11:00", "15:00", "16:00"]
}

CRITICAL_EMERGENCY_KEYWORDS = ["bleeding", "broken jaw", "trauma", "severe swelling", "accident"]

def check_appointment_availability(date_str: str) -> str:
    """Queries clinical schedules to isolate empty runtime blocks."""
    try:
        # Validate baseline ISO date parameters
        target_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        date_key = str(target_date)
    except ValueError:
        return "❌ Error: Invalid structural format. Use YYYY-MM-DD format configuration."
    
    all_slots = ["09:00", "10:00", "11:00", "14:00", "15:00", "16:00"]
    booked = DENTAL_CALENDAR_DB.get(date_key, [])
    available_slots = [slot for slot in all_slots if slot not in booked]
    
    if not available_slots:
        return f"📅 Configuration for {date_key}: Complete capacity reached. No openings found."
    return f"📅 Open slots on {date_key}: {', '.join(available_slots)}"

def screen_patient_severity(patient_notes: str) -> str:
    """Automated extraction logic to identify high-risk triage configurations."""
    notes_lower = patient_notes.lower()
    triggered_alerts = [word for word in CRITICAL_EMERGENCY_KEYWORDS if word in notes_lower]
    
    if triggered_alerts:
        return f"🚨 CRITICAL TRIAGE ALERT: Immediate priority flagged. Trigger words identified: {triggered_alerts}. Route directly to trauma surgeons."
    return "✅ ROUTINE TRIAGE: Case categorized as elective/standard operations. Proceed to standard calendar booking pipeline."

if __name__ == "__main__":
    # Internal Unit Tests
    print(check_appointment_availability("2026-08-18"))
    print(screen_patient_severity("I need a routine cleaning next week."))
    print(screen_patient_severity("Severe bleeding after tooth extraction accident!"))

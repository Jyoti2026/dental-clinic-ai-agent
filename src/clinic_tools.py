import sqlite3
import datetime

DB_FILE = "dental_clinic.db"

def initialize_database():
    """Establishes persistent SQLite relational schema configuration."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS appointments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                appointment_date TEXT NOT NULL,
                appointment_time TEXT NOT NULL,
                UNIQUE(appointment_date, appointment_time)
            )
        """)
        # Insert initial mocked booked slots if table is empty
        cursor.execute("SELECT COUNT(*) FROM appointments")
        if cursor.fetchone()[0] == 0:
            mock_data = [
                ("2026-08-18", "09:00"),
                ("2026-08-18", "10:00"),
                ("2026-08-18", "14:00"),
                ("2026-08-19", "11:00")
            ]
            cursor.executemany("INSERT INTO appointments (appointment_date, appointment_time) VALUES (?, ?)", mock_data)
        conn.commit()

CRITICAL_EMERGENCY_KEYWORDS = ["bleeding", "broken jaw", "trauma", "severe swelling", "accident"]

def check_appointment_availability(date_str: str) -> str:
    """Queries persistent relational disk files to find unbooked openings."""
    try:
        target_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        date_key = str(target_date)
    except ValueError:
        return "❌ Error: Invalid structural format. Use YYYY-MM-DD format configuration."
    
    initialize_database()
    all_slots = ["09:00", "10:00", "11:00", "14:00", "15:00", "16:00"]
    
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT appointment_time FROM appointments WHERE appointment_date = ?", (date_key,))
        booked = [row[0] for row in cursor.fetchall()]
        
    available_slots = [slot for slot in all_slots if slot not in booked]
    
    if not available_slots:
        return f"📅 Schedule for {date_key}: Full capacity. No open slots found."
    return f"📅 Open persistent slots on {date_key}: {', '.join(available_slots)}"

def screen_patient_severity(patient_notes: str) -> str:
    """Automated extraction logic to identify high-risk triage configurations."""
    notes_lower = patient_notes.lower()
    triggered_alerts = [word for word in CRITICAL_EMERGENCY_KEYWORDS if word in notes_lower]
    
    if triggered_alerts:
        return f"🚨 CRITICAL TRIAGE ALERT: Immediate priority flagged. Trigger words identified: {triggered_alerts}."
    return "✅ ROUTINE TRIAGE: Standard operational pipeline case."

if __name__ == "__main__":
    initialize_database()
    print(check_appointment_availability("2026-08-18"))
    

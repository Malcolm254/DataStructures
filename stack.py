# hospital_files.py
from typing import List

# Start with an empty tray
patient_files: List[str] = []

# 📥 Add files (PUSH)
patient_files.append("Room 101 - Check Vitals")
patient_files.append("Room 204 - Administer Meds")
patient_files.append("Room 101 - Update Chart")

print("📋 Top of tray:", patient_files[-1])  # PEAK at top

# 📤 Process most recent file first (POP)
latest_task = patient_files.pop()
print(f"✅ Handled: {latest_task}")
print("📋 Remaining files:", patient_files)
# user_profile.py
from typing import Dict, Any

def parse_api_response(raw_data: Dict[str, Any]) -> Dict[str, str]:
    # Safe access with .get()
    username = raw_data.get("username", "anonymous")
    email = raw_data.get("contact", {}).get("email", "no-email@placeholder.com")
    
    # Update with validation
    profile: Dict[str, str] = {"username": username, "email": email}
    
    # Merge external preferences
    preferences = raw_data.get("preferences", {})
    profile.update({f"pref_{k}": str(v) for k, v in preferences.items()})
    
    return profile

if __name__ == "__main__":
    sample_payload = {
        "username": "dev_alex",
        "contact": {"email": "alex@dev.io"},
        "preferences": {"theme": "dark", "notifications": True}
    }
    print("📦 Parsed:", parse_api_response(sample_payload))
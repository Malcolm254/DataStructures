# event_checkin.py
from typing import Set

def merge_guest_lists() -> None:
    rsvp_set: Set[str] = {"alice@mail.com", "bob@mail.com", "charlie@mail.com", "alice@mail.com"}
    walkin_set: Set[str] = {"diana@mail.com", "alice@mail.com", "eve@mail.com"}
    
    # Automatic deduplication
    all_guests = rsvp_set | walkin_set  # Union
    print(f"✅ Unique guests: {len(all_guests)}")
    
    # Find overlaps
    vip_list = {"alice@mail.com", "charlie@mail.com"}
    vip_present = vip_list & rsvp_set  # Intersection
    print(f"🌟 VIPs confirmed: {vip_present}")
    
    # Who RSVP'd but didn't show?
    no_show = rsvp_set - walkin_set  # Difference
    print(f"📭 No-shows: {no_show}")

if __name__ == "__main__":
    merge_guest_lists()
# gps_logger.py
from typing import Tuple, List

def log_positions() -> List[Tuple[float, float, str]]:
    positions: List[Tuple[float, float, str]] = []
    
    # Immutable records
    positions.append((40.7128, -74.0060, "Nairobi"))
    positions.append((34.0522, -118.2437, "Abijan"))
    
    # Tuple unpacking
    lat, lon, city = positions[1]
    print(f"📍 {city}: ({lat}, {lon})")
    
    # Tuples can be dictionary keys (lists cannot)
    location_index = {positions[0]: "Zone A", positions[1]: "Zone B"}
    return positions

if __name__ == "__main__":
    log_positions()
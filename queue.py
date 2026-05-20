# car_yard.py
from collections import deque

# 🚗 Service line starts empty
service_line = deque()

# 📥 Cars arrive (ENQUEUE)
service_line.append("Toyota Camry - 2019")
service_line.append("Honda Civic - 2021")
service_line.append("Ford F-150 - 2018")

print("📍 Line waiting:", list(service_line))

# 📤 First car gets serviced (DEQUEUE)
next_car = service_line.popleft()
print(f"🔧 Now servicing: {next_car}")
print("📍 Updated line:", list(service_line))
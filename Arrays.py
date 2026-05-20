# shop_inventory.py
from typing import List

# 0: Bread, 1: Milk, 2: Eggs, 3: Butter, 4: Cheese
prices: List[float] = [2.50, 3.10, 4.00, 5.20, 6.75]

print("📦 Full shelf:", prices)

# 🔍 Access by index (position)
print("💰 Milk (index 1): $", prices[1])

# ✏️ Update price
prices[2] = 4.20  # Eggs price changed
print("🔄 Updated eggs price to $", prices[2])

# 📏 Slice a range (items 1 to 3)
dairy_section = prices[1:4]
print("🥛 Dairy prices:", dairy_section)
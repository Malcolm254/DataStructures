# restaurant_queue.py
from typing import List

def process_orders() -> None:
    orders: List[str] = []
    
    # Simulate incoming orders
    orders.append("Veggie Burger")
    orders.append("Caesar Salad")
    orders.insert(0, "VIP Table: Truffle Pasta")  # O(n) shift
    
    # Modify an order
    orders[1] = "Caesar Salad (No Croutons)"
    
    # Remove completed order if it exists
    if "Veggie Burger" in orders:
        orders.remove("Veggie Burger")  # O(n) search + O(n) shift
    else:
        print("⚠️  Warning: Veggie Burger order not found to remove")
    
    # Slice: next 2 orders for kitchen dispatch
    next_batch = orders[:2]
    print("📤 Dispatch:", next_batch)

if __name__ == "__main__":
    process_orders()
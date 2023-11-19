class Item():
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def fractional_knapsack(bag_capacity, items):
    items = sorted(items, key=lambda item:(item.profit/item.weight), reverse=True)
    profit = 0
    
    for item in items:     
        if item.weight < bag_capacity:
            profit += item.profit
            bag_capacity -= item.weight
        else:
            profit += item.profit/item.weight * bag_capacity
            bag_capacity = 0
            break
    
    return profit
        
bag_capacity = 50

items = [Item(60,10), Item(100,20), Item(120,30)]

max_profit = fractional_knapsack(bag_capacity, items)
print(max_profit)
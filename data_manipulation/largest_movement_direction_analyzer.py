prices = [100, 105, 102, 110, 95, 95, 120, 115, 130]
largest_movement_amount = None

for index in range(len(prices) -1):
    next_price = prices[index + 1]
    
    if next_price > prices[index]:
       change_movement = next_price - prices[index]
        
    else:
        change_movement = prices[index] - next_price
        
        
    
    if largest_movement_amount is None or change_movement > largest_movement_amount:
       largest_movement_amount = change_movement

    
       starting_price = prices[index]
       ending_price = prices[index + 1]
       
       starting_index = index
       ending_index = index + 1
       
      
       
       
print(largest_movement_amount)   
if  ending_price > starting_price:
    print("Direction: Increase")
    print(f"Starting_price: {starting_price}")
    print(f"Ending_price: {ending_price}")    
    print(f"Starting index: {starting_index}")
    print(f"Ending index: {ending_index}")          
                 
elif ending_price < starting_price:
    print("Direction: Decrease")
    print(f"Starting_price: {starting_price}")
    print(f"Ending_price: {ending_price}")    
    print(f"Starting index: {starting_index}")
    print(f"Ending index: {ending_index}")                 
            
else:
    print("Direction: Unchanged")
    print(f"Starting price: {starting_price}")
    print(f"Ending price: {ending_price}")
    print(f"Starung index: {starting_index}") 
    print(f"Ending index: {ending_index}")        
    
    
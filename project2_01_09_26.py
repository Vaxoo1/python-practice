prices = [100, 105, 105, 103, 110, 108, 115, 95, 95, 120]

# Increase section
increase_count = 0
increase_found = False
change_percentage = 0
total_increase = 0
largest_percentage = 0
largest_increase = 0

#unchange section
unchange_count = 0

# Decrease section
decrease_count = 0
decrease_found = False
largest_decrease = 0
total_decrease = 0
largest_decrease_percentage = 0
change_decrease_percentage = 0

for index in range(len(prices) -1):
    next_price = prices[index + 1]
    
    if next_price > prices[index]:
        increase_count += 1
        change_price = next_price - prices[index]
        total_increase += change_price
        
        change_percentage = change_price / prices[index] * 100
        
        if not increase_found:
            starting_increase_price = prices[index]
            ending_increase_price = prices[index + 1]
                       
            starting_increase_index = index
            ending_increase_index = index + 1
                       
            increase_found = True
            
            
        if change_price > largest_increase:
           largest_increase = change_price    
        
        if change_percentage > largest_percentage:
            largest_percentage = change_percentage              
        
                     
    elif prices[index] == next_price:
         unchange_count += 1        
            
    else:
        
         decrease_count += 1
         decrease_change_price = prices[index] - next_price
         total_decrease += decrease_change_price
         
         change_decrease_percentage = decrease_change_price / prices[index] * 100
         
         if not decrease_found:
            starting_decrease_price = prices[index]
            ending_decrease_price = prices[index + 1]
                          
            starting_decrease_index = index
            ending_decrease_index = index + 1
                          
            decrease_found = True
         
         if decrease_change_price > largest_decrease:
             largest_decrease = decrease_change_price
             
         if change_decrease_percentage > largest_decrease_percentage:
             largest_decrease_percentage = change_decrease_percentage
         


print("-------------------- Increase section ----------------")            
print(f"increase count: {increase_count}")
print(f"Largest increase: {largest_increase}")
print(f"Total increase: {total_increase}")       
print(f"Largest percentage: {largest_percentage:.2f}%")
print(f"First increase price: {starting_increase_price} --> {ending_increase_price}")     
print(f"First increase price index: {starting_increase_index} ---> {ending_increase_index}")


print("-------------------- Unchange section ---------------------")
print(f"Unchange count: {unchange_count}")


print("------------------- Decrease section ----------------------")
print(f"Decrease count: {decrease_count}")
print(f"Total decrease: {total_decrease}")
print(f"Largest decrease: {largest_decrease}")
print(f"Largest decrease percentage: {largest_decrease_percentage:.2f}%")
print(f"Starting decrease price: {starting_decrease_price} --> {ending_decrease_price}")
print(f"Starting decrease price index: {starting_decrease_index} --> {ending_decrease_index}")
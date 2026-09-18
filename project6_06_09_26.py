prices = [100, 105, 105, 103, 110, 108, 115, 95, 95, 120]
#Increase section
increase_count = 0
total_increase = 0
largest_increase_amount = None
largest_increase_percentage = None
first_increase_price = None
ending_increase_price = None

first_increase_price_index = None
ending_increase_price_index = None
increase_found = False


for index in range(len(prices) -1):
    next_price = prices[index + 1]
    
    if next_price > prices[index]:
        increase_count += 1
        
        change_increase = next_price - prices[index]
        total_increase += change_increase
           
        #First increase and index capture
        if not increase_found:
            largest_increase_amount = change_increase
            
            first_increase_price = prices[index]
            ending_increase_price = prices[index + 1]
                   
            first_increase_price_index = index
            ending_increase_price_index = index + 1
            
            largest_increase_percentage = change_increase / prices[index] * 100
            
            increase_found = True
        
        #Largest increase  condition      
        if change_increase > largest_increase_amount:
           largest_increase_amount = change_increase
        
        #Largest increase percentage condition
        change_percentage = (change_increase / prices[index] * 100)
        if change_percentage > largest_increase_percentage:
           largest_increase_percentage = change_percentage
           

if increase_found:
    print(f"Increase count: {increase_count}")
    print(f"Total increase amount: {total_increase}")
    print(f"Largest increase amount: {largest_increase_amount}")
    print(f"Largest increase percentage: {largest_increase_percentage:.2f}%")
    print(f"First increase price: {first_increase_price}")
    print(f"Ending increase price: {ending_increase_price}")
    print(f"First increase price index: {first_increase_price_index}")
    print(f"Ending increase price index: {ending_increase_price_index}")
else:
    print("No increase found")
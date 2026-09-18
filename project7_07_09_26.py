prices = [100, 105, 105, 103, 110, 108, 115, 95, 95, 120]
#Increase section
increase_count = 0
total_increase_amount = 0
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
        
        increase_change = next_price - prices[index]
               
        #Total increase amount
        total_increase_amount += increase_change
       
        if prices[index] == 0:
           change_percentage = None
        else:    
            #Change percentage
            change_percentage = (increase_change / prices[index] * 100)
        
        if largest_increase_percentage is None:
            largest_increase_percentage = change_percentage
            
        if change_percentage > largest_increase_percentage:
           largest_increase_percentage = change_percentage     
        
        
        if not increase_found:
          
           #Capuring first and ending prices and index 
           first_increase_price = prices[index]
           ending_increase_price = prices[index + 1]
          
           first_increase_price_index = index
           ending_increase_price_index = index + 1
          
           increase_found = True
        
        #Assigning the first increase_chnage value to lagrest increase amount   
        if largest_increase_amount is None:
            largest_increase_amount = increase_change   
        
        if increase_change > largest_increase_amount:
           largest_increase_amount = increase_change        
        
           
           
if increase_found:
   print(f"Increase count: {increase_count}")
   print(f"Total increase amount: {total_increase_amount}")
   print(f"Largest increase amount: {largest_increase_amount}")
   print(f"Largest increase percentage: {largest_increase_percentage:.2f}%")
   print(f"First increase price: {first_increase_price} --> {ending_increase_price}")
   print(f"First increase price index: {first_increase_price_index} --> {ending_increase_price_index}")
               
else:
    print("No increase found")            
              
          
       
       

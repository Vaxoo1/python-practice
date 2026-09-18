scores = [72, 85, 85, 63, 91, 78, 91, 55, 55, 96]

decline_count = 0
total_decline = 0
largest_decline = None
largest_decline_percentage = None
decline_found = False

for num in range(len(scores) -1):
    next_num = scores[num + 1]
    
    if scores[num] > next_num:
        decline_count += 1
       
        change_decline = scores[num] - next_num
        total_decline += change_decline

        if largest_decline is None:
           largest_decline = change_decline
        
        if change_decline > largest_decline:
            largest_decline = change_decline
        
        
        change_percentage = change_decline / scores[num] * 100
        if largest_decline_percentage is None:
           largest_decline_percentage = change_percentage
        
        if change_percentage > largest_decline_percentage:
           largest_decline_percentage = change_percentage
           
        if not decline_found:
           starting_decline_num = scores[num]
           ending_decline_num = scores[num + 1]
           
           starting_decline_index = num
           ending_decline_index = num + 1
           
           decline_found = True
           


print(f"Decline count: {decline_count}")
print(f"Total decline: {total_decline}")

if decline_found:
    print(f"Largest decline: {largest_decline}")
    print(f"Largest decline percentage: {largest_decline_percentage:.2f}%")
    print(f"Starting decline price: {starting_decline_num}")
    print(f"Ending decline price: {ending_decline_num}")
    print(f"Starting decline index: {starting_decline_index}")
    print(f"Ending decline index: {ending_decline_index}")
    
else:
    print("Not found ")               
               
               
           
           
           
           
        

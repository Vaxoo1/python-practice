scores = [72, 85, 80, 92, 70, 70, 95, 88, 100]

largest_movement = None

#Increase Section
increase_count = 0
total_increase = 0
largest_increase = None
increase_found = False

#Decrease Section
decrease_count = 0
total_decrease = 0
largest_decrease = None
decrease_found = False

#Unchange Section
unchange_count = 0



for index in range(len(scores) -1):
    next_score = scores[index + 1]
    
    #Condition for fiding largest movement magitude 
    if next_score > scores[index]:
        #Another variable to decide the direction
        change_movement = next_score - scores[index]
         
        increase_count += 1
        increase_score = next_score - scores[index]
        total_increase += increase_score
        
        if largest_increase is None or increase_score > largest_increase:
            largest_increase = increase_score
            
        if not increase_found:
           starting_increase_price = scores[index]
           ending_increase_price = scores[index + 1]
           
           starting_increase_index = index
           ending_increase_index = index + 1      
           increase_found = True
  
  
    if scores[index] > next_score:
         #Same Direction varaible
         change_movement = scores[index] - next_score
         
         decrease_count += 1
         decrease_score = scores[index] - next_score
         total_decrease += decrease_score
         
         if largest_decrease is None or decrease_score > largest_decrease:
             largest_decrease = decrease_score
             
         if not decrease_found:
             starting_decrease_price = scores[index]
             ending_decrease_price = scores[index + 1]
             
             starting_decrease_index = index
             ending_decrease_index = index + 1
             decrease_found = True
             
             
    if scores[index] == next_score:
        unchange_count += 1
        change_movement = 0
        
    #Direction condition
    if largest_movement is None or change_movement > largest_movement:
        largest_movement = change_movement
        starting_largest_movement = scores[index]
        ending_largest_movement = scores[index + 1]
        
        starting_largest_movement_index = index
        ending_largest_movement_index = index + 1
        
        
print(f"Number of increase: {increase_count}")
print(f"Number of decreases: {decrease_count}")                         
print(f"Number of unchanged: {unchange_count}")

print(f"Total increase: {total_increase}")
print(f"Total decrease: {total_decrease}")

print(f"Largest increase: {largest_increase}")
print(f"Largest decrease: {largest_decrease}")

print(f"First increase: {starting_increase_price} --> {ending_increase_price}")
print(f"Indexes: {starting_increase_index} --> {ending_increase_index}")

print(f"First decrease: {starting_decrease_price} --> {ending_decrease_price}")
print(f"Indexes: {starting_decrease_index} --> {ending_decrease_index}")

print()
#Direction 
if starting_largest_movement < ending_largest_movement:
   print(f"Largest absolute movement: {largest_movement}")
   print(f"scores: {starting_largest_movement} --> {ending_largest_movement}")
   print(f"Indexes: {starting_largest_movement_index} --> {ending_largest_movement_index}")
   print("Direction: Increase")
   
elif starting_largest_movement > ending_largest_movement:
    print(f"Largest: {largest_movement}")
    print(f"scores: {starting_largest_movement} --> {ending_largest_movement}")
    print(f"Indexes: {starting_largest_movement_index} --> {ending_largest_movement_index}")
    print("Direction: Decrease")   
    
else:
    print("Direction: Unchange")    
   
#Name and Age inputs
name = input("Enter your name: ")
age = input("Enter your age: ")

#Choose an activity list input
activity_list = ['Music Jam Session (2 hours, easy, $5 fee)','Science Experiments Lab (3 hours, moderate, $10 fee)','Sports Leadership Training (4 hours, challenging, $12 fee)']

print('Choose an activity: ')
print(f'1. {activity_list[0]}')
print(f'2. {activity_list[1]}')
print(f'3. {activity_list[2]}')
chosen_activity = input("Enter the number of your chosen activity: ")

#Chosen activity fee
if chosen_activity == '1':
    activity_fee = 5
elif chosen_activity == '2':
    activity_fee = 10
elif chosen_activity == '3':
    activity_fee = 12


#Meal options list input
meal_options = ['Standerd', 'vegeterian', 'Dairy-free', 'Gluten-free','No meal']

print('Choose a meal option: ')
print(f'1. {meal_options[0]}')
print(f'2. {meal_options[1]}')
print(f'3. {meal_options[2]}')
print(f'4. {meal_options[3]}')
chosen_meal = input("Enter the number of your chosen meal: ")

#Chosen meal fee
if chosen_meal == '1' or chosen_meal == '2' or chosen_meal == '3':
    meal_fee = 7
else:
    meal_fee = 0

#Total fee
total_fee = activity_fee + meal_fee

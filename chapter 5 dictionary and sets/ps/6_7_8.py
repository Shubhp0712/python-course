d = {}

for i in range(4):
    p = input("Enter the key for your favourite language :")
    q = input("Enter the value for your favourite language :")

    d.update({p : q})

print("Initial dictionary :", d)

# output for problem 6:
# Enter the key for your favourite language :shubh
# Enter the value for your favourite language :hindi
# Enter the key for your favourite language :samarth
# Enter the value for your favourite language :english
# Enter the key for your favourite language :mir
# Enter the value for your favourite language :gujrati
# Enter the key for your favourite language :jay
# Enter the value for your favourite language :french
# Initial dictionary : {'shubh': 'hindi', 'samarth': 'english', 'mir': 'gujrati', 'jay': 'french'}

# output for problem 7:
# Enter the key for your favourite language :shubh
# Enter the value for your favourite language :hindi
# Enter the key for your favourite language :samarth
# Enter the value for your favourite language :english
# Enter the key for your favourite language :mir
# Enter the value for your favourite language :gujrati
# Enter the key for your favourite language :shubh
# Enter the value for your favourite language :french
# Initial dictionary : {'shubh': 'english', 'samarth': 'gujrati', 'mir': 'french'}

# output for problem 8:
# Enter the key for your favourite language :shubh
# Enter the value for your favourite language :hindi
# Enter the key for your favourite language :samarth
# Enter the value for your favourite language :gujrati
# Enter the key for your favourite language :mir
# Enter the value for your favourite language :hindi
# Enter the key for your favourite language :jay
# Enter the value for your favourite language :english
# Initial dictionary : {'shubh': 'hindi', 'samarth': 'gujrati', 'mir': 'hindi', 'jay': 'english'}

# Here it means that when two keys are same then the value of the key will be updated with the new value.but values of the key is possible to be same.
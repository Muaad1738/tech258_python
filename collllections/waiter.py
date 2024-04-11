# Waiter helper

prices = {
    "wings" : 1.5,
    "chips" : 2,
    "breadsticks" : 0.5,
    "garlic bread" : 2,
    "steak" : 5,
    "sea bass" : 4,
    "butter chicken" : 3.5,
    "lamb shank" : 4,
    "ice cream" : 2,
    "cheesecake" : 2,
    "baklava" : 2.5,

}

#Greet the customer
print("Welcome To The Restaurant")

#list of starts
starters = ["wings", "chips", "breadsticks", "garlic bread"]
print(starters)

#take starter
print("what would you like to have as a starter?")
cus_starter = input()

mains = ["steak","sea bass", "butter chicken", "lamb shank"]
print(mains)

print("what would you like to have as a main?")
cus_main = input()

deserts = ["ice cream, cheesecake, baklava"]
print(deserts)

print("what would you like to have as a desert?")
cus_desert = input()

cus_order_list = []

cus_order_list.append(cus_starter)
cus_order_list.append(cus_main)
cus_order_list.append(cus_desert)
print(cus_order_list)





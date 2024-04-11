# Set and frozen lists

#create a ste

fruits = {"apple", "banana", "cherry"}
print(fruits)

# sets are unordred and un indexed

fruits.add("orange")
print(fruits)

fruits.remove("apple")
print(fruits)

#adding dups
fruits.add("banana")
print(fruits)

# forezen sets

frozenset = frozenset(["hello", "world"])
print(frozenset)

normal_set = {"lets", "learn"}
normal_set.add(frozenset)
print(normal_set)


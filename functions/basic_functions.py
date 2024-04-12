# functions

# def addition(int1, int2):
#     return int1 + int2
#
# print(addition(2,2):
# print(addition(10,15):

def addition(int1=2, int2=2):
    return int1 + int2

print(addition())
print(addition(int2=15))

# multiple argument

def multi_args(*multiargs):
    for arg in multiargs:
        print(arg)

multi_args(1,2,3,4)

# type hints
def division 
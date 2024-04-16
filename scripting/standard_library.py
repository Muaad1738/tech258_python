# python standard libary
# import random
import math
import os
import random
import sys
import builtins
import requests


#standard libary consist if mo

# print(random.random))
# print(random.ranrandge))

# math demo
#
# num_float = 23.66
# print(math.ceil(num_float))
# print(math.floor(num_float))
# # print(math.pi)
# # print(f"remainder from 1/5: {math.remainder(1,5)}")
#
#
# # 0s demo
#
# # reutrning current working directory
#
# working_dir = os.getcwd()
# print(f"current working directory: {working_dir}")
#
# # get user
# username = os.environ['USER'] or os.environ.get['USER']
# print(f"username: {username}")
#
# # cpu cores
#
# cpu_cores = os.cpu_count()
# print(f"amount of cpus: {cpu_cores}")
#
# # make directory
#
# os.mkdir("test_dir")

# sys demo

#
# # builtins
#
# for name in dir(builtins):
#     if name[0].islower():
#         print(name)
#

# requests
request_bbc = requests.get("https://bbc.co.uk/")
print(request_bbc.status_code)

print(request_bbc.content)

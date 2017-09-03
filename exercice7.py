#!usr/bin/python3.4

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

new_list = [i for i in a if i%2 == 0]
print(new_list)
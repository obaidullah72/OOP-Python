my_word = "Hello World"
rev_word = my_word[::-1]
print(rev_word)


my_diction = {'name' : 'Ali', 'age':25, 'city' : 'Lahore'}
for key, value in my_diction.items():
    print(key, ':', value)

my_list = [1,2,3,4,6,7,8,9,2,3,4,5,5]
for item in my_list:
    print(item)
print(my_list)
sorted_list = sorted(my_list)
print(sorted_list)
rev_sort_list = sorted(my_list, reverse= True)
print(rev_sort_list)

my_tuples = (1,2,3,4,5)
for items in my_tuples:
    print(items)
print(my_tuples)



num_rows = 5
for i in range(1, num_rows+1):
    # for j in range(num_rows - i):
    #     print(" ", end="")
    for k in range(2 * i -1):
        print("*" , end=" ")

    print()
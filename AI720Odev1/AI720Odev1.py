#Create two lists. The first list should consist of odd numbers. The second list is should consist of even numbers.
list1=[1,3,5,7,9]
list2=[0,2,4,6,8]
print(list1)
print(list2)
print("******************************************************************************")
#Merge these two lists. Multiply all values in the new list by 2.
list1.extend(list2)
list1.sort()
print(list1)
print("**************************************************")
my_new_list = [i * 2 for i in list1]
print(my_new_list)
print("**************************************************")
#Use a loop to print the data type of the all values in the new list.
i=0
for i in my_new_list:
    print(type(i))

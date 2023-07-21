first_value=int(input("insert the number"))
second_value=int(input("insert the number"))
third_value=int(input("insert the number"))
fourth_value=int(input("insert the number"))

my_list= [first_value , second_value, third_value , fourth_value ]
a=my_list[0]

for x in my_list:
    if x > a:
        a = x
print("the most valuable is" ,a)

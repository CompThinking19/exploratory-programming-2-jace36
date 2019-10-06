def books(pages):
    if type(pages) != list:
        raise TypeError("Not a list")
    for element in pages:
        if element == 20:
                return "yes"
#Hopefully, this will be able to print out a type error and yes if I did this correctly

pages = [10, 11, 12, 13]
pos_count = 0
for num in pages:
        if num >= 0:
            pos_count += 1
print("Positive numbers in the list: ", pos_count)
#Using parantheses and quotation marks are the only way that it will print the positive number in the list

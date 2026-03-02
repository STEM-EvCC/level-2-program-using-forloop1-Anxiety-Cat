#the notes here were done on 3/2/2026 before class, after the actual assignment was already complete.
#missed the for loop lecture and wanted to get the notes added for my own reference, as I tend to go back and read through them to help me remember concepts
#the only commit today was to add the class.py file here.

#Basic For Loop
#for iterating over a set range of values
grocery_list = ["eggs", "milk", "pizza", "cereal"]
#for each item in list print item:
for x in grocery_list:
    print(x)
#print each letter in a word
for x in "Snorlax":
    print(x)
print("")
print("")
#can use break in for loops to stop it before it iterates through all the items
for x in grocery_list:
    print(x)
    if x == "pizza":
        break
    print(x)
#we can use continue to stop current iteration of the loop and continue to the next
for x in grocery_list:
    if x == "pizza":
        continue
    print(x)
#range() iterates a specific number of times
#ranges use index values
for x in range(8):
    print(x)
for x in range(4):
    print(x)
else:print("Sentence finished")
#nested for loops
spooky_adjectives = ["Frightful", "Scary", "Haunting"]
monster_list = ["Ghost", "Mummy", "Mike Wiczowski"]
for x in spooky_adjectives:
    for y in monster_list:
        print(x,y)
#for loops cannot be empty

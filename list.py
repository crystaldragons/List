import time

numsList = [7, 6, 23, 8.18, 18, 8, 7.2, 85, 915, 12]
print (numsList[-2])
time.sleep(0.5)
print (numsList[1])
time.sleep(0.5)
math = ((numsList[0]) + (numsList[1]) + (numsList[2]) + (numsList[3]) + (numsList[4]) + (numsList[5]) + (numsList[6]) + (numsList[7]) + (numsList[8]) + (numsList[9])) / 10
print(math)

stringsList = ["abc", "123", "2332", "aBBA", "heelloo", "1212", "DcEfD"]
count = 0
one = 1
for s in stringsList:
    if s[0].lower() == s[-1].lower():
        count = count + one
time.sleep(0.5)
print(count)
time.sleep(0.5)

pesto_counter = 0
foodlist = []

for i in range(8):
    food = input("What is your favorite food?(no plurals pls!) ")
    if food == "Pesto":
        pesto_counter = pesto_counter + one
    else:
        other_food = food
        foodlist.append(other_food)

print("Pesto is loved by ",pesto_counter, "people!")
for i in range(pesto_counter):
    print("I like pesto")
    time.sleep(0.3)
print("Other foods:", foodlist)
time.sleep(0.7)

cerealList = []

for i in range(5):
    cereal = input("Choose a cereal: ")
    if cereal == (("Sultana") or ("Weetbix") or ("Bran")):
        print("Good choice!")
    else:
        cerealList.append(cereal)
        print(cerealList)
        break

print("End of code!")

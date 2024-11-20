string = ["Ехал", "грека", "через", "Барабан", "арбалет", "абрикос"]
count = 0
for i in string:
    if "б" in i.lower():
        count += 1
print(count)

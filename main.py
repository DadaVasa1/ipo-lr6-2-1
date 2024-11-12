l = ["Ехал", "грека", "через", "Барабан", "арбалет", "абрикос"]
count = 0
for i in l:
    for j in i:
        if j.lower() == 'б':
            count += 1
            break
print(count)
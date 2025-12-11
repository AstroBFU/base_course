import random
flowers = ['Тюльпан', 'Роза', "Люпин", "Борщевик"]
colors = ["White", 'Blue', 'Gray', 'Red', 'Yellow', 'Orange']
lense = len(colors)-1
for i in range(len(colors)):
    colors[i] = colors[random.randint(0, lense)]
print(colors)
slownik = dict(zip(flowers, colors))
print(slownik)

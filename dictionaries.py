rooms = dict(living=True, bath=False)
rooms2 = {'living': True, 'bath': False}
rooms3 = dict(lving=False, bed=True, bath=True, kitchen=True)
kittens = dict(number=2, cute=True, loving=True, color="grey", breed="Nabby")
print(rooms)
print(rooms2)
print(rooms['living'])
print(rooms2['bath'])
print(kittens)
print('**********************')
for value in kittens.values():
    print(value)
print('**********************')
for value in rooms.values():
    print(value)
print('**********************')
for value in rooms2.values():
    print(value)
print('**********************')
for value in rooms3.values():
    print(value)
print('**********************')
for key in kittens.keys():
    print(key)
print('**********************')
for key in rooms.keys():
    print(key)
print('**********************')
for key in rooms2.keys():
    print(key)
print('**********************')
for key in rooms3.keys():
    print(key)
print('**********************')
print(rooms.items())
print(rooms2.items())
print(rooms3.items())
print(kittens.items())
print('**********************')
for item in kittens.items():
    print(item)
print('**********************')
for item in rooms3.items():
    print(item)
print('**********************')
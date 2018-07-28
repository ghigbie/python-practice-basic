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
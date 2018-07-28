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
print('**********************')
for key, value in kittens.items():
    print(key, ' --- ', value)
print('**********************')
for key, value in rooms3.items():
    print(key, ' --- ', value)
print('**********************')
for key, vlaue in rooms2.items():
    print(key, ' --- ', value)
print('**********************')
for key, value in kittens.items():
    print(f"The key is {key} & the value is {value}")
print('********* keys *************')
print("number" in kittens)
print("cute" in kittens)
print("loving" in kittens)
print("color" in kittens)
print('********** values ************')
print(2 in kittens.values())
print(True in kittens.values())
print('grey' in kittens.values())
print('******** clear **************')
doggies = dict(name=True, color="Golden", large=True)
#clear removes all items from a list
print(doggies)
doggies.clear()
print(doggies)
print('********* copy *************')
kittens2 = kittens.copy()
print(kittens2)
print('********** get ************')
print(kittens.get('size'))
print('*********** pop ***********')
#removes an item from a list when a key is passed in 
doggies = kittens.copy()
print(kittens2)
print(kittens2.pop('color'))
print(kittens2)
print('********* popitem *************')
#removes an item from the list - I think at radom
kittems2.popitem()
print(kittens2)
print('**********************')
# while True:
#     for i in range(348752):
#         while False:
#             raise ValueError

for i in range(8): # range-object [0,1,2,3,4,5,6,7] 
    pass 

names = ['dan', 'dave', 'damien']
for n in names:
    pass

password = 'avocado'
p = input('Enter your super secret password: ')
while p != password:
    print('INCORRECT')
    p = input('Enter your super secret password: ')

# break
# continue

for i in range(5):
    if i == 2:
        continue
    print(i)

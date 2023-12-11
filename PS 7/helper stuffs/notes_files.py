## FILES
'''
# METHOD 1 Open & Close
afile = open('/Volumes/Data stuffs/Python/LCCL_Python2/PS 7/helper stuffs/jigglypuff.txt', 'r')
print(afile.name)
print(afile.mode)
print(type(afile))

# do something with the file
afile.close()
print(afile.name)
print(afile.mode)
'''
# METHOD 2 Open & Close
with open('/Volumes/Data stuffs/Python/LCCL_Python2/PS 7/helper stuffs/OMEGA JIGGLYPUFF HIGH LORD.txt', 'r') as afile:
    # Reading a file
    content = afile.read() # returns a string
    # content = afile.read(100) # returns a string
    # content = afile.readlines() # returns a list
    # content = afile.readline(30) # returns a string
    # print(content)
    # content = afile.readline() # returns a string
    # print(content)
    # for line in afile:
    #     print('Element:', line, end='')

#     print(afile.closed)
# print(afile.closed)
# do something to afile -- FAIL
'''
# Writing to file
with open('/Volumes/Data stuffs/Python/LCCL_Python2/PS 7/helper stuffs/OMEGA JIGGLYPUFF HIGH LORD.txt', 'w') as afile:
    afile.write('hahahahahahahahahaahah\n')
    afile.write('HAR HAR')
    afile.seek(0)
    afile.write('begin')
    afile.write('begin')
'''
# Appending to file
with open('/Volumes/Data stuffs/Python/LCCL_Python2/PS 7/helper stuffs/OMEGA JIGGLYPUFF HIGH LORD.txt', 'a') as afile:
    afile.write('bye')


# Reading and writing
with open('/Volumes/Data stuffs/Python/LCCL_Python2/PS 7/helper stuffs/newfile.txt', 'r+') as afile:
    afile.write('HOHO')

with open('/Volumes/Data stuffs/Python/LCCL_Python2/PS 7/helper stuffs/newfile.txt', 'w+') as afile:
    afile.write('HOHO HEIL LORD HIGHEST PUFF')

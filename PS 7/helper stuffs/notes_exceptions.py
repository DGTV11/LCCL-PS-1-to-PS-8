# Error Handling, Exception Handling

try:
    eee = open('abcdef.txt', 'w')
    # stub
    # stub

except (FileNotFoundError, IndexError):
    print('There is an error')
except TypeError:
    # handle differently here
    print('HEIL HIGHEST LORD JIGGLYPUFF!!! (its a type error)')
else:
    pass
    # handle other errors another way
finally:
    eee.close()
    # do this no matter what

raise NotImplementedError('I AM YOUR LORD KNEEL BEFORE ME MUAHHAHAHAHAAH NO TRY CATCH CAN SAVE YOU NOW')
# code...
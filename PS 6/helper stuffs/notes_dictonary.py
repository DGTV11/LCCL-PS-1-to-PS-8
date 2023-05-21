d = dict()
d = {}
d = {
    "Singapore" : "sg",
    "Malaysia"  : "my",
    "Thailand"  : "th",
}

# accessing a value in dict
d['Singapore']
d.get('Singapore')

# adding a k-v pair to dict
d['Japan'] = 'jp'

d.setdefault('United States', 'us')
d.setdefault('Australia', 'au')

e = {
    'Vietnam'       : 'vn',
    'Philippines'   : 'ph'
}
f = [('Canada', 'ca'), ('Indonesia', 'id')]
print(d)
d.update(e)
print(d)
d.update(f)
print(d)
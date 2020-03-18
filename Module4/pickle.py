''' persistence.py:

    Illustrates the pickle module.

    Output:
['pickle', 'mylist', 'mytup', 'mytext', 'myhash', 'f']
['pickle']
['pickle', 'f', 'mylist', 'mytup', 'mytext', 'myhash']
'''

import pickle

mylist = [1, 2, 3]
mytup = (4, 5, 6)
mytext = "ten"
myHash = { 'alist': mylist, 'atuple': mytup, 'astring': mytext}

#pickle the objects
with open('keep.dat', 'wb') as f:
    pickle.dump(mylist, f)
    pickle.dump(mytup, f)
    pickle.dump(mytext, f)
    pickle.dump(myhash, f)
print([item for item in vars() if item[0] != '_'])

#delete the objects
del mylist; del mytup; del mytext; del myhash; del f
print([item for item in vars() if item[0] != '_'])

# Reconstitute the objects
with open('keep.dat','rb') as f:
    alist = pickle.load(f)
    atup = pickle.load(f)
    atext = pickle.load(f)
    ahash = pickle.load(f)
print([item for item in vars() if item[0] != '_'])

import hashlib
#import cryptography


def hash(mystring):
    first = hashlib.sha512()
    by = bytes(mystring, 'utf-8')
    first.update(by)
    return first.hexdigest()

#def passhash(mystring)

from hashlib import sha256
from random import randint

def hashThis(x):
    hash=sha256();
    hash.update(str(x).encode());
    return int(hash.hexdigest(),16);

def check (h,h2):
    if (h2 == h):
        return True
    else:
        return False

#AUTHENTICATION /random integers
p = 48731
q = 443
g = 11444
t = 8

#keys
s = randint(1,q)
v = pow(g,-s,p)
#pick random r
r = randint(1, q - 1)
x = pow(g, r, p)

#hash x
h = hashThis(x)

#pick random e
e = randint(1, pow(2,t)-1)

#compute y
y = (r + s*e) % q

#compute x'
xprim = (pow(g,y)*pow(v,e)) % p
h2 = hashThis(xprim)

#check h(x')

result = check(h,h2)
print(result)

# print(h)
# print(h2)
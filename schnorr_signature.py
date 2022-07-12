from hashlib import sha256
from random import randint

def hashThis(x,m):
    hash=sha256();
    hash.update(str(x).encode());
    hash.update(m.encode());
    return int(hash.hexdigest(),16);

def check (e,e2):
    if (e2 == e):
        return True
    else:
        return False

#AUTHENTICATION /random integers
p = 48731
q = 443
g = 11444
t = 8
message = 'This is random message'

#keys
s = randint(1,q)
v = pow(g,-s,p)

#pick random r
r = randint(1, q - 1)
x = pow(g, r, p)

#pick e
e = hashThis(x,message) % q

#compute y
y = (r + s*e) % q

#compute x'
xprim = (pow(g,y)*pow(v,e)) % p
e2 = hashThis(xprim,message) % q

#check h(x')

result = check(e,e2)
print(result)

# print(e)
# print(e2)
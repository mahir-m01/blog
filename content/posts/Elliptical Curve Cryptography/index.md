---
title: ECC CTFs are Interesting
date: 2025-09-29
draft: false
tags:
  - Cryptograpahy
  - ECC
---



I was reviewing a CTF that my friend shared with me and I came across a question about 'Elliptical Curve Cryptography'. I haven't yet explored the deeper waters of cryptography and this one was pretty new to me. But hey, thats the essence of CTFs and I always appreciate a CTF that encourages you to explore and research instead of expecting you to know everything to be able to solve the question it offers. 
And during my research, I came across an amazing github repo article that explains Elliptical Curve Cryptography beautifully. My colleagues are sick and tired of hearing me say this but it is one of the best explanations to any topic I've encountered thus far. 

{{< github repo="elikaski/ECC_Attacks" showThumbnail=true >}}

---

## The Challenge 

 The challenge provided 2 files and absolutely no context. So I had to go into this pretty much blind.

### ECC.py 

```python
from secrets import a, b  
from collections import namedtuple  
from Crypto.Util.number import inverse, bytes_to_long  
  
FLAG = b"<REDACTED>"  
coordinate = namedtuple("coordinate", "x y")  
  
o = 'inf'  

def check(P):  
    if P == o:  
        return True  
    else:  
        return (P.y**2 - (P.x**3 + a*P.x + b)) % p == 0 and 0 <= P.x < p and 0 <= P.y < p  
  
  
def pinverse(P):  
    if P == o:  
        return P  
    return coordinate(P.x, -P.y % p)  
  
  
def addition(P, Q):  
    if P == o:  
        return Q  
    elif Q == o:  
        return P  
    elif Q == pinverse(P):  
        return o  
    else:  
        if P == Q:  
            l = (3*P.x**2 + a)*inverse(2*P.y, p)  
            l%= p  
        else:  
            l= (Q.y - P.y) * inverse((Q.x - P.x), p)  
            l%= p  
    Sx = (l**2 - P.x - Q.x) % p  
    Sy = (l*(P.x - Sx) - P.y) % p  
    S = coordinate(Sx, Sy)  
    assert check(S)  
    return S  
    
def dbl(P, n):  
    Q = P  
    S = o  
    while n > 0:  
        if n % 2 == 1:  
            S = addition(S, Q)  
        Q = addition(Q, Q)  
        n = n // 2  
    assert check(S)  
    return S  
def public_key():  
    d = bytes_to_long(FLAG)  
    return dbl(G, d)  
  
p=8027944432202837970016382166567613248055695684315346001687786051508079095211  
# a and b are hidden :(  
gx =2105875689926932895143196884562047110500169848659102540268132432000998177662  
gy = 229423364975599771276867046437732535419264207423006298355584008095715972502  
G = coordinate(gx, gy)  
Q = public_key()  
print(Q)
```

### Output.txt

```
coordinate(x=3685899851710902647676109902198159056110437731756939136804788198715504103708, y=259383739652175557073121224113233231149464856533427701609450332409012223263)
```

---

## Analysis & Solution 

### 1) Compute the Curve Parameters

The first step  is to compute the value of `a` and `b` before we can analyse further. The values **`a`** and **`b`** are the **curve parameters** that define the specific elliptic curve.


```python 
from Crypto.Util.number import inverse

p = 8027944432202837970016382166567613248055695684315346001687786051508079095211
Gx = 2105875689926932895143196884562047110500169848659102540268132432000998177662  
Gy = 229423364975599771276867046437732535419264207423006298355584008095715972502  
Qx = 3685899851710902647676109902198159056110437731756939136804788198715504103708  
Qy = 259383739652175557073121224113233231149464856533427701609450332409012223263

# Compute curve parameters a and b
# The elliptic curve equation is: y^2 = x^3 + a*x + b (mod p)
# We have two points (G and Q) on the curve, so we can solve for a and b

# Step 1: compute numerator and denominator to solve for 'a'
# Derived from: gy^2 - qy^2 = (gx^3 + a*gx + b) - (qx^3 + a*qx + b) mod p
num = (pow(gy, 2, p) - pow(qy, 2, p) - (pow(gx, 3, p) - pow(qx, 3, p))) % p
den = (gx - qx) % p

# Step 2: compute 'a' using modular inverse
a = (num * inverse(den, p)) % p

# Step 3: compute 'b' using one of the points (G)
b = (pow(gy, 2, p) - pow(gx, 3, p) - (a * gx)) % p

print("Computed curve parameters:")
print("a =", a)
print("b =", b)

```

---
### 2) Verify Singularity 

Now that we have all the required information (to an extent), primarily `a` and `b` , in my opinion its best practice to test whether the curve is singular or elliptical. Depending on the result our exploit paths will differ significantly.

A non-singular curve is a curve whose certain value, called the "discriminant" of the curve, is nonzero. It holds when its parameters `𝑎` and `𝑏` satisfy the inequality:

{{< katex >}} 
\(4a^3 + 27b^2  \not = 0\)

A curve that does not satisfy this inequality has a "problematic" point called a `singular point`. There are two types of such points: node and cusp

**What this means:**

- The curve has a **cusp** or a  **node (self-intersection)** instead of being smooth.
    
- Because of this, the set of points on the curve **does not form a proper group** under standard elliptic curve addition.


{{< alert icon="check" cardColor="#b085d3" iconColor="#3b1d57" textColor="#f1faee" >}}
The curve does happen to be singular and is therefore vulnerable
{{< /alert >}}

---
### 3) Exploiting  the Vulnerability 

The following code from the github article exploits Elliptical Curves that are **singular**:

```sage
p = 8027944432202837970016382166567613248055695684315346001687786051508079095211  
a = 57276030533159328146887045530181492991804891249085933575331289605  
b = 4890108522805667613288743457538583820154692228816052112017335705944231712111  
  
assert (4*a^3 + 27*b^2) % p == 0  
  
Gx = 2105875689926932895143196884562047110500169848659102540268132432000998177662  
Gy = 229423364975599771276867046437732535419264207423006298355584008095715972502  
Qx = 3685899851710902647676109902198159056110437731756939136804788198715504103708  
Qy = 259383739652175557073121224113233231149464856533427701609450332409012223263  
  
x = GF(p)["x"].gen()  
f = x^3 + a*x + b  
roots = f.roots()  
  
assert len(roots) == 2 # two roots, so one must be double  
if roots[0][1] == 2:  
    double_root = roots[0][0]  
    single_root = roots[1][0]  
else:  
    double_root = roots[1][0]  
    single_root = roots[0][0]  
  
print("double root:", double_root)  
print("single root:", single_root)  
  
# map G and Q to the new "shifted" curve  
Gx = (Gx - double_root)  
Qx = (Qx - double_root)  
  
# Transform G and Q into numbers g and q, such that q=g^n  
t = double_root - single_root  
t_sqrt = t.square_root()  
  
def transform(x, y, t_sqrt):  
    return (y + t_sqrt * x) / (y - t_sqrt * x)  
  
g = transform(Gx, Gy, t_sqrt)  
q = transform(Qx, Qy, t_sqrt)  
print("g:", g)  
print("q:", q)  
  
# Find the private key n  
print("Factors of p-1:", factor(p-1))  
print("Calculating discrete log for g and q...")  
found_key = discrete_log(q, g)  
print("Found private key:", found_key)  
  
from Crypto.Util.number import long_to_bytes  
print("The secret is:", long_to_bytes(found_key).decode())
```

When I first tried it worked almost 'too-well'. I wonder if the creator took an inspiration from the same article to create the question. Nevertheless, it was fun to solve. 

---
## Conclusion

Obviously I did not get into the depths of Elliptical Curve Cryptography here, you can check out the github article for that. This was more of a documentation for one of the questions I encountered.  Its about time I get well versed with ECC now... 

---

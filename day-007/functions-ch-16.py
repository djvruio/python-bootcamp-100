# chapter 16
# def name(arg1, arg2, ..., argn):
#    statements
#    return --> optional

def times(x, y):
    return x * y

x = times(2, 2)
y = times(3.14, 4)
print(x, y)
z = times('Ni', 3) # functions are typeless
print(z)
a = times(4, 'No')
print(a)

# b = times('Dar', 'Raf') fails
# print(b)

def intersect(seq1, seq2):
    res = []                #start empty
    for x in seq1:          # scan seq 1
        if x in seq2:       # look up common item
            res.append(x)   # Add to end
    return res

s1 = "SPAM"
s2 = "SCAM"

print(intersect(s1, s2))

t1 = "SPAMSSS"
t2 = "MORASS"

print(intersect(t1, t2))

print([x for x in t1 if x in t2])

# polimorphims
x = intersect([1, 2, 3], (2, 4, 6, 0))
print(x)

# functions avoid code redundancy, are basic unit of code reuse, divide complex system 
# into maneageable parts.
# def creates a function object
# return None by default without a return statement
#

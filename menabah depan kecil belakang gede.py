a = [6, 1, 5]

besar = 0
kecil = a[0]

for i in range (len(a)):
    for j in range (len(a)):
        print (a[i], a[j])
        if a[i]>besar:
            besar = a[i]
        elif a[i] < kecil :
            kecil = a[i]
            
a.insert(len(a), besar)
print (a)
a.insert(0, kecil)
print (a)

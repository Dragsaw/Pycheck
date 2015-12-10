from libs.perceptron.Pyceptron import *
import random

p = Pyceptron(addressables_count=100)

for i in range(0, 600):
    c = random.randint(0, 2)
    p.learn("E:/\Downloads/\image/\/0%s.bmp" % c, "0")
    p.learn("E:/\Downloads/\image/\/1%s.bmp" % c, "1")
    p.learn("E:/\Downloads/\image/\/2%s.bmp" % c, "2")
    p.learn("E:/\Downloads/\image/\/3%s.bmp" % c, "3")
    p.learn("E:/\Downloads/\image/\/4%s.bmp" % c, "4")
    p.learn("E:/\Downloads/\image/\/5%s.bmp" % c, "5")
    p.learn("E:/\Downloads/\image/\/6%s.bmp" % c, "6")
    p.learn("E:/\Downloads/\image/\/7%s.bmp" % c, "7")
    p.learn("E:/\Downloads/\image/\/8%s.bmp" % c, "8")
    p.learn("E:/\Downloads/\image/\/9%s.bmp" % c, "9")

print("*** 0 ***")
for i in range(0, 3):
    print(p.resolve_path("E:/\Downloads/\image/\/0%s.bmp" % i))
    
print("*** 1 ***")
for i in range(0, 3):
    print(p.resolve_path("E:/\Downloads/\image/\/1%s.bmp" % i))

print("*** 2 ***")
for i in range(0, 3):
    print(p.resolve_path("E:/\Downloads/\image/\/2%s.bmp" % i))

print("*** 3 ***")
for i in range(0, 3):
    print(p.resolve_path("E:/\Downloads/\image/\/3%s.bmp" % i))

print("*** 4 ***")
for i in range(0, 3):
    print(p.resolve_path("E:/\Downloads/\image/\/4%s.bmp" % i))

print("*** 5 ***")
for i in range(0, 3):
    print(p.resolve_path("E:/\Downloads/\image/\/5%s.bmp" % i))

print("*** 6 ***")
for i in range(0, 3):
    print(p.resolve_path("E:/\Downloads/\image/\/6%s.bmp" % i))
    
print("*** 7 ***")
for i in range(0, 3):
    print(p.resolve_path("E:/\Downloads/\image/\/7%s.bmp" % i))

print("*** 8 ***")
for i in range(0, 3):
    print(p.resolve_path("E:/\Downloads/\image/\/8%s.bmp" % i))

print("*** 9 ***")
for i in range(0, 3):
    print(p.resolve_path("E:/\Downloads/\image/\/9%s.bmp" % i))

save(p, 'E:\\p5')

'''ranges = [ 100, 500, 700, 1000, 2000, 3000]
addressables = [ 30, 35, 55, 60, 65, 90]
for ar in addressables:
    for r in ranges:
        overall = 0
        for i in range(0, 10):
            p = Pyceptron(addressables_count=ar)
            for k in range(0, r):
                c = random.randint(1, 9)
                p.learn("E:/\Downloads/\image/\/A0%s.bmp" % c, "A")
                p.learn("E:/\Downloads/\image/\/B0%s.bmp" % c, "B")
                p.learn("E:/\Downloads/\image/\/C0%s.bmp" % c, "C")
            a = 0
            b = 0
            c = 0
            for i in range(1, 10):
                if p.resolve_path("E:/\Downloads/\image/\/A0%s.bmp" % i) == "A":
                    a+=1
            for i in range(1, 10):
                if p.resolve_path("E:/\Downloads/\image/\/B0%s.bmp" % i) == "B":
                    b+=1
            for i in range(1, 10):
                if p.resolve_path("E:/\Downloads/\image/\/C0%s.bmp" % i) == "C":
                    c+=1
            overall += (a + b + c) / 27
        final = (overall * 100) / 10
        print("{0} {1}: {2}%".format(ar, r, final))'''
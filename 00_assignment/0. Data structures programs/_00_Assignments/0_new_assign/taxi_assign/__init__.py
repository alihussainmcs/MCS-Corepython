
num=int(input("Enter a number:"))
for i in range(1,num+1):
    print(" "*(num-i),end="")
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()
for p in range(1,num):
    print(" "*p,end="")
    for q in range(1,num+1-p):
        print(chr(64+q+p),end=" ")
    print()
"""A
A B
A B C
A B C D
A B C D E
B C D E
C D E
D E
E"""
"""Pattern-82:
1) n=int(input("Enter a number:"))
2) for i in range(1,n+1):
3) print(" "*(n-i),end="")
4) for j in range(1,i+1):
5) print(n-i+j,end=" ")
6) for k in range(2,i+1):
7) print(n+1-k,end=" ")
8) print()
9) for i in range(1,n+1):
10) print(" "*i,end="")
11) for j in range(1+i,n+1):
12) print(j,end=" ")
13) for k in range(2,n+1-i):
14) print(n+1-k,end=" ")
15) print()
5
4 5 4
3 4 5 4 3
2 3 4 5 4 3 2
1 2 3 4 5 4 3 2 1
2 3 4 5 4 3 2
3 4 5 4 3
4 5 4"""
# for i in range(1, 5):
#     for j in range(1, 2):
#         print(f"i={i}, j={j}")

# for i in range(1, 4):
#     for j in range(1, i+1):
#         if (j==i): 
#             print("*", end='')
#         else: 
#             print(" ", end='')
#     print("")

# for i in range(4, 1, -1):
#     for j in range(i, 1, -1):
#         print("*", end = '')
#     print("")

# x = int(input("Enter the number between 2 to 9: 8"))
# for i in range(1, x):
#     for j in range(1, i+1):
#         print("x", end = '')
#     print("")

# for i in range(20):
#     if i%2 == 0:
#         continue
#     print(i)

# for i in range(8):
#     if i == 4:
#         continue
#     if i == 5:
#         break
#     print(i)

# int: r 
# r =8

# for k in range (10,0,-2):
#     if (k == 4):
#         print (k)
#     if ( k == r):
#         print (r)

j = int(input("Enter the number: "))
x = 0
y = 1
z = x+y
while(z <= j): 
    print(z)
    x = y
    y = z
    z = x + y





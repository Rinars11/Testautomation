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

x = int(input("Enter the number between 2 to 9: "))
for i in range(1, x):
    for j in range(1, i+1):
        print("x", end = '')
    print("")
    

vals = []
n = int(input("Enter the range "))
for i in range(n):
    x = int(input("Enter the no. "))
    vals.append(x)
    
search = int(input("Enter the no. to be searched "))
for i in vals:
    if(search == i):
        print("No. found at ",vals.index(i))
else:
    print("No. not found ")

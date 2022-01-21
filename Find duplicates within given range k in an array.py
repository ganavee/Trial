'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

a = [5,6,8,2,4,6,9]
k = 2
length = len(a)
count = 0
if(length < k):
    k = length - 1
for i in range(0,length):
    for j in range(i+1,i+k+1):
        if(((j)<length) and (a[i] == a[j])):
            print(a[j],"found at distance",(j-i))
            count += 1
        
if(count ==0):
    print("No duplicates found")
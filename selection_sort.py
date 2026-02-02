a=int(input("Enter total number of inputs"))
b=[]

for i in range(a):
    num=int(input("Enter the number"))
    b.append(num)
print("Entered number is",b)
    
    
def selection_sort():
    for i in range(a-1):
        min_index=i
        for j in range(i+1,a):
            if (b[j]<b[min_index]):
                min_index=j
                
        b[i],b[min_index]=b[min_index],b[i]
        print("current sorted array is", b)
        

    print("Sorted array is", b)
    
selection_sort()    
    


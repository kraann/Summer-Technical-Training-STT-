def display(n):
    
    if n<=0:
        
        return
    
    print(n,end=" ")
    
    display(n-1)

display(5)
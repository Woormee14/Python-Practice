try:
    l=[1,2,5,6]
    i=int(input("Enter the index:"))
    print(l[i])
except:
    print("Some error occured")
finally:
    print("I am always executed")

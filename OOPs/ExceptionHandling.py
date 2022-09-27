
arr = [1,2,3,4,5]
try:
    a = int (input())
    print(arr[2])
except Exception as e:
    print(e)

finally:
    print("Printing")

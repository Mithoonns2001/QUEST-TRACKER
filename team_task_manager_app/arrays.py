
# Write a function that will return the second largest value in an array
# Example secondLargest([1,25,200,3,7]) will return 25

def secondLargest(arr):
    num1 = arr[0]
    num2 = arr[1]
    for i in arr:
        if num1 < i:
            num2 = num1
            num1 = i
    print(num2)                                 


secondLargest([1,25,200,3,7])



# create a function
def search(list, guess, length):
    start = 0
    end = length-1
    while(start<=end):
        mid = (start + end) // 2
        if guess==list[mid]:
            print("element found at:",mid+1)
            break
        elif guess< list[mid]:
            end = mid -1
        elif guess>list[mid]:
            start= mid + 1
    else:
            print("value is not found")


    return -1

# create a list and get a number from the user
list = [2, 3, 4, 5, 6, 8]
guess = int(input("enter your guess:"))
length = len(list)


#functioncall
result = search(list, guess, length)


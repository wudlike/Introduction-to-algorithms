def binary_search(list_input,item):
    low = 0
    high = len(list_input) - 1
    while low<=high:
        mid = (low+high)//2
        if list_input[mid] == item:
            return mid
        elif list_input[mid] < item:
            low = mid + 1
        else:
            high = mid -1
    return None

# test
if __name__ == '__main__':
    list_test = [1,2,4,8]
    item = 8
    print(binary_search(list_test,item))


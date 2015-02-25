# Insertion sort implementation in Python
def sorting_method(nums_list):
    for j in range(1, len(nums_list)):
        key = nums_list[j]
        i = j-1
        while i>=0 and nums_list[i] > key:
            nums_list[i+1] = nums_list[i]
            i-=1
        nums_list[i+1] = key
    return nums_list

def main():
    nums = [5,2,3,6,1,7,8,9,4]
    sorting_method(nums)
    print nums

if __name__ == "__main__":
    main()

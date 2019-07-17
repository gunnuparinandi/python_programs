# JUNE 29, 2019
# DAILY CODING PROBLEM 102
# DESCRIPTION:
# This problem was asked by Lyft..
# Given a list of integers and a number K, return which contiguous
# elements of the list sum to K.
# For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return
# [2, 3, 4], since 2 + 3 + 4 = 9.

# method to find contiguous sum. Method has O(n^2) runtime.
def contiguous_sum(k, list_nums):
    index = 0
    for i in  list_nums:
        sum_elements = 0
        for j in list_nums[index:]:
            sum_elements = sum_elements + list_nums[j]

            if k == sum_elements:
                return (list_nums[i:j + 1])
        index += 1


if __name__ == "__main__":
    #enter array:
    list_numbers = [1, 2, 3, 4, 5]
    #enter total sum:
    k = 9
    print(contiguous_sum(k, list_numbers))

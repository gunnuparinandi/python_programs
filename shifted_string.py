# JUNE 29, 2019
# DAILY CODING PROBLEM 108
# DESCRIPTION:
# This problem was asked by Google.
# Given two strings A and B, return whether or not A can be shifted some number of times to get B.
# For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.


# BRUTE FORCE METHOD
# method below collects and returns all "clockwise" shifted strings.
# see below for explicit example.

def shifted_string(string):
    permuted_string_list = []
    for index in range(len(string)):
        permuted_string_list.append(string[index:len(string)] + string[0:index])
    #   print(permuted_string_list)
    return permuted_string_list


# This method checks to see if a given string is shifted sequence of the previous string.

def is_shifted(permuted_string_list, string):
    for word in range(len(permuted_string_list)):
        if permuted_string_list[word] == string:
            return True
    return False


if __name__ == "__main__":
    # type original string here:
    orignal_string = 'abcde'

    # type new string here:
    new_string = 'bcdea'

    shifted_string(new_string)
    print(is_shifted(shifted_string(orignal_string), new_string))

# THOUGHT PROCESS:
# abcde ~ string[0:5] + string[0:0]
# bcdea ~ string[1:5] + string[0:1]
# cdeab ~ string[2:5] + string[0:2]
# deabc ~ string[3:5] + string[0:3]
# eadbc ~ string[4:5] + string[0:4]
#
#

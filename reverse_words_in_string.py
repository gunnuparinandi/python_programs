# JULY 3, 2019
# DAILY CODING PROBLEM 113
# DESCRIPTION:
# This problem was asked by Google.
# Given a string of words delimited by spaces, reverse the words in
# string. For example, given "hello world here", return "here world hello"
#
# Follow-up: given a mutable string representation, can you perform this operation in-place?

# Immutable way to reverse the words in a string.
# This method takes O(n) time.
def reverse_words_in_string_immutable(string):
    new_string = string.split(' ')
    return ' '.join(list(reversed(new_string)))


print(reverse_words_in_string_immutable('hello world here'))

# I need to work on the mutable case. But the logic is similar to if we rotated each char of each word,
# and the rotated the list.

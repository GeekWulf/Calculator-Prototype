def remove_ith_character(s, i):
	# Base case: if index is 0,
	# return string with first character removed
	if i == 0:
		return s[1:]

	# Recursive case: return first character
	# concatenated with result of calling function
	# on string with index decremented by 1
	return s[0] + remove_ith_character(s[1:], i - 1)


# Test the function
test_str = "Bjajfkfkasjfdk"
new_str = remove_ith_character(test_str, 0)
print("The string after removal of ith character:", new_str)
# This code is contributed by Edula Vinay Kumar Reddy

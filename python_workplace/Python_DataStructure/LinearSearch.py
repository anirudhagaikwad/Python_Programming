#program for linear search
def search(arr, search_Element):
	left = 0
	length = len(arr)
	position = -1
	right = length - 1

	# Run loop from 0 to right
	for left in range(0, right, 1):

		# If search_element is found with
		# left variable
		if (arr[left] == search_Element):
			position = left
			print("Element found in Array at ", position +
				1, " Position with ", left + 1, " Attempt")
			break

		# If search_element is found with
		# right variable
		if (arr[right] == search_Element):
			position = right
			print("Element found in Array at ", position + 1,
				" Position with ", length - right, " Attempt")
			break
		left += 1
		right -= 1

	# If element not found
	if (position == -1):
		print("Not found in Array with ", left, " Attempt")

# Driver code
arr = [1, 2, 3, 4, 5]
search_element = 5

# Function call
search(arr, search_element)


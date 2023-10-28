def is_prefix_exist(root, key): 
	# Initialize the currentNode pointer 
	# with the root node 
	current_node = root 

	# Iterate across the length of the string 
	for c in key: 
		# Check if the node exist for the current 
		# character in the Trie. 
		if current_node.child_node[ord(c) - ord('a')] is None: 
			# Given word as a prefix does not exist in Trie 
			return False

		# Move the currentNode pointer to the already 
		# existing node for current character. 
		current_node = current_node.child_node[ord(c) - ord('a')] 

	# Prefix exist in the Trie 
	return True

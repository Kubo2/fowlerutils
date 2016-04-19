"""
Provides a function to get unique list of values from two dictionaries.

Author:  Kubis Fowler
Version: 0.1
"""

def uniquedict(dict1, dict2):
	"""
	Takes dict1 and dict2 and returns a new asc sorted distinct list from their values.
	"""

	which = len(dict1) > len(dict2)
	primary = which and dict2 or dict1
	secondary = which and dict1 or dict2

	distinct = [val for val in primary if val not in secondary] + [val for val in secondary]
	distinct.sort()

	return distinct

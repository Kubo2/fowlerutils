"""
Handy and unique utility functions for instant use.

Author:  Kubis Fowler
Version: 0.2
"""

def uniquedict(dict1, dict2):
	"Takes dict1 and dict2 and returns a new distinct asc-sorted list of their values."

	def conv(arb):
		if type(arb) is dict:
			return arb.values()
		elif type(arb) is set:
			return list(arb)
		else:
			raise TypeError('arguments must be dict or set')

	dict1, dict2 = conv(dict1), conv(dict2)

	distinct = list(set(dict1 + dict2))
	distinct.sort()

	return distinct


import unittest

import sys
sys.path.insert(0, '../fowlerutils')

import uniquedict

class uniquedictTestCase(unittest.TestCase):
	"""
	Test case for function fowlerutils.uniquedict()
	"""

	def testFirstLonger(self):
		"Test whether uniquedict.uniquedict() performs length normalization properly"
		self.assertEqual(
			uniquedict.uniquedict({5, 6, 7, 8, 1, 2, 3, 4}, {1, 2, 3, 4}),
			[1, 2, 3, 4, 5, 6, 7, 8]
		)

	def testLastLonger(self):
		"Test second argument a longer dict than the first"
		self.assertEqual(
			uniquedict.uniquedict({1, 2, 3, 4}, {5, 6, 7, 8, 1, 2, 3, 4}),
			[1, 2, 3, 4, 5, 6, 7, 8]
		)

	def testEmptyDict(self):
		"Test empty dict arguments case"
		self.assertEqual(uniquedict.uniquedict({}, {1, 2, 3}), [1, 2, 3])
		self.assertEqual(uniquedict.uniquedict({1, 2, 3}, {}), [1, 2, 3])

	def testSorting(self):
		"Test the sorting feature of uniquedict.uniquedict()"
		self.assertEqual(uniquedict.uniquedict({2, 3, 1}, {4, 6, 5}), [1, 2, 3, 4, 5, 6])

	def testDuplicates(self):
		"Test the behavior if there is more than one same value in one of the dicts"
		self.assertEqual(uniquedict.uniquedict({1, 2, 3, 3, 4, 5, 4, 4, 5, 6}, {1, 2, 3}), [1, 2, 3, 4, 5, 6])

	def testKeys(self):
		"Test the behavior when passing associative arrays (dicts with keys) to the function"
		self.assertEqual(uniquedict.uniquedict({'a':1, 'b':2, 'c':3}, {'foo':4, 'bar':8, 'php':7, 'vek':2, 'ja':1, 'ty':3}), [1,2,3,4,7,8])

	def testErrorCases(self):
		self.assertRaises(TypeError, lambda: uniquedict.uniquedict(123, {}))


if __name__ == '__main__':
	unittest.main()

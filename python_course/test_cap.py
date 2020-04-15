import unittest
import cap


class TestCap(unittest.TestCase):
	"""General structure of a TEST!!!"""
	def test_one_word(self):
		text = 'python'
		result = cap.cap_text(text)
		self.assertEqual(result, 'Python')

	def test_multiple_words(self):
		text = 'monthy python'
		result = cap.cap_text(text)
		self.assertEqual(result, 'Monthy Python')

	def test_with_apostrophes(self):
		text = "monthy python's flying circus"
		result = cap.cap_text(text)
		self.assertEqual(result, "Monthy Python's Flying Circus")


if __name__ == '__main__':
	unittest.main()

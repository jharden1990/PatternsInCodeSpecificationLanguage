import unittest
import ast
import sys
import os




sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pedal import contextualize_report
from pedal.cait.cait_api import *
from pedal.core.report import MAIN_REPORT
from pedal.source import set_source, verify
from pedal.tifa import tifa_analysis
from new_patterns_2020_08_14 import *


class MistakeTest(unittest.TestCase):
	SUBMISSION_STRING = ''

	@staticmethod
	def to_source(source):
		MAIN_REPORT.clear()
		contextualize_report(source)
		verify()
		parse_program()
		tifa_analysis()

	def setUp(self):
		self.to_source(self.SUBMISSION_STRING)

	def test_wrong_conversion_placement_1(self, ):
		self.assertFalse(wrong_conversion_placement_1(), 'The input is always a string and must be converted to a number before being used in an arithmetic calculation.')

	def test_wrong_conversion_placement_2(self, ):
		self.assertFalse(wrong_conversion_placement_2(), 'The input is always a string and must be converted to a number before being used in an arithmetic calculation.')

	def test_wrong_conversion_placement_3(self, ):
		self.assertFalse(wrong_conversion_placement_3(), 'The conversion should be applied to result of the input operation.')

	def test_wrong_conversion_type(self, ):
		self.assertFalse(wrong_conversion_type(), 'The input is a number with a decimal point. The conversion should reflect this type of number.')

	def test_missing_float_conversion(self, ):
		self.assertFalse(missing_float_conversion(), 'The input is always a string and must be converted to a number with decimals.')

	

if __name__ == "__main__":
	if len(sys.argv) > 1:
		potential_file = sys.argv.pop()
		if os.path.isfile(potential_file):
			with open(potential_file, 'r') as read_file:
				MistakeTest.SUBMISSION_STRING = read_file.read()
	unittest.main()
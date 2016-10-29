#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_hallie
----------------------------------

Tests for `hallie` module.
"""

import unittest

from hallie import hallie
import sys
from StringIO import StringIO


class TestHallie(unittest.TestCase):

	def testEmptyCommand(self):
		out = StringIO()
		sys.stdout = out
		hallie.main()
		output = out.getvalue().strip()
		assert "I'm sorry, I don't understand that command" in output

	def testBadCommand(self):
		out = StringIO()
		sys.stdout = out
		hallie.parse("asdfjlasdhfjlasjdf")
		output = out.getvalue().strip()
		assert "I'm sorry, I don't understand that command" in output

	def testGoodCommand(self):
		out = StringIO()
		sys.stdout = out
		hallie.parse("show me the current files")
		output = out.getvalue().strip()
		assert "I'm sorry, I don't understand that command" not in output

if __name__ == '__main__':
    unittest.main()

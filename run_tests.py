#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Unit tests
# Copyright (c) 2013 Vikas Panwar <vicky.panwar@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import unittest
from WikiLookup import WikiLookup
from Calculator import Calculator
from Temperature import Temperature
from DictionaryEng import DictionaryEng
from DictionaryEng2Ch import DictionaryEng2Ch
from DictionaryEng2Hi import DictionaryEng2Hi

class WikiLookupTestCase(unittest.TestCase):
    def runTest(self):
        wiki = WikiLookup()
        res = wiki.lookup("solar eclipse")
        self.assertTrue(len(res) > 100)
        self.assertFalse("Sorry, I don't know!" in res)

class CalculatorTestCase(unittest.TestCase):
    def runTest(self):
        calc = Calculator()
        self.assertEqual(calc.calc("6+9"), 15, 'wrong simple addition')
        self.assertEqual(calc.calc("6*9"), 54, 'wrong simple multiplication')
        self.assertEqual(calc.calc("(6*9)/2"), 27, 'wrong simple division')
        self.assertEqual(calc.calc("(6*9)/2 - 10"), 17)

class TemperatureTestCase(unittest.TestCase):
    def runTest(self):
        temp = Temperature()
        res = temp.convert("32")
        answer = (str(0.0) in res) and (str(89.6) in res)
        self.assertTrue(answer)

        res = temp.convert("-12")
        answer = (str(10.4) in res) and (str(-24.44) in res)
        self.assertTrue(answer)

        res = temp.convert("-500")
        answer = (str(-868.0) in res) and (str(-295.56) in res) and ("impossible" in res)
        self.assertTrue(answer)

class DictionaryTestCase(unittest.TestCase):
    def runTest(self):
        dict = DictionaryEng()
        res = dict.lookup("eclipse")
        self.assertTrue(len(res) > 100)
        self.assertFalse("No results found!" in res)

        res = dict.lookup("asdafsgdf")
        self.assertTrue("No results found!" in res)


class ChineseTestCase(unittest.TestCase):
    def runTest(self):
        dict = DictionaryEng2Ch()
        res = dict.lookup("eclipse")
        self.assertFalse("No results found!" in res)

        res = dict.lookup("asdafsgdf")
        self.assertTrue("No results found!" in res)


class HindiTestCase(unittest.TestCase):
    def runTest(self):
        dict = DictionaryEng2Hi()
        res = dict.lookup("eclipse")
        self.assertFalse("No results found!" in res)

        res = dict.lookup("asdafsgdf")
        self.assertTrue("No results found!" in res)

if __name__ == '__main__':
    unittest.main()

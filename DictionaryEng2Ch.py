#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# An english to chinese translator implmented using web scraping
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
from bs4 import BeautifulSoup
import urllib2
import html5lib
from Dictionary import Dictionary

class DictionaryEng2Ch(Dictionary):
	def lookup(this, word):
		url = "http://tw.dictionary.search.yahoo.com/search?p="		
		page = urllib2.urlopen(url + word + "&fr2=dict")
		soup = BeautifulSoup(page.read(), 'html5lib')
		results = soup.find_all("p", class_="explanation")

		return this.answer(results)

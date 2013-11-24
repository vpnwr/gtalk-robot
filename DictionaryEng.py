#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# An english dictionary lookup implmented using web scraping
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

class DictionaryEng(Dictionary):
	def lookup(this, word):
		url = "http://www.thefreedictionary.com/"
		page = urllib2.urlopen(url + word)
		soup = BeautifulSoup(page.read(), 'html5lib')
		results = soup.find_all("div", class_="ds-list")

		return this.answer(results)

#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# An english to hindi translator implmented using web scraping
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

class DictionaryEng2Hi(Dictionary):
	def lookup(this, word):
		url = "http://www.shabdkosh.com/hi/translate?e="		
		page = urllib2.urlopen(url + word + "&l=hi")
		soup = BeautifulSoup(page.read(), 'html5lib', from_encoding='utf-8')
		results = soup.find_all("a", class_="in l")
		
	        if len(results) >= 3:
                    answer = results[0].text.encode('utf-8') + "\n" + results[1].text.encode('utf-8') + "\n" + results[2].text.encode('utf-8')
                elif len(results) == 2:
                    answer = results[0].text.encode('utf-8') + "\n" + results[1].text.encode('utf-8') + "\n"
                elif len(results) ==1:
                    answer = results[0].text.encode('utf-8')
                else:
                    answer = "No results found!"

                return answer

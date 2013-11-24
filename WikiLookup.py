#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Wikipedia web scraping
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

skipwords = ["a", "an", "the", "called", "as", "on", "known"]
class WikiLookup(Dictionary):
	def lookup(this, words):
                what = ""
                
                tokens = words.split(" ")
                for word in tokens:
                        word = word.lower()
                        
                        if word not in skipwords:
                                if len(word) > 0:
                                    word = word[0].upper() + word[1:]
                                what = what + "_" + word

                url = "http://en.wikipedia.org/wiki/"
                req = urllib2.Request (url+what)
                req.add_header('User-Agent', 'Event Horizon')

                try:
                        page = urllib2.urlopen(req)
                        soup = BeautifulSoup(page.read(), 'html5lib')

                        results = soup.find_all("p")
                except:
                        return "Sorry, I don't know!"

                if len(results) > 0:
                        if "may refer to" in results[0].text:
                                results = soup.find_all("li")
                                
                #return results[0].text
		return this.answer(results)

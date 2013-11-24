#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# A Dictionary lookup base class
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

class Dictionary:
    def answer(this, results):
        if len(results) >= 3:
            answer = results[0].text + "\n" + results[1].text + "\n" + results[2].text
	elif len(results) == 2:
            answer = results[0].text + "\n" + results[1].text + "\n"
	elif len(results) ==1:
            answer = results[0].text
	else:
            answer = "No results found!"

        return answer

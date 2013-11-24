#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Temperature conversion between celcius and fahrenheit
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

class Temperature():
	def convert(this, temp):
                try:
                        t = int(temp)
                        fahrenheit = round( ((t * 9.0) / 5.0) + 32, 2)
                        celsius = round( ((t - 32) / 9.0) * 5.0, 2)

                        result = temp + " C = " + str(fahrenheit) + " F\n"
                        result += temp + " F = " + str(celsius) + " C"
                        if celsius < -273.15 or t < -273.15:
                                result += "\nNote that " + str(t) + " C is below absolute zero and thermodynamically impossible."
                except:
                        return "usage example: temp 23"
                
		return result

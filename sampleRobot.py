#!/usr/bin/python
# -*- coding: utf-8 -*-

# PyGtalkRobot: A simple jabber/xmpp bot framework using Regular Expression Pattern as command controller
# Copyright (c) 2013 Vikas Panwar <vicky.panwar@gmail.com>
# Original contribution by Demiao Lin <ldmiao@gmail.com>
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
# Homepage: http://code.google.com/p/pygtalkrobot/
#

#
# This is an sample PyGtalkRobot that serves to set the show type and status text of robot by receiving message commands.
#

import sys
import time
import random

from PyGtalkRobot import GtalkRobot
from DictionaryEng import DictionaryEng
from DictionaryEng2Ch import DictionaryEng2Ch
from DictionaryEng2Hi import DictionaryEng2Hi
from Calculator import Calculator
from WikiLookup import WikiLookup
from Temperature import Temperature

############################################################################################################################

class SampleBot(GtalkRobot):
    
    #Regular Expression Pattern Tips:
    # I or IGNORECASE <=> (?i)      case insensitive matching
    # L or LOCALE <=> (?L)          make \w, \W, \b, \B dependent on the current locale
    # M or MULTILINE <=> (?m)       matches every new line and not only start/end of the whole string
    # S or DOTALL <=> (?s)          '.' matches ALL chars, including newline
    # U or UNICODE <=> (?u)         Make \w, \W, \b, and \B dependent on the Unicode character properties database.
    # X or VERBOSE <=> (?x)         Ignores whitespace outside character sets
    
    #"command_" is the command prefix, "001" is the priviledge num, "setState" is the method name.
    #This method is used to change the state and status text of the bot.
    def command_001_setState(self, user, message, args):
        #the __doc__ of the function is the Regular Expression of this command, if matched, this command method will be called. 
        #The parameter "args" is a list, which will hold the matched string in parenthesis of Regular Expression.
        '''(available|online|on|busy|dnd|away|idle|out|off|xa)( +(.*))?$(?i)'''
        show = args[0]
        status = args[1]
        jid = user.getStripped()

        # Verify if the user is the Administrator of this bot
        if jid == 'vicky.panwar@gmail.com':
            print jid, " ---> ",bot.getResources(jid), bot.getShow(jid), bot.getStatus(jid)
            self.setState(show, status)
            self.replyMessage(user, "State settings changed！")

    #This method is used to send email for users.
    def command_002_SendEmail(self, user, message, args):
        #email ldmiao@gmail.com hello dmeiao, nice to meet you, bla bla ...
        #'''(email|mail|em|m)\s+(.*?@.+?)\s+(.*?),\s*(.*?)(?i)'''
        '''(email|mail|em|m)'''
        email_addr = args[0]
        #subject = args[1]
        #body = args[2]
        #call_send_email_function(email_addr, subject,  body)
        
        self.replyMessage(user, "\nEmail sent to "+ email_addr +" at: "+time.strftime("%Y-%m-%d %a %H:%M:%S", time.localtime()))


    def command_009_default(self, user, message, args):
        '''(what)(.*)(you)(.*)(name)(.*)(?i)'''
        self.replyMessage(user, "my name is Event Horizon")

    def command_100_default(self, user, message, args):
        '''(dict)\s+(.*)'''
        print args[1]
        d = DictionaryEng()
        self.replyMessage(user, d.lookup(args[1]))

    def command_101_default(self, user, message, args):
        '''(ch)\s+(.*)'''
        print args[1]
        d = DictionaryEng2Ch()
        self.replyMessage(user, d.lookup(args[1]))

    def command_102_default(self, user, message, args):
        '''(hin)\s+(.*)'''
        print args[1]
        d = DictionaryEng2Hi()
        self.replyMessage(user, d.lookup(args[1]))

    def command_103_default(self, user, message, args):
        '''(calc)\s+(.*)'''
        print args[1]
        calc = Calculator()
        self.replyMessage(user, calc.calc(args[1]))

    def command_104_default(self, user, message, args):
        '''(temp)\s+(-\d*|\d*)'''
        print args[1]
        temp = Temperature()
        self.replyMessage(user, temp.convert(args[1]))
        
    def command_105_default(self, user, message, args):
        '''(what|who)\s+(is|are)\s+(.*)'''
        print args[2]
        wiki = WikiLookup()
        self.replyMessage(user, wiki.lookup(args[2]))

    def command_400_default(self, user, message, args):
        '''(help|\?|madad|helpme)'''
        print "help"
        self.replyMessage(user, """I understand the following commands -
*dict <word> - dictionary lookup
*ch <word> - english to chinese
*hin <word> - english to hindi
*calc <expr> - simple calculator. e.g. calc (34*5)+3
*temp t - convert between C/F
*what is <something>
*who is <someone>""")

    # commands 5xx model the 'intelligent' behaviour
    def command_500_default(self, user, message, args):
        '''(how)(.*)(you)(?i)'''
        print "how are you"
        self.replyMessage(user, "I am doing fine, thanks")

    def command_502_default(self, user, message, args):
        '''(hi|hello|ni hao|namaste|namaskar|hola|nihao).*(?i)'''
        print "hi"
        self.replyMessage(user, "Hello " + user.getStripped())

    def command_503_default(self, user, message, args):
        '''(.*)(love)(.*)(you)(?i)'''
        self.replyMessage(user, "That's sweet!")

    def command_504_default(self, user, message, args):
        '''(.*)(good)(.*)(night)(?i)'''
        self.replyMessage(user, "good night")

    def command_505_default(self, user, message, args):
        '''(.*)(good)(.*)(morn)(?i)'''
        self.replyMessage(user, "a very good morning to you")

    def command_506_default(self, user, message, args):
        '''(.*)(good)(.*)(afterno)(?i)'''
        self.replyMessage(user, "good afternoon :-)")

    def command_507_default(self, user, message, args):
        '''(.*)(bbye|bye|tata|chao|ttyl|later|sayonara)(.*)(?i)'''
        responses = ["Bye now", "Tata", "Sayonara", "Bye", "See you later", "chao"]

        index = random.randint(0,5)
        self.replyMessage(user, responses[index])

    def command_508_default(self, user, message, args):
        '''(thank)(.*)(?i)'''
        responses = ["you are welcome", "no problem", "my pleasure", "you are welcome", "np", "sure"]

        index = random.randint(0,5)
        self.replyMessage(user, responses[index])
        
    #This method is used to response users.
    def command_990_default(self, user, message, args):
        '''.*?(?s)(?m)'''
        self.replyMessage(user, time.strftime("%Y-%m-%d %a %H:%M:%S", time.localtime()))

    def command_900_default(self, user, message, args):
        '''.*?(?s)(?m)'''
        responses = ["Sorry, I didn't understand that", "No clue", "I have no idea about that", "Don't know about that", "I didn't get that"]

        index = random.randint(0,4)
        self.replyMessage(user, responses[index])

        if index == 1:
            self.replyMessage(user, "try tyipng 'help'")

############################################################################################################################
if __name__ == "__main__":
    bot = SampleBot()
    bot.setState('available', "type help to see what I can do")
    bot.start("username@gmail.com", "password")

#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# A Calculator Implemented With A Top-Down, Recursive-Descent Parser
# Copyright (c) 2013 Vikas Panwar <vicky.panwar@gmail.com>
# Credits for original source: Erez Shinan, Dec 2012
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

import re, collections
from operator import add,sub,mul,div



class Calculator:
    def __init__(self):
        self.token_map = {'+':'ADD', '-':'ADD', '*':'MUL', '/':'MUL', '(':'LPAR', ')':'RPAR'}
        self.Token = collections.namedtuple('Token', ['name', 'value'])
        self.RuleMatch = collections.namedtuple('RuleMatch', ['name', 'matched'])
        self.rule_map = {
                'add' : ['mul ADD add', 'mul'],
                'mul' : ['atom MUL mul', 'atom'],
                'atom': ['NUM', 'LPAR add RPAR', 'neg'],
                'neg' : ['ADD atom'],
            }
        self.calc_map = {
                'NUM' : float,
                'atom': lambda x: x[len(x)!=1],
                'neg' : lambda (op,num): (num,-num)[op=='-'],
                'mul' : self.calc_binary,
                'add' : self.calc_binary,
            }
        self.fix_assoc_rules = 'add', 'mul'
        self.bin_calc_map = {'*':mul, '/':div, '+':add, '-':sub}
        
    def calc_binary(this,x):
        while len(x) > 1:
            x[:3] = [ this.bin_calc_map[x[1]](x[0], x[2]) ]
        return x[0]
    
    def match(this, rule_name, tokens):
        if tokens and rule_name == tokens[0].name:      # Match a token?
            return tokens[0], tokens[1:]
        for expansion in this.rule_map.get(rule_name, ()):   # Match a rule?
            remaining_tokens = tokens
            matched_subrules = []
            for subrule in expansion.split():
                matched, remaining_tokens = this.match(subrule, remaining_tokens)
                if not matched:
                    break   # no such luck. next expansion!
                matched_subrules.append(matched)
            else:
                return this.RuleMatch(rule_name, matched_subrules), remaining_tokens
        return None, None   # match not found
    def _recurse_tree(this, tree, func):
        return map(func, tree.matched) if tree.name in this.rule_map else tree[1]
    def flatten_right_associativity(this, tree):
        new = this._recurse_tree(tree, this.flatten_right_associativity)
        if tree.name in this.fix_assoc_rules and len(new)==3 and new[2].name==tree.name:
            new[-1:] = new[-1].matched
        return this.RuleMatch(tree.name, new)
    def evaluate(this, tree):
        solutions = this._recurse_tree(tree, this.evaluate)
        return this.calc_map.get(tree.name, lambda x:x)(solutions)
    def calc(this, expr):
        split_expr = re.findall('[\d.]+|[%s]' % ''.join(this.token_map), expr)
        tokens = [this.Token(this.token_map.get(x, 'NUM'), x) for x in split_expr]
        tree = this.match('add', tokens)[0]
        tree = this.flatten_right_associativity( tree )
        return this.evaluate(tree)

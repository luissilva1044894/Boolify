#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from boolify import boolify

print(boolify([ '1', 'active', 'ok']))#list

print(boolify(( 'enabled', 'off', 'oks' )))#tuple

print(boolify({ 'ok', 't', 'true' }))#set

print(boolify({ '1': 'n', '2': 'off', '3': 'no'}))#dict

print(boolify([ 'n', 'true', object()], non_str=False))

test_cases = [ 'f', 'false', 'n', 'no', 'on', 't', 'true', 'y', 'yes', '0', '1', '', -1, 0, 0.0, 1, 1.0, 123, [], {}, (), [1], {1:2}, (1,), True, False, None, object() ]
print([[x, boolify(x)] for x in test_cases])

_str = 'oks'
print(boolify(_str))

print(boolify(_str, custom_values=( '1', 'oks', 'on', 't', 'true', 'up', 'y', 'yes' )))

print(boolify(_str, raise_exc=True))

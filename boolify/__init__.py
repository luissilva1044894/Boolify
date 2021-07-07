#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

TRUE = (
  '1',
  'able',
  'active',
  'allow',
  'allowed',
  'enabled',
  'in',
  'ok',
  'on',
  'running',
  't',
  'true',
  'up',
  'y',
  'yes',
)
FALSE = (
  '0',
  'disabled',
  'disallowed',
  'down',
  'f',
  'false',
  'off',
  'n',
  'no',
  'stopped',
  'out',
)
try:
  string_types = basestring
except NameError:
  try:
    from six import string_types
  except ImportError:
    string_types = str

try:
  from distutils.util import strtobool
except ImportError:
  strtobool = None

_str = lambda raw: isinstance(raw, string_types)

def _boolify(raw, custom_values=None, *, non_str=True, raise_exc=False, **kw):
  if isinstance(raw, bool):
    return raw
  if not non_str and not _str(raw):
    return bool(raw)
  if isinstance(raw, float):
    #int(raw)
    return _boolify(round(raw), custom_values=custom_values, non_str=non_str, raise_exc=raise_exc, **kw)
  raw = str(raw).strip().lower().lower()
  if raw in FALSE and raw in TRUE or custom_values is not None and raw in custom_values:
    try:
      return bool(strtobool(raw))
    except (AttributeError, NameError, TypeError, ValueError):
      pass
  if raise_exc and raw not in (custom_values or TRUE) and raw not in FALSE:
    raise ValueError('Invalid value %r. Expected values are : \'%s\'' % (raw, '\', \''.join((custom_values or TRUE))))
  return raw in (custom_values or TRUE)

def boolify(raw=None, custom_values=None, *, non_str=True, raise_exc=False, **kw):
  if isinstance(raw, (list, dict, tuple, set)) and len(raw) > 0:
    if hasattr(raw, 'iteritems') or hasattr(raw, 'items'):
      return {k: _boolify(raw=_, custom_values=custom_values, non_str=non_str, raise_exc=raise_exc) for k,_ in (raw.items() if hasattr(raw, 'items') else raw.iteritems())}
    return [_boolify(raw=_, custom_values=custom_values, non_str=non_str, raise_exc=raise_exc) for _ in raw]
  return _boolify(raw=raw, custom_values=custom_values, non_str=non_str, raise_exc=raise_exc)

boolify.__doc__ = """
Function that will translate common strings into bool values.

  Case is ignored for strings. These string values are handled:
    True -> '{TRUE}'
    False -> any other string

  {PARAM1}:
    Non-string values are passed to bool.

  When '{PARAM1}' is passed as False, Objects other than string will be transformed using built-in bool() function.

  Raises ValueError when '{PARAM2}' is passed as True and it gets a string it doesn't handle.
""".format(TRUE="', '".join(TRUE), PARAM1=boolify.__code__.co_varnames[-3], PARAM2=boolify.__code__.co_varnames[-2])

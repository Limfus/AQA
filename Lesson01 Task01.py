"""
we have norway text in old style formatting
re-write the same text as:
#1 string with format() call
#2 f-string
use linter(https://github.com/wemake-services/wemake-python-styleguide)
to check your new created python module for possible linter errors
try to run code from pycharm/command line
"""

norway_text = 'Automatisering akselererer %syeblikket da roboter vil erobre planeten v%sr. (%s)' % ('ø', 'å', 'Æ')
print(norway_text)

norway_text1 = 'Automatisering akselererer {}yeblikket da roboter vil erobre planeten v{}r. ({})'.format('ø', 'å', 'Æ')
print(norway_text1)

ø = 'ø'
å = 'å'
Æ = 'Æ'
norway_text2 = f'Automatisering akselererer {ø}yeblikket da roboter vil erobre planeten v{å}r. ({Æ})'
print(norway_text2)

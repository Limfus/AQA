norway_text = 'Automatisering akselererer %syeblikket da' \
              ' roboter vil erobre planeten v%sr. (%s)' % ('ø', 'å', 'Æ')
print(norway_text)

norway_text1 = 'Automatisering akselererer {}yeblikket da roboter vil' \
               ' erobre planeten v{}r. ({})'.format('ø', 'å', 'Æ')
print(norway_text1)

ø = 'ø'
å = 'å'
Æ = 'Æ'
norway_text2 = f'Automatisering akselererer {ø}yeblikket' \
               f' da roboter vil erobre planeten v{å}r. ({Æ})'
print(norway_text2)

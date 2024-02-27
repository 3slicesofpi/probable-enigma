# must be more than 8, less than 24 chars long
# no spaces
# must contain 1 uppercase
# must contain 1 mathsymbol +=*/
# must contain 1 wordsymbol !?,.
# symbols cannot be at the very front.
# must contain 5 numbers

import re

raw = 'Password=12345!'
if (((len(raw)<8) or (len(raw)>24)) == False) and (re.search(' ',raw) == None) and (re.search('[A-Z]+',raw) != None) and (re.search('.[+|=|*|/]+',raw) != None) and (re.search('.[!|?|.|,]+',raw) != None) and (len(re.findall('[0-9]',raw))>=5):
    print('good')
else:
    print('bad')


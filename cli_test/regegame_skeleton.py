import csv
filename = 'puzzleDataFile.csv'
fields = ('identifier', 'expression','difficulty', 'description', 'solution', 'charlimit')
puzzleData = [  # PEP 8 E231: Please include spaces after commas in lists (everything will explode)
    # word, word NOT word,word learn the best practices its definitely not because I created a huge pile of jank
    # ignore the 7 red errors
    ['T01', 'Literal Introduction', 'abcABC123', 0, "Let's start off simple. These are literal characters.\nFor each character in the pattern, copy them down to match them.", 'abcABC123', 9, ['tutorial', 't1' 'begin', 'start', 'first', '1st', 'string', 'uniq:00Ehk']],
    ['T02', 'Bracket Basics', '[abc][ABC](123)', 0, 'Square Brackets: One of each character in the bracket will be matched.\nExample: [abc] will match either "a", "b" or "c".\nCircular Brackets: All the characters within are grouped together.', 'aA123', 5, ['tutorial', 't2', 'second', ' 2nd', 'round', 'square', 'circular', '[', '(', 'uniq:00Ehk']],
    ['T03', 'Simple Symbols', '^n...a$', 0, "\The caret '^' Characters/groups after the '^' should be in the beginning of the line.\nThe dollar symbol '$' Characters preceding the '$' should be at the end of the line.\nThe Wildcard '.' Any character will be matched.", 'ninja', 5, ['tutorial', 't3', 'caret', 'dollar', 'wildcard', 'period', 'dot', '.', '^', '$', 'uniq:00Ehk']],
    ['T04', 'Repeaters/Quantifiers', 'c*a+t?', 0,"Simple Repeaters.\nThe Plus symbol '+' The character/group preceding the '+' needs to be matched one or more times\nThe Asterisk '*': The character/group before the '*' can be matched one or more times or be omitted entirely.\nThe Optional '?' The character/group before the '?' can be matched once or not at all.", 'cat', 6, ['tutorial', 't4', 'repeater', 'quantifier', 'plus', 'counter', 'asterisk', '*', '+', '?', 'uniq:00Ehk']],
    ['T05', 'Number of Repetitions', 'repeat[ME]twice{2}[thrice]{3,}(4ice...?){1,4}', 0, "Repeaters with Curly Braces. '{number}'\nThe character/group before the '{N}' should be matched N times\n{MIN} means that the preceding character/group should be matched a minimum of min times.\n{MIN, MAX}means that the preceding group/character should be matched at least MIN and at most MAX times.", 'repeatMtwiceetttt4iceyco?iceyco?', 30, ['tutorial', 't5', 'repeater', 'quantifier', 'count', 'curly', 'bracket', '{', 'range', 'uniq:00Ehk']],
    ['T06', 'Character Classes', '-\d{3}\s\S\D*\w*.\W?', 0, "\n\s: Any whitespace characters such as space and tab. \S: Any non-whitespace characters.\n\d: Any digit character.\D: Any non-digit characters.\n\w : Any word character (basically alpha-numeric). \W: Any non-word character.", '', 8, ['tutorial','t6','class', '/', '\\', 'whitespace', 'alphanumeric', 'alpha-numeric', 'uniq:00Ehk']],
    ['T07', 'Square Brackets Extras', '^[n-v][C-f][^3][^0-9\w]?', 0, "Range 'first-last' Any single character between the range will be matched. Example: a-c matches 'a','b','c', z-A matches 'z' and 'a'.\nNegation '^' Matches any character except the characters in the brackets.", 'nC4a', 5, ['tutorial', 't7', 'second', ' 7th', '[', 'uniq:00Ehk']],
    ['T08', 'Alternative Answers', '(OR|andonlyOR)(and|maybe|AND)', 0, "Alternation '|'\nExpressions matching the text either before and after the '|' are matched.", 'andonlyor', 12, ['tutorial', 't8', 'alternation', '|', 'or', '(', 'choose', 'uniq:00Ehk']],
    ['T09', 'Backslash Backshot', '\^\[doin.regex!\]\{3\}\$+', 0, "Some symbols will appear with the backslash symbol. These are escaped symbols to match for the actual '+','?','*' characters.", '^[doingregex!]{3}$$$', 20, ['tutorial', 't9', 'backslash', 'sex', 'symbols', 'escaped', 'backshot', 'actual', '/', 'uniq:00Ehk']],
    ['T10', 'Tutorial End', '.(?#prepare to suffer)', 0, "Comments '(?# words)' have no effect. They start with a '(?#' and end with ')'.", 'a', 1, ['like', 'and', 'subscribe', 'suffer', 'last', '#', 'comment', 'uniq:00Ehk']],
    ['E01', 'Exact Phrases', '.*stocks?\s?tips?.*', 1, "The '.'s matches any characters before the expression, preventing regex from matching stuff before and after.\nThe '?' after 's' allows matches of both stocks and stock and tips and tip.\nThe '?' after '/s' allows matches of spaces between stock and tip.", 'stock tip', 20, ['stock', 'tip', 'literal', 'uniq:00Fla']],
    ['E02', 'Barcode', '\s.\d{6}.\d{6}.\s', 1, "Example Regex for UPC-A barcodes, which have twelve numbers. This expression uses repeaters to match multiple numbers.", ' |123456|789012| ', 17, ['upc-a', 'repeater', 'quantifier', 'uniq:00Fla']],
    ['E03', 'Postal Code', '[0[1-9]|[1-7]\d|8[1|2]]\d{4}', 1, 'This expression matches six numbers which start from 01 to 82, as per regional codes.', '821000', 100, ['address', 'house', 'pipe', 'bomb', '82', 'quantifier', 'uniq:00Fla']],
    ['E04', 'Email', '.+@(mymail|gmail|hotmail|yahoo)(?#add more if needed).*\.com', 1, 'This expression uses alternation so match different email service providers like gmail and yahoo.\nThe inline comment reminds others to add more email service providers.', 'example@mymail.com', 50, ['alternation','asterisk','quantifier', 'uniq:00Fla']],
    ['E05', 'Phone Number', '(\+?\d{1,3})?(-\s\.)?\d{4}(-\s\.)?\d{4}', 1, 'Phone Number\nThis expression matches eight numbers with allowance for dash or whitespace in the middle.\nAlso allows for country codes.', '+65-1234-5678', 13, ['whitespace', 'escaped', 'contact', 'uniq:00Fla']],
    ['E06', 'IP Address', '((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])', 1, "'25[0-5]' matches numbers from 250-255, '2[0-4][0-9]' matches 200-249, '1[0-9]{2}' matches 100-199\n'[1-9]?[0-9]' matches numbers from 0-99 and '[1-9]?' wnsures single digits 0-9 are matched correctly.\nThe first group contains an extra '\.' to separate the numbers and is matched thrice.", '', 15, ['grabber', 'quantifier', 'repeater', 'ipv4', 'uniq:00Fla']]]

with open(filename, 'w', newline='') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    # writing the fields
    csvwriter.writerow(fields)
    csvwriter.writerows(puzzleData)

with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        print(row)


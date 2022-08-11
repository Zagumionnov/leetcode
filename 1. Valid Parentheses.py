def is_valid(s: str) -> bool:
    if len(s) == 0 or s[0] == '}' or s[0] == ']' or s[0] == ')':
        return False
    while len(s) > 0:
        if '()' in s or '[]' in s or '{}' in s:
            s = s.replace('()', '').replace('[]', '').replace('{}', '')
            if len(s) == 0:
                return True
        else:
            return False



s1 = "()()()()()()()"
s2 = "(){}[][))("
s3 = "({[]})"
s4 = "(]"
s5 = ''
s6 = '('
s7 = '()'
s8 = '(()'


print(is_valid(s8))

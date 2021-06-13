# Input (string with only well balanced parenthesis and spaces are only for illustrative purposes):
# ( ( ) ( ) ) ( ) ( )
# 0 1 2 3 4 5 6 7 8 9
#
# Output:
# [(0, 5), (1, 2), (3, 4), (6, 7), (8, 9)]

from typing import List

def parse(items: List):
  m1 = dict()
  s = []

  for k, v in enumerate(items):
    if v == '(':
      s.append(k)
      m1[k] = (k)

    if v == ')':
      begin = s.pop()
      m1[begin] = (begin, k)

  return list(m1.values())

#---------------
tst1 = ['(', '(', ')', '(', ')', ')', '(', ')', '(',')']
tst2 = '(()())()()'

rv1 = parse( [c for _, c in enumerate(tst2)] )
rv2 = parse(tst1)
print(rv1)
print(rv1)
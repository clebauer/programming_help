# Setting up my functions. Good luck.
# If you wanna read the program, scroll down a little farther.
def so(g):
  return ''.join([chr(x) for x in g])
def cassie(h):
  return ''.join([chr(x) for x in h])
def is_in(l):
  return ''.join([chr(x) for x in l])
def confusing(f):
  return ''.join([chr(x) for x in f])
def love(m):
  return ''.join([chr(x) for x in m])
def that(d):
  return ''.join([chr(x) for x in d])
def lets(a):
  return ''.join([chr(x) for x in a])
def you(o):
  return ''.join([chr(x) for x in o])
def say(j):
  return ''.join([chr(x) for x in j])
def she(k):
  return ''.join([chr(x) for x in k])
def can(i):
  return ''.join([chr(x) for x in i])
def make(b):
  return ''.join([chr(x) for x in b])
def functions(c):
  return ''.join([chr(x) for x in c])
def with_(n):
  return ''.join([chr(x) for x in n])
def are(e):
  return ''.join([chr(x) for x in e])

# HERE IT IS. THE CODE.
vals = {0:[73], 1:[97,109], 2:[115,111], 3:[117,110,98,101,108,105,101,118,97,98,108,121], 4:[105,110], 5:[108,111,118,101], 6:[119,105,116,104], 7:[121,111,117], 8:[97,110,100], 9:[73,39,109], 10:[115,111], 11:[112,114,111,117,100], 12:[116,111], 13:[116,101,108,108], 14:[121,111,117,33]}

fns = [lets, make, functions, that, are, confusing, so, cassie, can, say, she, is_in, love, with_, you]

wctb = {k:v(vals[k]) for (k,v) in zip(range(len(fns)), fns)}

# ❤
print ''.join(['{} '.format(x) for x in wctb.values()])

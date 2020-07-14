'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
  if len(word) == 0 or len(word) == 1:
    return 0
  idx = 0
  count = [0] 
  fn(word, idx, count)
  return count[0]

def fn(word, idx, count):
  if idx == len(word) - 1:
    return
  if word[idx] == 't' and word[idx+1] == 'h':
    count[0] += 1
  fn(word, idx + 1, count)


print(count_th("thxxtxxxthhxxxxth"))
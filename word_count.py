def word_count(line):
  # comp_dict = {i : 0 for i in comps}
  counts = {}

  words = line.split()
  print(words)
    
  print('Words: ', words)
  print('Counting..')
    
  for word in words:
      counts[word] = counts.get(word, 0) + 1

  print('Counts', counts)

  bigCount = None
  bigWord = None
  for word, count in counts.items():
      if bigCount is None or count > bigCount: 
          bigWord = word
          bigCount = count

  print(bigWord, bigCount)


if __name__ == '__main__':
	line = 'The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog.'
	word_count(line)
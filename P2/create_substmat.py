def create_substmat(filename):
  f = open(filename)
  sequences = []
  for line in f.readlines():
        if not line.startswith('>'):
          line.strip()
          sequences.append(line)

  count = 0
  alignments = {}
  for i in range(0,len(sequences) - 1):
    for j in range(1+count, len(sequences)):

      pairs = zip(sequences[i], sequences[j])
      
      for pair in pairs:
        if pair[::-1] in alignments:
          pair = pair[::-1]
        elif pair not in alignments:
          alignments[pair] = 0
        alignments[pair] += 1
        
    count += 1


return matrix

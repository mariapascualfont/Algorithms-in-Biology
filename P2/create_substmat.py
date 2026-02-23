def create_substmat(filename):
  f = open(filename)
  sequences = []
  for line in f.readlines():
        if not line.startswith('>'):
          line.strip()
          sequences.append(line)

  count = 0
  total_alignments = 0
  alignments = {}
  for i in range(0,len(sequences) - 1):

    for j in range(1+count, len(sequences)):
      total_alignments += len(sequences[0]) 
      pairs = zip(sequences[i], sequences[j])
      
      for pair in pairs:
        if pair[::-1] in alignments:
          pair = pair[::-1]
        elif pair not in alignments:
          alignments[pair] = 0
        alignments[pair] += 1
    
    count += 1

  observed_frequencies = alignments.copy()
  
  for i in observed_frequencies:
    observed_frequencies[i] = observed_frequencies[i]/total_alignments

  expected_frequencies = {}
  total_elems = 0

  for i in sequences:
    for j in i:
      total_elems += 1
      if j not in expected_frequencies:
        expected_frequencies[j] = 0
      expected_frequencies[j] += 1

  for i in expected_frequencies:
    expected_frequencies[i] = expected_frequencies[i]/total_elems    
  

  log_odds_ratio = alignments.copy()

  for i in log_odds_ratio:
    log_odds_ratio[i] = int((math.log(observed_frequencies[i]/(expected_frequencies[i[0]] *expected_frequencies[i[1]])))*10)

  return log_odds_ratio


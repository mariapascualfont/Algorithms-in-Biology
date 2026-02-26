
import math
def create_substmat(filename, aminoacids: str ='ACDEFGHIKLMNPQRSTVWY'):
  f = open(filename)
  sequences = []
  for line in f.readlines():
        if not line.startswith('>'):
          line = line.strip()
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


  expected_frequencies_elems = {}
  total_elems = 0

  for i in sequences:
    for j in i:
      total_elems += 1
      if j not in aminoacids:
         print("The alignment contains amino acids that are not in the provided alphabet")
      if j not in expected_frequencies_elems:
        expected_frequencies_elems[j] = 0
      expected_frequencies_elems[j] += 1

  for i in expected_frequencies_elems:
    expected_frequencies_elems[i] = expected_frequencies_elems[i]/total_elems


  expected_frequencies = alignments.copy()

  for pair in expected_frequencies:
    a,b = pair
    if a == b:
      expected = expected_frequencies_elems[a] ** 2
    else:
      expected = 2 * expected_frequencies_elems[a] * expected_frequencies_elems[b]

    expected_frequencies[pair] = expected

  log_odds_ratio = alignments.copy()

  for i in log_odds_ratio:
    ratio = observed_frequencies[i] / expected_frequencies[i]
    log_val = math.log10(ratio)
    log_odds_ratio[i] = round(log_val * 10)

  symbols = expected_frequencies_elems.keys()
  symbols = sorted(symbols)


  print(" ", end="")
  for s in symbols:
      print("    " + s, end="")
  print()

  for i, s1 in enumerate(symbols):
      print(f"{s1}", end="")
      for j, s2 in enumerate(symbols):
          if j > i:
              break

          pair = (s1, s2)
          if pair not in log_odds_ratio:
              pair = (s2, s1)

          value = log_odds_ratio.get(pair, 0)
          print(f"{value:>5}", end="")
      print()
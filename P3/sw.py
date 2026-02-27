from Bio.Align import substitution_matrices
import sys

def sw(seq_i, seq_j, gap):

    gap = int(gap)
    subst_mat = substitution_matrices.load('BLOSUM62')
    # Store the lengths of the sequences
    n_i, n_j = len(seq_i), len(seq_j)

    # Initialize scores and traceback matrices
    scores = [[0 for _ in range (n_j + 1)] for _ in range(n_i + 1)]
    traceback = [[0 for _ in range (n_j + 1)] for _ in range(n_i + 1)]

    # Initialize edges with gaps
    for i in range(1, n_i + 1):
        scores[i][0] = 0
        traceback[i][0] = 1

    for j in range(1, n_j + 1):
        scores[0][j] = 0
        traceback[0][j] =  -1

    # Fill the matrices
    for i in range(1, n_i + 1):
        for j in range(1, n_j + 1):
            # Calculate scores for all possibilities
            diag = scores[i-1][j-1] + subst_mat[seq[i-1]][seq[i-1]]
            left = scores[i][j-1] + gap
            up = scores[i-1][j] + gap

            # Choose the best scores
            # Set traceback pointer
            if diag > left and diag > up:
              if diag < 0:
                scores[i][j] = 0
                traceback[i][j] = 2
              else:
                scores[i][j] = diag
                traceback[i][j] = 0

            elif left > up:
              if left < 0:
                scores[i][j] = 0
                traceback[i][j] = 2
              else:
                scores[i][j] = left
                traceback[i][j] = -1

            else:
              if up < 0:
                scores[i][j] = 0
                traceback[i][j] = 2
              else:
                scores[i][j] = up
                traceback[i][j] = 1


    #search for the max value 
    maximum = 0
    max_i = 0
    max_j= 0
    for i in range(len(scores)) :
      if max(scores[i]) > maximum:
        maximum = max(scores[i])
        max_i = i
        max_j = scores[i].index(max(scores[i]))

    # Print optimal score
    print("Optimal score:", scores[max_i][max_j])
    # Prepare for traceback
    aln_i, aln_j = [], []

    i, j = max_i, max_j # the starting point is the highest value cell

    # Traceback
    while scores[i][j] != 0:

        if traceback[i][j] == 0:  # diagonal
                i -= 1
                j -= 1
                aln_i.append(seq_i[i])
                aln_j.append(seq_j[j])
        elif traceback[i][j] == -1:  # left
                j -= 1
                aln_i.append('-')
                aln_j.append(seq_j[j])
        else:  # up (traceback[i][j] == 1)
                i -= 1
                aln_j.append('-')
                aln_i.append(seq_i[i])

    # Print the alignment
    # a few lines here
    aln_i = "".join(aln_i[::-1])
    aln_j = "".join(aln_j[::-1])
    print(aln_i)
    print(aln_j)

nw_substmat(sys.argv[1], sys.argv[2], sys.argv[3])

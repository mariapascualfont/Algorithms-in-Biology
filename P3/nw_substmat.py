from Bio.Align import substitution_matrices
import sys

def nw_substmat(seq_i, seq_j, gap):

    gap = int(gap)
    subst_mat = substitution_matrices.load('BLOSUM62')
    # Store the lengths of the sequences
    n_i, n_j = len(seq_i), len(seq_j)

    # Initialize scores and traceback matrices
    scores = [[0 for _ in range (n_j + 1)] for _ in range(n_i + 1)]
    traceback = [[0 for _ in range (n_j + 1)] for _ in range(n_i + 1)]

    # Initialize edges with gaps
    for i in range(1, n_i + 1):
        scores[i][0] = i * gap
        traceback[i][0] = 1 

    for j in range(1, n_j + 1):
        scores[0][j] = j * gap
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
                scores[i][j] = diag
                traceback[i][j] = 0  
                # a few lines here
            elif left > up:
                scores[i][j] = left
                traceback[i][j] = -1  
                # a few lines here
            else:
                scores[i][j] = up
                traceback[i][j] = 1 
                # a few lines here


    # Print optimal score
    print("Optimal score:", scores[n_i][n_j])
    # Prepare for traceback
    aln_i, aln_j = [], []
    i, j = n_i, n_j # fill in; this is the starting point for traceback

    # Traceback
    while i > 0 or j  > 0:  # fill in
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

    aln_i = "".join(aln_i[::-1])
    aln_j = "".join(aln_j[::-1])
    print(aln_i)
    print(aln_j)

nw_substmat(sys.argv[1], sys.argv[2], sys.argv[3])

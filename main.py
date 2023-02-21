##################################################
# Original code accessed on the 02/17/2023
# taken from: https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/
# Author: Nikhil Kumar Singh
# Dynamic Programming implementation of LCS problem
##################################################

from textModule import *
import math

online_code = process_file("online_code.txt", "utf-8")
edit_code = process_file("edit_code.txt", "utf-8")


def lcs(X, Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)

    # declaring the array for storing the dp values
    L = [[None] * (n + 1) for i in range(m + 1)]

    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]


def main():
    edit_len = len(edit_code)
    text_uniqueness = lcs(edit_code, online_code)

    print(f"{math.floor(text_uniqueness / edit_len * 100)}% texts of this code was copied online.")
    print(f"{math.ceil((edit_len - text_uniqueness) / edit_len * 100)}% texts of this code was unique.")


if __name__ == "__main__":
    main()

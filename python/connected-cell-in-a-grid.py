#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict, deque


# Complete the connectedCell function below.
def connectedCell(matrix):
    m, n = len(matrix), len(matrix[0])
    visited = {}
    edges = defaultdict(list)

    def insert_edge(u, v):
        edges[u].append(v)

    for i in range(m):
        for j in range(n):
            cur = i * 10 + j
            visited[cur] = False
            if matrix[i][j] == 1:
                insert_edge(cur, cur)
                if i - 1 >= 0 and j - 1 >= 0 and matrix[i - 1][j - 1] == 1:
                    insert_edge(cur, (i - 1) * 10 + (j - 1))
                if i - 1 >= 0 and matrix[i - 1][j] == 1:
                    insert_edge(cur, (i - 1) * 10 + j)
                if i - 1 >= 0 and j + 1 < n and matrix[i - 1][j + 1] == 1:
                    insert_edge(cur, (i - 1) * 10 + (j + 1))
                if j + 1 < n and matrix[i][j + 1] == 1:
                    insert_edge(cur, i * 10 + (j + 1))
                if i + 1 < m and j + 1 < n and matrix[i + 1][j + 1] == 1:
                    insert_edge(cur, (i + 1) * 10 + (j + 1))
                if i + 1 < m and matrix[i + 1][j] == 1:
                    insert_edge(cur, (i + 1) * 10 + j)
                if i + 1 < m and j - 1 >= 0 and matrix[i + 1][j - 1] == 1:
                    insert_edge(cur, (i + 1) * 10 + (j - 1))
                if j - 1 >= 0 and matrix[i][j - 1] == 1:
                    insert_edge(cur, i * 10 + (j - 1))

    def bfs(start):
        q = deque([start])
        visited[start] = True
        counter = 1
        while q:
            u = q.popleft()
            for v in edges[u]:
                if visited[v] is False:
                    q.append(v)
                    visited[v] = True
                    counter += 1
        return counter

    ans = 0
    for i in range(m):
        for j in range(n):
            cur = i * 10 + j
            if visited[cur] is False and matrix[i][j] == 1:
                ans = max(ans, bfs(cur))
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()

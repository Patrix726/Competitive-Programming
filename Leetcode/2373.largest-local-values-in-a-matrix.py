# @leet imports start
import bisect
import collections
import copy
import datetime
import functools
import heapq
import io
import itertools
import json
import math
import operator
import random
import re
import statistics
import string
import sys
from bisect import *
from builtins import *
from collections import *
from copy import *
from datetime import *
from functools import *
from heapq import *
from io import *
from itertools import *
from json import *
from math import *
from operator import *
from random import *
from re import *
from statistics import *
from string import *
from sys import *
from typing import *

# @leet imports end


# @leet start
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        centers = {}
        for i in range(n - 2):
            for j in range(m - 2):
                key = "_".join([str(i + 1), str(j + 1)])
                centers[key] = -1

        for i in range(n):
            for j in range(m):
                value = grid[i][j]
                possible_centers = [
                    "_".join([str(i), str(j)]),
                    "_".join([str(i + 1), str(j)]),
                    "_".join([str(i - 1), str(j)]),
                    "_".join([str(i), str(j + 1)]),
                    "_".join([str(i), str(j - 1)]),
                    "_".join([str(i + 1), str(j + 1)]),
                    "_".join([str(i - 1), str(j - 1)]),
                    "_".join([str(i + 1), str(j - 1)]),
                    "_".join([str(i - 1), str(j + 1)]),
                ]
                for key in possible_centers:
                    if centers.get(key, False):
                        centers[key] = max(centers[key], value)
        output = [[0 for i in range(m - 2)] for j in range(n - 2)]
        for key, value in centers.items():
            str_i, str_j = key.split("_")
            i, j = int(str_i) - 1, int(str_j) - 1
            output[i][j] = value
        return output


# @leet end


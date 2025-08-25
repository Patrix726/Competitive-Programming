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
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        elms = n * m
        up_dir = True
        x, y = 0, 0
        output = []
        while elms > 0:
            if up_dir:
                if y < 0 and x >= m:
                    up_dir = False
                    y += 2
                    x -= 1
                elif y < 0:
                    up_dir = False
                    y += 1
                elif x >= m:
                    up_dir = False
                    x -= 1
                    y += 2
            else:
                if x < 0 and y >= n:
                    up_dir = True
                    y -= 1
                    x += 2
                elif y >= n:
                    up_dir = True
                    y -= 1
                    x += 2
                elif x < 0:
                    up_dir = True
                    x += 1
            if x >= 0 and x < m and y >= 0 and y < n:
                output.append(mat[y][x])
                elms -= 1
            if up_dir:
                x += 1
                y -= 1
            else:
                x -= 1
                y += 1
        return output


# @leet end


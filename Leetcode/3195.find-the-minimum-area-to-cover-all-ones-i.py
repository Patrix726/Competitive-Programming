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
    def minimumArea(self, grid: List[List[int]]) -> int:
        m = len(grid[0])
        n = len(grid)
        min_x, min_y = n, m
        max_x, max_y = 0, 0
        for x in range(n):
            for y in range(m):
                if grid[x][y] == 1:
                    min_x = min(x, min_x)
                    min_y = min(y, min_y)
                    max_x = max(x, max_x)
                    max_y = max(y, max_y)
        width = max_x - min_x + 1
        height = max_y - min_y + 1
        # if height == 0 and width == 0:
        #     return 1
        # if height == 0:
        #     return width
        # if width == 0:
        #     return height
        return height * width


# @leet end


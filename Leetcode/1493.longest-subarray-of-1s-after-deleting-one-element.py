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
    def longestSubarray(self, nums: List[int]) -> int:
        counts = []
        count = 0

        for num in nums:
            if num != 1:
                counts.append(count)
                count = 0
            else:
                count += 1
        counts.append(count)
        print(counts)
        max_count = -1
        if len(counts) == 1:
            return counts[0] - 1

        if len(counts) <= 2:
            return sum(counts)

        for i in range(1, len(counts)):
            max_count = max(max_count, counts[i] + counts[i - 1])
        return max_count


# @leet end


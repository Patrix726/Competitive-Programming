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
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        unique_freq = set()
        multi_freq = set()
        for num, num_count in count.items():
            if num_count in unique_freq or num_count in multi_freq:
                unique_freq.discard(num_count)
                multi_freq.add(num_count)
            else:
                unique_freq.add(num_count)
        sorted_list = list(
            sorted(
                filter(lambda x: count[x] in unique_freq, nums), key=lambda x: count[x]
            )
        )
        for val in multi_freq:
            duplicate_list = list(filter(lambda x: count[x] == val, nums))
            duplicate_list.sort(reverse=True)
            cur = 0
            while cur < len(sorted_list):
                cur_count = count[sorted_list[cur]]
                if cur_count > val:
                    break
                cur += cur_count
            sorted_list[cur:cur] = duplicate_list
        return sorted_list


# @leet end


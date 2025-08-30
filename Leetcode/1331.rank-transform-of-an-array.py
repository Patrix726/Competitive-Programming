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
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = list(sorted(arr))
        rank = {}
        cur_rank = 1
        for num in sorted_arr:
            if not rank.get(num, False):
                rank[num] = cur_rank
                cur_rank += 1
        return [rank[num] for num in arr]


# @leet end


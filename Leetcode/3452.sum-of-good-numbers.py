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
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        total_sum = 0
        n = len(nums)
        for i in range(n):
            if (i - k < 0 or nums[i-k] < nums[i]) and (i+k>=n or nums[i+k] < nums[i]):
                total_sum += nums[i]

        return total_sum
        
# @leet end

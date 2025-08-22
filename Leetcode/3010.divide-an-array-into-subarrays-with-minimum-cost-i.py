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
    def minimumCost(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return sum(nums)

        mins = [nums[1], nums[2]]
        mins.sort()
        for num in nums[3:]:
            if num < mins[0]:
                mins[1], mins[0] = mins[0], num
            elif num < mins[1]:
                mins[1] = num
        return sum(mins) + nums[0]


# @leet end


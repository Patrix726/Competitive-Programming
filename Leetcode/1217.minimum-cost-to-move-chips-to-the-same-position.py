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
    def minCostToMoveChips(self, position: List[int]) -> int:
        odds = list(filter(lambda x: x % 2 != 0, position))
        evens = list(filter(lambda x: x % 2 == 0, position))

        if len(odds) >= len(evens):
            return len(evens)
        else:
            return len(odds)


# @leet end


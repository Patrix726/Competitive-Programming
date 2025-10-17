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
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        coordinates = {}
        distances = {}
        for idx, char in enumerate(s):
            coordinate = coordinates.get(char, None)
            if not coordinate and coordinate != 0:
                coordinates[char] = idx
            else:
                distances[char] = idx - coordinates[char] - 1

        for key, val in distances.items():
            idx = ord(key) - 97
            if val != distance[idx]:
                return False
        return True


# @leet end


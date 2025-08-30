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
    def generateTheString(self, n: int) -> str:
        char1 = "a"
        char2 = "b"
        char3 = "c"
        if n == 1:
            return char1
        if n % 2 == 0:
            return "".join([char1 * (n - 1), char2])
        return "".join([char1 * (n - 2), char2, char3])


# @leet end


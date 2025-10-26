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
    def numPrimeArrangements(self, n: int) -> int:
        prime_count = 0
        for i in range(1, n + 1):
            if i == 1:
                continue
            is_prime = True
            for j in range(2, ceil(sqrt(i)) + 1):
                if i % j == 0:
                    is_prime = False
            if is_prime or i == 2:
                prime_count += 1
        return (factorial(prime_count) * factorial(n - prime_count)) % (10**9 + 7)


# @leet end


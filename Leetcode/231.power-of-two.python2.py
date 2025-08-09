# @leet imports start
import bisect
import collections
import copy
import datetime
import functools
import heapq
import itertools
import math
import operator
import random
import re
import string
from bisect import *
from collections import *
from copy import *
from datetime import *
from functools import *
from heapq import *
from itertools import *
from math import *
from operator import *
from random import *
from re import *
from string import *

# @leet imports end

# @leet start
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1:
            return True
        while n > 2:
            n /= 2.0
        return n==2.0


        
# @leet end

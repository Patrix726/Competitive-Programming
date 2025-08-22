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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.total = 0

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        cur = root
        self.dfs(root)
        return self.total

    def dfs(self, cur):
        if not cur:
            return 0
        if not cur.left and not cur.right:
            return True
        left = self.dfs(cur.left)
        right = self.dfs(cur.right)
        if left:
            self.total += cur.left.val
        return False


# @leet end


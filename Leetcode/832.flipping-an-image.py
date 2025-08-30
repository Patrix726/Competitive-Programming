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
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        for i in range(n):
            for j in range((m + 1) // 2):
                if j != m - j - 1:
                    image[i][j], image[i][m - j - 1] = image[i][m - j - 1], image[i][j]
                    image[i][j] = 1 if image[i][j] == 0 else 0
                    image[i][m - j - 1] = 1 if image[i][m - j - 1] == 0 else 0
                else:
                    image[i][j] = 1 if image[i][j] == 0 else 0
        return image


# @leet end


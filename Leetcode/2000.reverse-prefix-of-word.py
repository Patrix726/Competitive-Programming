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
    def reversePrefix(self, word: str, ch: str) -> str:
        ch_idx = word.find(ch)
        if ch_idx == -1:
            return word
        sliced_word = word[: ch_idx + 1]
        sliced_word = "".join(list(reversed(sliced_word)))

        if ch_idx == len(word) - 1:
            return sliced_word
        return "".join([sliced_word, word[ch_idx + 1 :]])


# @leet end


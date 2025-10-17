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
    def reorderSpaces(self, text: str) -> str:
        split_text = text.split(" ")
        split_text_normalized = list(filter(lambda x: len(x) > 0, split_text))
        text_without_spaces = "".join(split_text_normalized)
        space_count = len(text) - len(text_without_spaces)
        if len(split_text_normalized) == 1:
            return text_without_spaces + " " * space_count
        n = len(split_text_normalized) - 1
        inside_spaces = space_count // n
        end_spaces = space_count % n
        join_char = " " * inside_spaces
        return join_char.join(split_text_normalized) + " " * end_spaces


# @leet end


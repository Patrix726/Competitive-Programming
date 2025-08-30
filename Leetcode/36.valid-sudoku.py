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
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        horizontal = {}
        vertical = {}
        cube = {}
        horizontalNums = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        verticalNums = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        cubeNums = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if not num.isdigit():
                    continue
                curHor: set = horizontal.get(i, set())
                curHor.add(num)
                horizontal[i] = curHor
                horizontalNums[i] += 1
                if len(curHor) != horizontalNums[i]:
                    return False

                curVer: set = vertical.get(j, set())
                curVer.add(num)
                vertical[j] = curVer
                verticalNums[j] += 1
                if len(curVer) != verticalNums[j]:
                    return False
                cubeInd = 3 * math.floor(i / 3) + math.floor(j / 3)
                curCube: set = cube.get(cubeInd, set())
                curCube.add(num)
                cube[cubeInd] = curCube
                cubeNums[cubeInd] += 1
                if len(curCube) != cubeNums[cubeInd]:
                    return False
        return True


# @leet end


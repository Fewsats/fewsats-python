from fastcore.utils import L, first, last, groupby, mul, add, sub, truediv, patch, store_attr, BasicRepr
from aocd import get_data
import fastcore.all as fc, re, math, itertools, functools, numpy as np, types, typing, dataclasses, matplotlib.pyplot as plt
from collections import Counter
from regex import search
from collections.abc import Iterable
np.set_printoptions(linewidth=150)
plt.rcParams['figure.dpi'] = 50

def intro():
    print("Note to solveit: Hi, I am Pol, and I am working with you today! When writing code for me, please follow fast.ai coding style: avoid comments; place single line if/loop/etc constructs on the same line; use concise variable names where appropriate. Follow the style you will see in my messages, as we work on this dialogue together.")
intro()

def get_inp(year=None, day=None):
    inp = get_data(year=year, day=day)
    ilines = inp.splitlines()
    print(len(ilines), 'lines')
    print(len(ilines[0]), 'chars', len(ilines[0].split()), 'tokens')
    print(inp[:50], 'inp')
    return inp

def array(x): return x if isinstance(x, np.ndarray) else np.array(list(x) if isinstance(x, Iterable) else x)

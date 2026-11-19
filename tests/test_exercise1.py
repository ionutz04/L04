import os
import sqlite3
import subprocess

import pytest

import exercise1
from exercise1 import *


# bug report 1
def test_r1_is_even_returns_true():
    assert is_even(4) == True


# bug report 2
def test_r2_rectangle_area_with_correct_docstring():
    assert rectangle_area(3, 4) == 12

#!/usr/bin/env python3
""" index range tool """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    """ page system """
    page = page - 1
    start_index = page * page_size
    end_index = (page + 1) * page_size
    return tuple((start_index, end_index))

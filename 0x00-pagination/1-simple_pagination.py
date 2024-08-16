#!/usr/bin/env python3
""" index range tool """
from typing import Tuple, List
import csv
import math


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page: int, page_size: int) -> Tuple[int, ...]:
        """ page system """
        page = page - 1
        start_index = page * page_size
        end_index = (page + 1) * page_size
        return tuple((start_index, end_index))

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert type(page) is int and type(page_size) is int, \
            "Page and page size must be int"
        assert page > 0, "Page number must be greater than 0"
        assert page_size > 0, "Page size must be greater than 0"
        totlines = len(list(self.dataset()))
        totpages = math.ceil(totlines / page_size)
        if page > totpages or page_size > totlines:
            return []
        indexrange = self.index_range(page, page_size)
        return [line for line in self.dataset()[indexrange[0]: indexrange[1]]]
    


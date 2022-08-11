from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        jobs = csv.DictReader(file)
        list = []
        for job in jobs:
            list.append(job)
    return list

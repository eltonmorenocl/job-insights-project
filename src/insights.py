from src.jobs import read


def get_unique_job_types(path):
    list_jobs = read(path)
    types = set()
    for job in list_jobs:
        types.add(job["job_type"])
    return types


def filter_by_job_type(jobs, job_type):
    list_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            list_jobs.append(job)
    return list_jobs


def get_unique_industries(path):
    list_jobs = read(path)
    types = set()
    for ind in list_jobs:
        if ind["industry"] != '':
            types.add(ind["industry"])
    return types


def filter_by_industry(jobs, industry):
    list_jobs = []
    for job in jobs:
        if job["industry"] == industry:
            list_jobs.append(job)
    return list_jobs


def get_max_salary(path):
    list_jobs = read(path)
    salary = 0
    for job in list_jobs:
        if job["max_salary"].isdigit() and job["max_salary"] != '':
            if int(job["max_salary"]) > salary:
                salary = int(job["max_salary"])
    return salary


def get_min_salary(path):
    list_jobs = read(path)
    salary_min = set()
    for salary in list_jobs:
        if salary["min_salary"].isdigit() and salary["min_salary"] != '':
            salary_min.add(int(salary["min_salary"]))

    return min(salary_min)


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError('min_salary ou max_salary ausentes no dicionário')

    if type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        raise ValueError('min_salary ou max_salary tem valores não-numéricos')

    if type(salary) != int:
        raise ValueError('parâmetro salary tem valores não numéricos')

    if job["min_salary"] > job["max_salary"]:
        raise ValueError('valor min_salary é maior que o valor de max_salary')

    return salary in range(int(job["min_salary"]), int(job["max_salary"]))


def filter_by_salary_range(jobs, salary):
    list_salary = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                list_salary.append(job)
        except ValueError:
            print('')
    return list_salary

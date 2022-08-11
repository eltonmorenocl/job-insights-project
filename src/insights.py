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
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []

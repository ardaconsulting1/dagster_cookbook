import dagster as dg
from .ops import reload_repo_op

@dg.job()
def reload_repo_job():
    reload_repo_op()
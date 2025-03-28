import dagster as dg
from dagster_graphql import DagsterGraphQLClient, ReloadRepositoryLocationInfo, ReloadRepositoryLocationStatus

@dg.op()
def reload_repo_op():
    client = DagsterGraphQLClient("localhost", port_number=3000) 
    #if for some unthinkable reason you are not running this locally, change this

    reload_info: ReloadRepositoryLocationInfo = client.reload_repository_location('definitions')
    #may need to change this if you get this code out and put it elsewhere

    if reload_info.status == ReloadRepositoryLocationStatus.SUCCESS:
        pass
    else:
        raise dg.Failure(
            "Repository location reload failed because of a "
            f"{reload_info.failure_type} error: {reload_info.message}"
        )
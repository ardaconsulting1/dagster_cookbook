import dagster as dg

@dg.asset_sensor(asset_key=dg.AssetKey("adjust_file"), job_name = "reload_repo_job")
def reload_on_file_adjustment():
    return dg.RunRequest()
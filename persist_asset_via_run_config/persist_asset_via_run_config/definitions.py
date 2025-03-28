from dagster import Definitions, load_assets_from_modules

from persist_asset_via_run_config import assets  # noqa: TID252
from persist_asset_via_run_config.jobs import reload_repo_job
from persist_asset_via_run_config.sensors import reload_on_file_adjustment

all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=all_assets,
    jobs=[reload_repo_job],
    sensors=[reload_on_file_adjustment]
)

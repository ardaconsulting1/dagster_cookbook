from dagster import Definitions, load_assets_from_modules

from persist_asset_via_run_config import assets  # noqa: TID252

all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=all_assets,
)

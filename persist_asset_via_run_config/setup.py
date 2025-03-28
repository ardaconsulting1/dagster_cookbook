from setuptools import find_packages, setup

setup(
    name="persist_asset_via_run_config",
    packages=find_packages(exclude=["persist_asset_via_run_config_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)

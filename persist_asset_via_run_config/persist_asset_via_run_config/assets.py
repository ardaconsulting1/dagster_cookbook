import dagster as dg
import yaml

# This is the operation that makes all of this necessary
# If you don't reload dagster, this never gets rerun and won't reflect
# Updates you make to it in the run config
with open('list_of_tables.yaml','r') as file:
    tables = yaml.safe_load(file)

# Inherits from the Config class in dagster
class TableEditingConfig(dg.Config):
    editable_file: dict = tables


@dg.asset(description='Static file to be updated.')
def adjust_file(config:TableEditingConfig):

    #The changes are made in the Dagster UI
    #You need to hit "Open launchpad"
    with open('list_of_tables.yaml','w') as file:
        yaml.safe_dump(config.editable_file,file)

    return dg.MaterializedResult(
        metadata={
            'tables':dg.MetadataValue.text(str(config.editable_file['tables']))
        }
    )

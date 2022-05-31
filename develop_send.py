import logging
import argparse
import apache_beam as beam
from apache_beam.io.gcp.internal.clients import bigquery
from apache_beam.options.pipeline_options import PipelineOptions
from develop_db import (
    return_database_values,
    produce_database_values, 
)
from config import BigQueryTable

def run(argv=None):
    produce_database_values()    
    pipeline_options = PipelineOptions(
        runner=argv.runner,
        project=argv.project,
        temp_location = f'gs://{argv.bucket}/temp',
        staging_location = f'gs://{argv.bucket}/staging',
        # template_location=f'gs://{argv.bucket}/templates/test.json',
        region=argv.region
    )
    with beam.Pipeline(options=pipeline_options) as pipeline:
        values_new = (
            pipeline
            | beam.Create(return_database_values())
        )
        values_new | beam.io.WriteToBigQuery(
        bigquery.TableReference(
            projectId=argv.project,
            datasetId=argv.dataset,
            tableId=argv.table
        ),
        schema=BigQueryTable.schema,
        method="STREAMING_INSERTS",
        create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
        write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--project',
        required=False,
        default=BigQueryTable.project_id,
        help="ID of the used project",
    )
    parser.add_argument(
        "--runner",
        required=False,
        default='DataflowRunner'
    )
    parser.add_argument(
        '--region',
        required=False,
        default='us-central1',
        help='region where to operate'
    )
    parser.add_argument(
        '--dataset',
        required=False,
        default=BigQueryTable.dataset,
        help='selected dataset values'
    )
    parser.add_argument(
        '--table',
        required=False,
        default=BigQueryTable.table,
        help='data table where to insert values'
    )
    parser.add_argument(
        '--bucket',
        default=BigQueryTable.bucket,
        help='bucket of the user'
    )
    args, beam_args = parser.parse_known_args()
    logging.getLogger().setLevel(logging.INFO)
    run(args)
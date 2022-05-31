import os
from dotenv import load_dotenv


load_dotenv()

class DataBase:
    tablename_test = 'table_test'
    host = os.getenv('HOST', '0.0.0.0')
    user = os.getenv('USER_DB', 'postgres')
    port = int(os.getenv('PORT', 5432))
    data = os.getenv('DATABASE', 'db')
    pawd = os.getenv("PASSWORD", 'postgres')

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(
    os.getcwd(), 
    os.getenv('JSON_NAME')
)

df_path = os.path.join(
    os.getcwd(), 
    'storage', 
    'df_vote.csv'
)

class BigQueryTable:
    project_id = os.getenv('PROJECT_ID', '')
    dataset = os.getenv('DATASET', '')
    table = os.getenv('TABLE', '')
    bucket = os.getenv('BUCKET', '')
    schema = {
        'fields': [
            {'name': 'sex', 'type': 'STRING', 'mode': 'NULLABLE'},
            {'name': 'year', 'type': 'STRING', 'mode': 'NULLABLE'},
            {'name': 'day', 'type': 'STRING', 'mode': 'NULLABLE'},
            {'name': 'birthday', 'type': 'STRING', 'mode': 'NULLABLE'},
            {'name': 'surname', 'type': 'STRING', 'mode': 'NULLABLE'},
            {'name': 'street', 'type': 'STRING', 'mode': 'NULLABLE'},
            {'name': 'state', 'type': 'STRING', 'mode': 'NULLABLE'},
            {'name': 'age', 'type': 'STRING', 'mode': 'NULLABLE'},
            {'name': 'id', 'type': 'STRING', 'mode': 'NULLABLE'},
            {'name': 'month', 'type': 'STRING', 'mode': 'NULLABLE'},
            {'name': 'street_number', 'type': 'STRING', 'mode': 'NULLABLE'},
            {'name': 'city', 'type': 'STRING', 'mode': 'NULLABLE'},
            {'name': 'state_voted', 'type': 'STRING', 'mode': 'NULLABLE'},
            {'name': 'name', 'type': 'STRING', 'mode': 'NULLABLE'},
        ]
    }
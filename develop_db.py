import pandas as pd
from pprint import pprint
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
)
from config import DataBase, df_path


Base = declarative_base()

class TableTest(Base):
    __tablename__ = DataBase.tablename_test
    id = Column(Integer, primary_key=True)
    sex = Column(String, default='')
    age = Column(String, default='')
    year = Column(String, default='')
    month = Column(String, default='')
    day = Column(String, default='')
    street_number = Column(String, default='')
    birthday = Column(String, default='')
    surname = Column(String, default='')
    city = Column(String, default='')
    street = Column(String, default='')
    state_voted = Column(String, default='')
    state = Column(String, default='')
    name = Column(String, default='')

class DatabaseDevelop:
    """
    class which is dedicated to develop the database connection and values
    """
    def __init__(self) -> None:
        self.engine = create_engine(
            f'postgresql://{DataBase.data}:{DataBase.pawd}@{DataBase.host}/{DataBase.user}'
        )
        self.create_db()
        self.session = self.produce_session()

    def create_db(self):
        """
        Method which is dedicated to create databse values of this
        Input:  None
        Output: we created the selected values for the database values
        """
        try:
            Base.metadata.create_all(self.engine)
        except Exception as e:
            print(f"We faced problems with Base: {e}")

    def produce_session(self) -> object:
        """
        Method which is dedicated to create the session values for the database
        Input:  None
        Output: we create session for creation
        """
        Session = sessionmaker(bind=self.engine)
        return Session()

    def develop_database(self) -> None:
        """
        Method which is dedicated to develop values of the postgresql values
        Input:  None
        Output: we developed the 
        """
        if self.session.query(TableTest.id).count():
            return
        self.session.add_all(
            [
                TableTest(
                    sex=elem.get('Sex', ''),
                    age=elem.get('Age', ''),
                    year=elem.get('Year', ''),
                    month=elem.get('Sex', ''),
                    day=elem.get('Sex', ''),
                    street_number=elem.get('Street_Number', ''),
                    birthday=elem.get('Birthday', ''),
                    surname=elem.get('Surname', ''),
                    city=elem.get('City', ''),
                    street=elem.get('Street', ''),
                    state_voted=elem.get('State_Voted', ''),
                    state=elem.get('State', ''),
                    name=elem.get('Name', '')
                )
                for elem in pd.read_csv(df_path).to_dict('records')
            ]
        )
        self.session.commit()
    
    def develop_database_values(self) -> list:
        """
        Method which is dedicated to develop values which we would get
        Input:  None
        Output: list of the dictionary values to the postgresql
        """
        def test_function(x) -> dict:
            x.pop('_sa_instance_state')
            return x
        return [test_function(f.__dict__) for f in self.session.query(TableTest).all()]
        
def produce_database_values():
    db = DatabaseDevelop()
    db.develop_database()

def return_database_values():
    db = DatabaseDevelop()
    return db.develop_database_values()
    

if __name__ == '__main__':
    produce_database_values()
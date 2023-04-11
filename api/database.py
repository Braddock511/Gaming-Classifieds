from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from os import environ

user = environ.get("POSTGRES_USER")
password = environ.get("POSTGRES_PASSWORD")
host = environ.get("POSTGRES_HOST")
port = environ.get("POSTGRES_PORT")
db = environ.get("POSTGRES_DB")

if not user:
    user = "postgres"
    password = "admin"
    host = "localhost"
    port = "5432"
    db = "postgres"

SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{db}"

def create_user(login: str, password: str, email: str):
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    Base = declarative_base()

    Session = sessionmaker(bind=engine)
    session = Session()

    class Users(Base):
        __tablename__ = "users"

        id = Column(Integer, primary_key=True, index=True, autoincrement=True)
        login = Column(String)
        password = Column(String)
        email = Column(String)
        
    # Create the table if it does not exist
    Base.metadata.create_all(engine)

    data_to_insert = {
        "login": login,
        "password": password,
        "email": email
    }       

    data_image_instance = Users(**data_to_insert)
    session.add(data_image_instance)
    session.commit()
    session.close()

def check_user(login, password):
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    Base = declarative_base()

    Session = sessionmaker(bind=engine)
    session = Session()

    class Users(Base):
        __tablename__ = "users"

        id = Column(Integer, primary_key=True, index=True, autoincrement=True)
        login = Column(String)
        password = Column(String)
        email = Column(String)
        
    # Create the table if it does not exist
    Base.metadata.create_all(engine)
    
    # Query the Users table for a matching user
    user = session.query(Users).filter_by(login=login, password=password).first()

    return user is not None
    
from fastapi.testclient import TestClient
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from api.main import app
import api.database as db 

Base = declarative_base()

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    login = Column(String)
    password = Column(String)
    email = Column(String)

class TestUserRegistration:
    SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:admin@localhost:5432/postgres"

    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    def test_register_user(self):
        client = TestClient(app)

        data = {
            "login": "testuser",
            "password": "password123",
            "email": "testuser@example.com"
        }
        response = client.post("/register", json=data)
        
        assert response.json() == {"result": 200}

    def test_register_user_already_exist(self):
        client = TestClient(app)

        data = {
            "login": "testuser",
            "password": "password123",
            "email": "testuser@example.com"
        }
        client.post("/register", json=data)
        response = client.post("/register", json=data)
        
        assert response.json() == {"result": 401}

    def test_create_user(self):
        db.create_user("testuser", "password123", "testuser@example.com")
        user = self.session.query(Users).filter_by(login="testuser").first()
        
        assert user.login == "testuser"
        assert user.email == "testuser@example.com"

    def test_check_user_exist(self):
        db.create_user("testuser", "password123", "testuser@example.com")
        result = db.check_user("testuser", "password123")

        assert result == True
    
    def test_check_user_exist(self):
        result = db.check_user("nbvcxz", "bvcxz")

        assert result == False

class TestGames:
    SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:admin@localhost:5432/postgres"

    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    def test_get_games(self):
        games = db.get_games()

        assert games[0].title == "Minecraft"

    def test_listing_game(self):
        game = {
            "image_url": "https://test.png",
            "title": "Test",
            "description": "test test test",
            "genre": "RPG",
            "platform": "PC",
            "price": 99.99
        }

        db.listing_game(game)
        games = db.get_games()

        assert games[-1].title == "Test"

    def test_delete_game(self):
        db.delete_game(3)

    def test_get_game(self):
        client = TestClient(app)

        response = client.get("/get-game?game_id=1")

        assert response.json()['output'][0]['title'] == "Minecraft"

class TestPayment:
    SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:admin@localhost:5432/postgres"

    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    def test_add_payment(self):
        payment = {
            "email": "test@test",
            "name": "Test",
            "phone": "111111111",
            "city": "Warsaw",
            "address": "3 Maja",
            "buildingNumber": "43",
            "apartmentNumber": "",
            "instructions": "",
            "products_id": [3, 4],
            "price": 99.99
        }

        db.add_payment(payment)
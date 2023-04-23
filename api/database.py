from sqlalchemy import Column, String, Integer, Float, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
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

# Create database
SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{db}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    login = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)
    games = relationship("Games", back_populates="users")

class Games(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    users = relationship("Users", back_populates="games")
    image_url = Column(String, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    platform = Column(String, nullable=False)
    price = Column(Float, nullable=False)

class Payments(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String)
    name = Column(String)
    phone = Column(String)
    city = Column(String)
    postalCode = Column(String)
    address = Column(String)
    buildingNumber = Column(String)
    apartmentNumber = Column(String)
    instructions = Column(String)
    products_id = Column(String)
    price = Column(Float)

class ImageCredentials(Base):
    __tablename__ = "image_credentials"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    api_imagekit_id = Column(String)
    api_imagekit_secret = Column(String)
    api_imagekit_endpoint = Column(String)

Base.metadata.create_all(engine)

# Insert default data
Session = sessionmaker(bind=engine)

credentials = {
    "api_imagekit_id": environ.get("API_IMAGEKIT_ID"),
    "api_imagekit_secret": environ.get("API_IMAGEKIT_SECRET"),
    "api_imagekit_endpoint": environ.get("API_IMAGEKIT_ENDPOINT"),
}

image_urls = ['https://ik.imagekit.io/ztf601lz0/minecraft.png?updatedAt=1681495106029', 'https://ik.imagekit.io/ztf601lz0/wiedzmin.jpg?updatedAt=1681495105935', 'https://ik.imagekit.io/ztf601lz0/reddead.jpg?updatedAt=1681495105811', 'https://ik.imagekit.io/ztf601lz0/ufc.jpg?updatedAt=1681495105811', 'https://ik.imagekit.io/ztf601lz0/max_payne.png?updatedAt=1681495105439', 'https://ik.imagekit.io/ztf601lz0/lego1.jpg?updatedAt=1681495105432', 'https://ik.imagekit.io/ztf601lz0/hitman.png?updatedAt=1681495104154', 'https://ik.imagekit.io/ztf601lz0/fifa23.png?updatedAt=1681495104089', 'https://ik.imagekit.io/ztf601lz0/GTAiv.jpg?updatedAt=1681495104014', 'https://ik.imagekit.io/ztf601lz0/cajberpank.png?updatedAt=1681495104006', 'https://ik.imagekit.io/ztf601lz0/hary_piter.png?updatedAt=1681495104000', 'https://ik.imagekit.io/ztf601lz0/codbo3.png?updatedAt=1681495103962', 'https://ik.imagekit.io/ztf601lz0/fallout.jpg?updatedAt=1681495103916', 'https://ik.imagekit.io/ztf601lz0/gtaV.png?updatedAt=1681495103904', 'https://ik.imagekit.io/ztf601lz0/agent.png?updatedAt=1681495103640', 'https://ik.imagekit.io/ztf601lz0/hawk.jpg?updatedAt=1681495103597']
titles = ['Minecraft', 'Witcher 3', 'Red Dead Redemption 2', 'UFC 3', 'Max Payne 3', 'Lego Star Wars', 'Hitman III', 'Fifa 23', 'GTA IV', 'Cyberpunk 2077', 'Hogwarts Legacy', 'Call of Duty Black Ops III', 'Fallout 4', 'GTA V', 'Splinter Cell Agent', 'Tony Hawk 3']
descriptions =  ['Minecraft: A sandbox game where players can explore, build and survive in a blocky, pixelated world.','Witcher 3: An action role-playing game set in a vast open world, following the story of the monster hunter Geralt of Rivia.','Red Dead Redemption 2: A western-themed action-adventure game where players assume the role of an outlaw in a vast, detailed open-world environment.','UFC 3: A mixed martial arts simulation game that allows players to experience the intensity and excitement of UFC fights.','Max Payne 3: A third-person shooter game where players take control of the titular character as he navigates through a world of crime and corruption.','Lego Star Wars: A family-friendly action-adventure game that retells the Star Wars saga in a humorous and whimsical Lego style.','Hitman III: A stealth-based game where players take on the role of Agent 47, a professional assassin tasked with eliminating various targets around the world.','Fifa 23: A sports simulation game that allows players to experience the excitement of professional soccer matches.','GTA IV: A gritty open-world action-adventure game set in a fictionalized version of New York City.','Cyberpunk 2077: An open-world action-adventure game set in a dystopian future where players assume the role of a mercenary in a world of advanced technology.','Hogwarts Legacy: A role-playing game set in the Wizarding World of Harry Potter, where players can attend Hogwarts School of Witchcraft and Wizardry and explore its magical secrets.','Call of Duty Black Ops III: A first-person shooter game where players take on the role of a special forces operative in a near-future setting.','Fallout 4: A post-apocalyptic action role-playing game where players must navigate a world ravaged by nuclear war and make choices that affect the game outcome.','GTA V: An open-world action-adventure game set in a fictionalized version of Los Angeles.','Splinter Cell Agent: A stealth-based game where players take on the role of Sam Fisher, a highly trained covert operative working for the NSA.','Tony Hawk 3: A skateboarding simulation game that allows players to perform tricks and stunts in a variety of locations around the world.']
genres = ['Survival', 'RPG', 'Adventure', 'Sports', 'Action', 'Adventure', 'Action', 'Sports', 'Action', 'Action', 'Adventure', 'Action', 'RPG', 'Action', 'Action', 'Sports']
platforms = ['PS4', 'Xbox One', 'Xbox One', 'Xbox 360', 'PC', 'PS5', 'PS4', 'PS4', 'PC', 'Xbox One', 'PS5', 'Xbox One', 'Xbox One', 'PS4', 'Xbox 360', 'PC']
prices = [23.99, 16.99, 34.99, 12.99, 12.99, 46.99, 45.99, 46.99, 27.99, 34.99, 56.99, 29.99, 12.99, 12.99, 12.99]


with Session() as session:
    exist = True if session.query(Users).filter_by(login='admin').first() is not None else False

    if not exist:
        admin = Users(id=0, login='admin', password='admin', email='admin@admin.com')       
        session.add(admin)
        session.commit()

    if session.query(Games).count() == 0:
        for i in range(15):
            game = Games(
                user_id=0,
                image_url=image_urls[i],
                title=titles[i],
                description=descriptions[i],
                genre=genres[i],
                platform=platforms[i],
                price=prices[i])
            session.add(game)

    credentials_data = ImageCredentials(**credentials)
    session.add(credentials_data)
        
    session.commit()

# Database scripts

def create_user(login: str, password: str, email: str) -> bool:
    Session = sessionmaker(bind=engine)

    with Session() as session:
        exist = True if session.query(Users).filter_by(login=login).first() is not None else False

        if not exist:
            user_data = {
                "login": login,
                "password": password,
                "email": email
            }       

            user = Users(**user_data)
            session.add(user)
            session.commit()

            return True
        else:
            return False

def check_user(login, password) -> bool:
    Session = sessionmaker(bind=engine)

    with Session() as session:
        # Query the Users table for a matching user
        user = session.query(Users).filter_by(login=login, password=password).first()

    return user is not None

def get_games() -> list:
    Session = sessionmaker(bind=engine)

    with Session() as session:
        games = session.query(Games).all()

    return games

def listing_game(game: dict):
    Session = sessionmaker(bind=engine)

    with Session() as session:
        new_game = Games(**game)
        session.add(new_game)
        session.commit()

def delete_game(game_id: str):
    Session = sessionmaker(bind=engine)
    
    with Session() as session:
        game = session.query(Games).get(game_id)
        session.delete(game)
        session.commit()

def get_credentials() -> dict:
    Session = sessionmaker(bind=engine)
    
    with Session() as session:
        # Get credentials from database
        row = session.query(ImageCredentials).order_by(ImageCredentials.id.desc()).limit(1).first()
        credentials = row.__dict__
        del credentials['_sa_instance_state']

    return credentials

def add_payment(payment: dict):
        Session = sessionmaker(bind=engine)
    
        with Session() as session:
            new_payment = Payments(**payment)
            session.add(new_payment)
            session.commit()


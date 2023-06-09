from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from typing import Optional
from json import loads
import database as db
from imageKit import upload_file_imageKit

app = FastAPI()

# CORS middleware to allow requests from a specific origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/register")
async def register_user(request: Request):
    try:
        response = loads((await request.body()).decode('utf-8'))
        login = response['login']
        password = response['password']
        email = response['email']

        result = db.create_user(login, password, email)
        if result:
            return {"status": 200, "output": login}
        
        return {"status": 401}
    except Exception as e:
        return {"error": f"Exception in register_user: {str(e)}"}
    
@app.post("/login")
async def login(request: Request):
    try:
        response = loads((await request.body()).decode('utf-8'))
        login = response['login']
        password = response['password']

        result = db.check_user(login, password)

        if result:
            return {"status": 200}
        return {"status": 404}
    except Exception as e:
        return {"error": f"Exception in login: {str(e)}"}
    
@app.get("/get-games")
async def get_games(genre: Optional[str] = None, platform: Optional[str] = None):
    try:
        games = db.get_games()

        if genre:
            if genre == "All":
                pass
            else:
                games = [game for game in games if game.genre == genre]
        if platform:
            if platform == "All":
                pass
            else:
                games = [game for game in games if game.platform == platform]

        return {"status": 200, "output": games}
    
    except Exception as e:
        return {"error": f"Exception in get_games: {str(e)}"}

@app.get("/get-game")
async def get_game(game_id: Optional[str] = None):
    try:
        games = db.get_games()
        
        if game_id:
            game_product = [game for game in games if int(game.id) == int(game_id)]

            return {"status": 200, "output": game_product}
        return {"status": 404, "output": game_id}
    
    except Exception as e:
        return {"error": f"Exception in get_game: {str(e)}"}

@app.post("/listing-game")
async def get_game(request: Request):
    try:
        response = loads((await request.body()).decode('utf-8'))
        new_game = response['newGame']
        image = new_game['image']
        image_url = upload_file_imageKit(image)
        user_id = db.get_user_id(response['userLogin'])

        game = {
            "user_id": user_id,
            "title": new_game['title'],
            "description": new_game['description'],
            "genre":  new_game['genre'],
            "platform": new_game['platform'],
            "price": new_game['price'],
            "image_url": image_url['url']
        }

        db.create_game(game)

        return {"status": 200, "output": game}
    
    except Exception as e:
        return {"error": f"Exception in get_game: {str(e)}"}
    
@app.post("/order")
async def order(request: Request):
    try:
        response = loads((await request.body()).decode('utf-8'))
        order = response['order']
        db.add_order(order)

        for game_id in order['products_id']:
            db.delete_game(game_id)

        return {"status": 200, "output": order}
    
    except Exception as e:
        return {"error": f"Exception in order: {str(e)}"}
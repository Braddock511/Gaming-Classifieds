from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from json import loads
from api.database import create_user, check_user

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

        create_user(login, password, email)

        return {"result": 200}
    except Exception as e:
        return {"error": f"Exception in register_user: {str(e)}"}
    
@app.post("/login")
async def login(request: Request):
    try:
        response = loads((await request.body()).decode('utf-8'))
        login = response['login']
        password = response['password']

        result = check_user(login, password)

        if result:
            return {"result": 200}
        return {"result": 404}
    except Exception as e:
        return {"error": f"Exception in login: {str(e)}"}
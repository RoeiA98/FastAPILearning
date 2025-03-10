from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return "Welcome to the homepage!"


@app.get('/about')
def about():
    return {
        "developer": {
            "name": "Roei Itzhak"
        }
    }
    

@app.get('/{user_id}')
def get_user_by_id(user_id: int):
    return f'Hello user {user_id}!'
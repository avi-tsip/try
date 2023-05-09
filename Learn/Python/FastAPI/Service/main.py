import fastapi
import uvicorn
from models.movie_model import MovieModel
import db_service

app = fastapi.FastAPI()

@app.get('/')
def index():
    return {
        "message": "hello world!",
        "usage": "call /api/movie/{title} to use the API"
    }

@app.get('/api/movie/{title}', response_model=MovieModel)
async def get_movie(title: str):
    movie = await db_service.get_movie(title)
    if not movie:
        raise fastapi.HTTPException(status_code=404)
    return movie.dict()

if __name__ == '__main__':
    uvicorn.run(app)
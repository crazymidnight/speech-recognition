from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    """Index page route."""
    return {'message': 'Hello World'}

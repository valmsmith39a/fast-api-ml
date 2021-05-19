from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def main():
	return {'message': 'Welcome to The Cheese Shop'}

@app.get('/{name}')
def hello_cheese(name : str):
	return {'message': f'Welcome to the Cheese Shop!, {name}'}

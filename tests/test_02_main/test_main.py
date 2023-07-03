from fastapi import FastAPI

from fastapi_cors.main import FastAPI_Cors

def test_app() -> None:
    
    app = FastAPI()
    
    app = FastAPI_Cors(app=app)
    
    assert isinstance(app, FastAPI)

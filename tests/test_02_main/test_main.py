from fastapi import FastAPI
from fastapi.testclient import TestClient

from fastapi_cors.main import CORS

def test_app_type() -> None:
    
    app = FastAPI()
    
    CORS(app=app)
    
    assert isinstance(app, FastAPI)

def test_health_check() -> None:
    
    app = FastAPI()
    
    CORS(app=app)
    
    client = TestClient(app)

    response = client.get("/health")
    assert response.status_code == 200
    assert list(response.json().keys()) == ["status", "details", "env"]


def test_health_check_disabled() -> None:
    
    app = FastAPI()
    
    CORS(app=app, include_health_check=False)
    client = TestClient(app)
    

    response = client.get("/health")
    assert response.status_code == 404



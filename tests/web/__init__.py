from fastapi.testclient import TestClient

from api.web import app


client = TestClient(app)

import pytest
from company import app
from company.core.views import core

def test_core():
    response = app.test_client().get('/')
    assert response.status_code == 200

def test_info():
    response = app.test_client().get("/info")
    assert response.status_code == 200

def test_test():
    response = app.test_client().get("/notfound")
    assert response.status_code == 200


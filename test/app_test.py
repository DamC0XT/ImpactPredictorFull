import os
import tempfile

import pytest

from app import app


@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])

def test_Index(client):

    response = client.get('/')
    assert response.data
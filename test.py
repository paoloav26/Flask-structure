import unittest
from flask_sqlalchemy import SQLAlchemy

from server import create_app
from models import setup_db
import json

class TestCaseTodoApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = ''
        self.database_path = 'postgresql+psycopg2://{}@{}/{}'.format('postgres:1234', 'localhost:5432', self.database_name)

        setup_db(self.app, self.database_path)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()
    
    def test_sample(self):
        # pick one
        res = self.client().get('/<your_endpoint>')
        res = self.client().post('/<your_endpoint>', json={})
        res = self.client().patch('/<your_endpoint>', json={})
        res = self.client().delete('/<your_endpoint>')
        
        # deserialize data
        data = json.loads(res.data)
        
        # testing one by one
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')
        self.assertTrue(len(data['elements']))

    def tearDown(self):
        pass

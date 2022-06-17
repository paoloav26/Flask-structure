from flask_sqlalchemy import SQLAlchemy

user = "user:password"
conection = "localhost:5432"
data_base_name = "dbname"
database_path = f"postgresql+psycopg2://{user}@{conection}/{data_base_name}"

db=SQLAlchemy()

def setup_db(app,database_path=database_path):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    db.create_all()

# models
class BaseModel(db.Model):
    __tablename__ = 'tablename'
    # attributes
    id = db.Column(db.Integer, primary_key=True)

    # methods
    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()

    def update(self):
        try:
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
        

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
        

    def format(self):
        return {
            'id': self.id
        }

    def __repr__(self):
        return f'Model: id={self.id}'

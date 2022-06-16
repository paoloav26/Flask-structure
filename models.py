from flask_sqlalchemy import SQLAlchemy

user="user:password"
conection="localhost:5432"
data_base_name="dbname"
database_path=f"postgresql+psycopg2://{user}@{conection}/{data_base_name}"

db=SQLAlchemy()

def setup_db(app,database_path=database_path):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    db.create_all()

#aca ya van los modelos

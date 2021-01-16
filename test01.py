from re import U
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    email = db.Column(db.String, primary_key=True, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

db.create_all()
archie = User(email = "archie.andrews@email.com", password = "football4life")
veronica = User(email = "veronica.lodge@email.com", password = "fashiondiva")

db.session.add(veronica)
db.session.add(archie)

try:
    db.session.commit()
except Exception as e:
    db.session.rollback()

print("Metodo all(): ", User.query.all())
print("Método first(): ", User.query.first())
print("-"*50)

# recupera valor de la base de datos mediante un argumento
user = User.query.get("veronica.lodge@email.com")
print(user)
print(user.email)
print(user.password)

print("-"*50)

user = User.query.filter_by(password='football4life')
print(user) # Objeto base Query
print('*'*20)

## Agrega el primer resultado de la consulta
user = User.query.filter_by(password='football4life').first()
print(user)
print(user.email)
print(user.password)


# Uso del método filter()
## user_bad = User.query.filter(email == "veronica.lodge@email.com")
## user_ok = User.query.filter(User.email == "veronica.lodge@email.com")

user = User.query.filter(User.email == "veronica.lodge@email.com")
print("a:", user)
print('*'*20)

# Agrega el primer método para recuperar el primer resultado
user = User.query.filter(User.email == "veronica.lodge@email.com").first()
print("b: ",user)
print('*'*20)

# Consulta con varias expresiones
user = User.query.filter(User.email ==  "archie.andrews@email.com", User.password.contains("anonpass"))
print("c: ",user)
print('*'*20)
print(user.first())



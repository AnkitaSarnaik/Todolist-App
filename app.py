
import logging
from flask import Flask
from flask_graphql import GraphQLView
from flask_oidc import OpenIDConnect
from keycloak import keycloakOpenID

from flask_stripe import Stripe
from models import db
from schema import schema

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db',
app.config['SECRET_KEY'] = 'unhkxHEPkhMMdYQWMzt53gD2QJ4sHgC7'
app.config['KEYCLOAK_SERVER_URL'] = 'http://localhost:8080/admin/master/console/#/Todolist',
app.config['KEYCLOAK_REALM_NAME'] = 'Todolist',
app.config['KEYCLOAK_CLIENT_ID'] = 'ankita',
app.config['STRIPE_PUBLIC_KEY'] = 'pk_test_51ORxbiSE5gGr31tfZMLM2fNhUqB8EdhUlSa9R3m0F0AgAOPNZOVHkpAxcOgmWkLtubh4pjerJul1G4BEOf0grvux00PfxWSdeC',
app.config['STRIPE_SECRET_KEY'] = 'sk_test_51ORxbiSE5gGr31tfHHXALoaoxZdPyYT7ziyyioB5Jp0THE0FhUZ8Ro6XNpYt8MFOAH0BkpTZQnAAV2R6Qy2hJmCb00RiXEkhUQ'
keycloak = Keycloak(app)
stripe = Stripe(app)
db.init_app(app)

app.add_url_rule('/graphql', view_func=keycloak.graphql_view(schema=schema, graphiql=True))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    
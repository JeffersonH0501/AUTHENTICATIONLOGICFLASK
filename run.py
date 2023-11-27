from app import app, db
from app.models import Usuario

from flask_migrate import Migrate
migrate = Migrate(app, db)

if __name__ == '__main__':
    # app.run(debug=True)  # Comentamos esto, ya que usaremos el servidor de desarrollo de Flask
    db.create_all()
    app.run()

from app import app, db
from flask_migrate import Migrate

migrate = Migrate(app, db)

if __name__ == '__main__':
    # app.run(debug=True)
    db.create_all()
    app.run(host='0.0.0.0', port=8080, debug=True)

from exts import db
from flask import Flask
import config
from apps.cmdb import bp as cmdb_bp
from apps.common import bp as common_bp
from apps.front import bp as front_bp

app = Flask(__name__)
app.config.from_object(config)

app.register_blueprint(cmdb_bp)
app.register_blueprint(common_bp)
app.register_blueprint(front_bp)
db.init_app(app)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=82)
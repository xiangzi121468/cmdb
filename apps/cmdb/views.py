
from flask import Blueprint
from  flask  import render_template
from flask import Flask,views,url_for
bp = Blueprint('cmdb', __name__, url_prefix='/cmdb')

@bp.route('/')
def index():
    return 'cmdb index'
class LoginView(views.MethodView):
    def get(self):
        return render_template('cmdb/cmdb_login.html')

    def post(self):
        pass

bp.add_url_rule('/login/', view_func=LoginView.as_view('login'))

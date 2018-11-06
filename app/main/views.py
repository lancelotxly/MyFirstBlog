from flask import render_template, session, redirect, url_for
from .. import db
from ..models import User
from . import main
from .forms import NameForm

@main.route('/',methods=['GET','POST'])
def index():
    db.create_all()
    form = NameForm()
    if form.validate_on_submit():
        user = db.session.query(User).filter_by(username = form.name.data).first()
        if user is None:
            user = User(username = form.name.data)
            db.session.add()
            db.session.commit()
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('.index'))
    return render_template('index.html', form = form, name = session.get('name'), known = session.get('known'))
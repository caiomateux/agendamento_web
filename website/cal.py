from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .models import Event
from . import db
from sqlalchemy import exc

cal = Blueprint('cal', __name__)


@cal.route('/calendar')
@login_required
def calendar():
    all_events = Event.query.all()
    return render_template("calendar.base.html", events=all_events, user=current_user, calendar=calendar)


@cal.route('/add', methods=['POST'])
@login_required
def add():
    if request.method == "POST":
        title = request.form['title']
        start = request.form['start']
        end = request.form['end']
        info = request.form['info']

        my_events = Event(title=title, start=start, end=end, info=info, user_id=current_user.id)

        try:
            db.session.add(my_events)
            return db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()

    return redirect(url_for('cal.calendar'))

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import Event
from . import db
from sqlalchemy import exc

cal = Blueprint('cal', __name__)



@cal.route('/calendar')
@login_required
def calendar():
    all_events = Event.query.all()
    return render_template("calendar.base.html", my_events=all_events, user=current_user, calendar=calendar)

@cal.route('/add', methods=['GET','POST'])
@login_required
def add():
    if request.method == "POST":
        title = request.form['title']
        start = request.form['start']
        end_event = request.form['end_event']
        info = request.form['info']

        my_events = Event(title=title, start=start, end_event=end_event, info=info, user_id=current_user.id)

        db.session.add(my_events)
        db.session.commit()
    return redirect(url_for('cal.calendar'))


@cal.route('/update/', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        my_events = Event.query.get(request.form.get('id'))

        my_events.title = request.form['title']
        my_events.start = request.form['start']
        my_events.end_event = request.form['end_event']
        my_events.info = request.form['info']

        db.session.flush()
        db.session.commit()
        flash("Agendamento atualizado")

        return redirect(url_for('cal.calendar'))


@cal.route('/delete', methods=['GET', 'POST'])
def delete(id):
    my_events = Event.query.get(id)
    db.session.delete(my_events)
    db.session.flush()
    db.session.commit()
    flash("Evento apagado")

    return redirect(url_for('cal.calendar'))


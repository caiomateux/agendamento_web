from flask import Blueprint, render_template, request
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


cal = Blueprint('cal', __name__)

events = [{'title' : 'TestEvent',
        'start' : '2021-08-24',
        'end' : '',
        'info' : ''
    },
    {
        'title' : 'TestEvent',
        'start' : '2021-08-24',
        'end' : '2021-08-25',
        'info' : 'hahaha'
    }
    ]
@cal.route('/calendar')
@login_required
def calendar():
    return render_template("calendar.base.html", User=current_user)


@cal.route('/add', methods=['GET','POST'])
def add():
    if request.method == "POST":
        title = request.form['title']
        start = request.form['start']
        end = request.form['end']
        info = request.form['info']
        if end == '':
            end=start
        events.append({
            'title' : title,
            'start' : start,
            'end' : end,
            'info' : info
        },
        )

    return render_template("add.html")
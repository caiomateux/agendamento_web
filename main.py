#pip3 install flask
#pip3 install flask-sqlalchemy
#pip3 install flask-logingit remote add origin https://github.com/caiomateux/agendamento_web.git

from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run()
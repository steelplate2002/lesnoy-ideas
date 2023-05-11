from project import db, create_app, models

with create_app().app_context():
    db.drop_all()
    db.create_all()

    guest = models.Role(code='guest', name='Гость', level=-1)
    part = models.Role(code='part', name='Житель', level=10)
    manager = models.Role(code='manager', name='Член правления', level=50)
    admin = models.Role(code='admin', name='Администратор', level=100)

    db.session.add(guest)
    db.session.add(part)
    db.session.add(manager)
    db.session.add(admin)

    db.session.commit()
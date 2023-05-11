from project import db, create_app, models

with create_app().app_context():
    db.drop_all()
    db.create_all()

    guest = models.Role(code='guest', name='Гость', level=-1)
    part = models.Role(code='part', name='Житель', level=11)
    manager = models.Role(code='manager', name='Член правления', level=51)
    admin = models.Role(code='admin', name='Администратор', level=101)

    state_idea = models.Project_state(level=0,name='Идея')
    state_indevelopment = models.Project_state(level=5,name='В проработке')
    state_inprogress = models.Project_state(level=10,name='На реализации')
    state_done = models.Project_state(level=15,name='Реализовано')
    state_arch = models.Project_state(level=20,name='Архив')

    g2_like = models.Like(code='++', icon='fa-regular fa-face-grin-stars', wieght=2)
    g1_like = models.Like(code='+', icon='fa-regular fa-face-grin', wieght=1)
    b1_like = models.Like(code='-', icon='fa-regular fa-face-rolling-eyes', wieght=-1)
    b2_like = models.Like(code='--', icon='fa-regular fa-face-angry', wieght=-2)

    db.session.add(state_idea)
    db.session.add(state_indevelopment)
    db.session.add(state_inprogress)
    db.session.add(state_done)
    db.session.add(state_arch)
    
    db.session.add(guest)
    db.session.add(part)
    db.session.add(manager)
    db.session.add(admin)

    db.session.add(g2_like)
    db.session.add(g1_like)
    db.session.add(b1_like)
    db.session.add(b2_like)

    db.session.commit()

    db.session.close()
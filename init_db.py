from project import db, create_app, models
from datetime import datetime
from werkzeug.security import generate_password_hash

with create_app().app_context():
    db.drop_all()
    db.create_all()

    guest = models.Role(code='guest', name='Гость', level=-1)
    part = models.Role(code='part', name='Житель', level=11)
    manager = models.Role(code='manager', name='Член правления', level=51)
    admin = models.Role(code='admin', name='Администратор', level=101)

    state_idea = models.Project_state(level=0,name='Идея',icon='fa-regular fa-lightbulb')
    state_indevelopment = models.Project_state(level=5,name='В проработке',icon='fa-solid fa-pen-ruler')
    state_inprogress = models.Project_state(level=10,name='На реализации',icon='fa-solid fa-hammer')
    state_done = models.Project_state(level=15,name='Реализовано',icon='fa-solid fa-circle-check')
    state_arch = models.Project_state(level=20,name='Архив',icon='fa-solid fa-box-archive')

    g2_like = models.Like(code='++', icon='fa-regular fa-face-grin-stars', descr='Супер!', wieght=2, color='success')
    g1_like = models.Like(code='+', icon='fa-regular fa-face-grin', descr='Звучит неплохо', wieght=1, color='primary')
    b1_like = models.Like(code='-', icon='fa-regular fa-face-rolling-eyes', descr='Сомнительно...', wieght=-1, color='warning')
    b2_like = models.Like(code='--', icon='fa-regular fa-face-angry', descr='Ну уж нет!', wieght=-2, color='danger')

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

    land = models.Land(number=1)
    user = models.User(email='qwe@qwe', password=generate_password_hash('qwe', method='scrypt'), land=land, name='qwe', role=guest)
    project = models.Project(title='Сделать хорошо',
                             description='Счастье для всех, даром, и пусть никто не уйдет обиженным!',
                             image='https://cdn-icons-png.flaticon.com/512/6213/6213355.png',
                             state=state_idea,
                             author=user,
                             modifyer=user,
                             created_at=datetime.now(),
                             modify_at=datetime.now()
                             )
    project2 = models.Project(title='Сделать хорошо 2',
                             description='Сделать, чтобы всё было ещё лучше',
                             image='https://cdn-icons-png.flaticon.com/512/5232/5232319.png',
                             state=state_idea,
                             author=user,
                             modifyer=user,
                             created_at=datetime.now(),
                             modify_at=datetime.now()
                             )

    db.session.add(land)
    db.session.add(user)
    db.session.add(project)
    db.session.add(project2)

    db.session.commit()
    
    db.session.close()
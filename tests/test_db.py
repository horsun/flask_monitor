from monitor import db
from monitor.apps.monitor_app.models import User


def add(username='test2', email='test@test.com'):
    """
    db add data
    """
    new_user = User(username=username,
                    password='test1232',
                    email=email)
    db.session.add(new_user, new_user)
    db.session.commit()


def all():
    """
    db get all
    """
    users = User.query.all()
    print(users)


def find_by():
    """
    filter_by data  精确查询
    """
    me = User.query.filter_by(username='test2').first()  # all() is ok
    print(me)


def find():
    """
    filter  startwith("")
            endwith("")
            not_(User.username=='test')
            and(User.username=='test')
    """
    me = User.query.filter(User.username.startswith('test')).all()
    print(me)


def update():
    """
    update data
    """
    me = User.query.filter_by(username='test2').first()
    print(me)
    me.username = 'update_test2'
    db.session.commit()
    print(me)


def delete():
    """
    delete data
    """
    me = User.query.filter_by(username='test1').first()
    print('now delete ' + str(me))
    db.session.delete(me)
    db.session.commit()
    print(User.query.all())


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    add(username='test1', email='test1@test.com')
    add(username='test2', email='test2@test.com')
    add(username='test3', email='test3@test.com')
    print('获取所有')
    all()
    print('-------------------------------------------------------')
    print('精确查询  username is test2')
    find_by()
    print('-------------------------------------------------------')
    print('模糊查询  username startwith test')
    find()
    print('-------------------------------------------------------')
    print('数据更新  username is test2 >>>>> update_test2')
    update()
    print('-------------------------------------------------------')
    print('数据删除 delete test1 ')
    delete()

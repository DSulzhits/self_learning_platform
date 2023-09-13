from users.models import User, UserRoles


def get_admin_user():
    user = User.objects.create(
        email='tester@test1.com',
        role=UserRoles.MODERATOR,
        is_active=True,
        is_superuser=True,
        is_staff=True
    )
    user.set_password('qwerty')
    user.save()
    return user


def get_member_user():
    user = User.objects.create(
        email='tester_member@test1.com',
        role=UserRoles.MEMBER,
        is_active=True,
        is_superuser=False,
        is_staff=False
    )
    user.set_password('qwerty')
    user.save()
    return user

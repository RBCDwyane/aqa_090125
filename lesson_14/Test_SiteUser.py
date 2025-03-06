import pytest
import json
from homework_14 import SiteUser

'''тестування ініціації'''
def test_create_user_success1():
    user = SiteUser(name="Dave", email="dave@here.com", access_level="user", logcount=0)
    assert user.name == "Dave"
    assert user.email == "dave@here.com"
    assert user.access_level == "user"
    assert user._logcount == 0
def test_create_user_success2():
    user = SiteUser(name="Dave", email="dave@here.com", access_level="admin", logcount=5)
    assert user.name == "Dave"
    assert user.email == "dave@here.com"
    assert user.access_level == "admin"
    assert user._logcount == 5
def test_create_user_success3():
    user = SiteUser(name="Dave", email="dave@here.com", access_level="moderator", logcount=5)
    assert user.name == "Dave"
    assert user.email == "dave@here.com"
    assert user.access_level == "moderator"
    assert user._logcount == 5
def test_create_user_success4():
    user = SiteUser(name="Dave", email="dave@here.com", access_level="blocked", logcount=5)
    assert user.name == "Dave"
    assert user.email == "dave@here.com"
    assert user.access_level == "blocked"
    assert user._logcount == 5
def test_create_user_success5():
    user = SiteUser(name="Dave", email="dave@here.com", logcount=5)
    assert user.name == "Dave"
    assert user.email == "dave@here.com"
    assert user.access_level == "user"
    assert user._logcount == 5
def test_create_user_success6():
    user = SiteUser(name="Dave", email="dave@here.com", access_level="admin")
    assert user.name == "Dave"
    assert user.email == "dave@here.com"
    assert user.access_level == "admin"
    assert user._logcount == 0
def test_invalid_name1():
    with pytest.raises(TypeError, match="Значення name повинно бути строкою."):
        SiteUser(name=12345, email="dave@here.com", access_level="user")
def test_invalid_name2():
    with pytest.raises(TypeError, match="Значення name повинно бути строкою."):
        SiteUser(name="", email="dave@here.com", access_level="user")
def test_invalid_email1():
    with pytest.raises(TypeError, match="Значення email повинно бути строкою."):
        SiteUser(name="Dave", email=12345, access_level="user")
def test_invalid_email2():
    with pytest.raises(TypeError, match="Значення email повинно бути строкою."):
        SiteUser(name="Dave", email="", access_level="user")
def test_invalid_access_level1():
    with pytest.raises(ValueError, match="Некоректне занчення  access level. Має бути одним з admin, moderator, user чи blocked."):
        SiteUser(name="Dave", email="dave@here.com", access_level="success")
def test_invalid_access_level2():
    with pytest.raises(TypeError, match="Некоректне занчення  access level. Має бути одним з admin, moderator, user чи blocked."):
        SiteUser(name="Dave", email="dave@here.com", access_level=12345)
def test_invalid_logcount1():
    with pytest.raises(TypeError, match="Некоректне занчення  logcount. Має бути натуральним числом."):
        SiteUser(name="Dave", email="dave@here.com", access_level="user", logcount="text")
def test_invalid_logcount2():
    with pytest.raises(ValueError, match="Некоректне занчення  logcount. Має бути натуральним числом."):
        SiteUser(name="Dave", email="dave@here.com", access_level="user", logcount=-1)

'''тестування виводу'''
def test_str_method():
    user = SiteUser(name="Dave", email="dave@here.com", access_level="admin")
    expected_output = json.dumps({'User': "Dave", 'email': "dave@here.com", 'access level': "admin"})
    assert str(user) == expected_output
def test_str_method2():
    user = SiteUser(name="Dave", email="dave@here.com")
    expected_output = json.dumps({'User': "Dave", 'email': "dave@here.com", 'access level': "user"})
    assert str(user) == expected_output
def test_str_method3():
    user = SiteUser(name="Dave", email="dave@here.com", access_level="admin")
    user.set_name("Gretta")
    user.set_email('gretta@mail.com')
    user.set_access_level('blocked')
    user.set_logcount(56)
    expected_output = json.dumps({'User': "Gretta", 'email': "gretta@mail.com", 'access level': "blocked"})
    assert str(user) == expected_output

'''тестування функції порівняння'''
def test_users_with_same_email():
    user1 = SiteUser(name="Dave", email="dave@here.com")
    user2 = SiteUser(name="Robert", email="dave@here.com")
    assert user1 == user2
def test_users_with_different_email():
    user1 = SiteUser(name="Dave", email="dave@here.com")
    user2 = SiteUser(name="Robert", email="robert@mail.com")
    assert user1 != user2
def test_user_not_equal():
    user1 = SiteUser(name="Dave", email="dave@here.com")
    user2 = 'text'
    user3 = 23
    user4 = None
    assert user1 != user2
    assert user1 != user3
    assert user1 != user4

'''тестування сеттера, геттера та функції додавання для logcount'''
def test_get_logcount1():
    user = SiteUser(name="Dave", email="dave@here.com", logcount=10)
    assert user.get_logcount() == 10
def test_get_logcount2():
    user = SiteUser(name="Dave", email="dave@here.com")
    assert user.get_logcount() == 0
def test_set_logcount_positive1():
    user = SiteUser(name="Dave", email="dave@here.com", logcount=10)
    user.set_logcount(3)
    assert user.get_logcount() == 3
def test_set_logcount_positive2():
    user = SiteUser(name="Dave", email="dave@here.com", logcount=10)
    user.set_logcount(0)
    assert user.get_logcount() == 0
def test_set_logcount_negative_raises_value_error():
    user = SiteUser(name="Dave", email="dave@here.com", logcount=10)
    with pytest.raises(ValueError, match="Некоректне занчення  logcount. Має бути натуральним числом."):
        user.set_logcount(-2)
    assert user.get_logcount() == 10
def test_set_logcount_negative_raises_type_error1():
    user = SiteUser(name="Dave", email="dave@here.com", logcount=10)
    with pytest.raises(TypeError, match="Некоректне занчення  logcount. Має бути натуральним числом."):
        user.set_logcount(2.5)
    assert user.get_logcount() == 10
def test_set_logcount_negative_raises_type_error2():
    user = SiteUser(name="Dave", email="dave@here.com", logcount=10)
    with pytest.raises(TypeError, match="Некоректне занчення  logcount. Має бути натуральним числом."):
        user.set_logcount('text')
    assert user.get_logcount() == 10
def test_set_logcount_negative_raises_type_error3():
    user = SiteUser(name="Dave", email="dave@here.com", logcount=10)
    with pytest.raises(TypeError, match="Некоректне занчення  logcount. Має бути натуральним числом."):
        user.set_logcount(None)
    assert user.get_logcount() == 10
def test_add_logcount_positive():
    user = SiteUser(name="Dave", email="dave@here.com")
    user.add_logcount(1)
    assert user.get_logcount() == 1
def test_add_logcount_negative_raises_value_error():
    user = SiteUser(name="Dave", email="dave@here.com", logcount=10)
    with pytest.raises(ValueError, match='Некоректне занчення  logcount. Має бути натуральним числом більше 0.'):
        user.add_logcount(0)
    assert user.get_logcount() == 10
def test_add_logcount_negative_raises_value_error1():
    user = SiteUser(name="Dave", email="dave@here.com", logcount=10)
    with pytest.raises(ValueError, match="Некоректне занчення  logcount. Має бути натуральним числом більше 0."):
        user.add_logcount(-1)
    assert user.get_logcount() == 10
def test_add_logcount_negative_raises_typeerror2():
    user = SiteUser(name="Dave", email="dave@here.com", logcount=10)
    with pytest.raises(TypeError, match="Некоректне занчення  logcount. Має бути натуральним числом більше 0."):
        user.add_logcount(2.5)
    assert user.get_logcount() == 10
def test_add_logcount_negative_raises_typeerror3():
    user = SiteUser(name="Dave", email="dave@here.com", logcount=10)
    with pytest.raises(TypeError, match="Некоректне занчення  logcount. Має бути натуральним числом більше 0."):
        user.add_logcount('text')
    assert user.get_logcount() == 10
def test_add_logcount_negative_raises_typeerror4():
    user = SiteUser(name="Dave", email="dave@here.com", logcount=10)
    with pytest.raises(TypeError, match="Некоректне занчення  logcount. Має бути натуральним числом більше 0."):
        user.add_logcount(None)
    assert user.get_logcount() == 10

'''тестування сеттера та геттера для name'''
def test_get_name():
    user = SiteUser(name="Dave", email="dave@here.com")
    assert user.get_name() == "Dave"
def test_set_name_positive():
    user = SiteUser(name="Dave", email="dave@here.com")
    user.set_name('Gretta')
    assert user.get_name() == 'Gretta'
def test_set_name_negative1():
    user = SiteUser(name="Dave", email="dave@here.com", logcount=10)
    with pytest.raises(TypeError, match="Значення name повинно бути строкою."):
        user.set_name(None)
    assert user.get_name() == "Dave"
def test_set_name_negative2():
    user = SiteUser(name="Dave", email="dave@here.com", logcount=10)
    with pytest.raises(TypeError, match="Значення name повинно бути строкою."):
        user.set_name(5)
    assert user.get_name() == "Dave"

'''тестування сеттера та геттера для email'''
def test_get_email():
    user = SiteUser(name="Dave", email="dave@here.com")
    assert user.get_email() == "dave@here.com"
def test_set_email_positive():
    user = SiteUser(name="Dave", email="dave@here.com")
    user.set_email('gretta@mail.com')
    assert user.get_email() == 'gretta@mail.com'
def test_set_email_negative1():
    user = SiteUser(name="Dave", email="dave@here.com", logcount=10)
    with pytest.raises(TypeError, match="Значення email повинно бути строкою."):
        user.set_email(None)
    assert user.get_email() == "dave@here.com"
def test_set_email_negative2():
    user = SiteUser(name="Dave", email="dave@here.com", logcount=10)
    with pytest.raises(TypeError, match="Значення email повинно бути строкою."):
        user.set_email(5)
    assert user.get_email() == "dave@here.com"

'''тестування сеттера та геттера для access_level'''
def test_get_access_level1():
    user = SiteUser(name="Dave", email="dave@here.com")
    assert user.get_access_level() == "user"
def test_get_access_level2():
    user = SiteUser(name="Dave", email="dave@here.com", access_level='admin')
    assert user.get_access_level() == "admin"
def test_set_accesslevel_positive1():
    user = SiteUser(name="Dave", email="dave@here.com")
    user.set_access_level('admin')
    assert user.get_access_level() == 'admin'
def test_set_accesslevel_positive2():
    user = SiteUser(name="Dave", email="dave@here.com")
    user.set_access_level('moderator')
    assert user.get_access_level() == 'moderator'
def test_set_accesslevel_positive3():
    user = SiteUser(name="Dave", email="dave@here.com")
    user.set_access_level('blocked')
    assert user.get_access_level() == 'blocked'
def test_set_accesslevel_positive4():
    user = SiteUser(name="Dave", email="dave@here.com", access_level='admin')
    user.set_access_level('user')
    assert user.get_access_level() == 'user'
def test_set_accesslevel_negative():
    user = SiteUser(name="Dave", email="dave@here.com", logcount=10)
    with pytest.raises(ValueError, match="Некоректне занчення  access level. Має бути одним з admin, moderator, user чи blocked."):
        user.set_access_level('success')
    assert user.get_access_level() == "user"
def test_set_accesslevel_negative1():
    user = SiteUser(name="Dave", email="dave@here.com", logcount=10)
    with pytest.raises(ValueError, match="Некоректне занчення  access level. Має бути одним з admin, moderator, user чи blocked."):
        user.set_access_level(None)
    assert user.get_access_level() == "user"
def test_set_accesslevel_negative2():
    user = SiteUser(name="Dave", email="dave@here.com", logcount=10)
    with pytest.raises(ValueError, match="Некоректне занчення  access level. Має бути одним з admin, moderator, user чи blocked."):
        user.set_access_level(5)
    assert user.get_access_level() == "user"
import sys
import unittest
import os

sys.path.append("..")

import sql_manager


class SqlManagerTests(unittest.TestCase):

    def setUp(self):
        sql_manager.create_clients_table()
        sql_manager.register('Tester', '123')

    def tearDown(self):
        sql_manager.cursor.execute('DROP TABLE clients')

    @classmethod
    def tearDownClass(cls):
        os.remove("bank.db")

    def test_register(self):
        sql_manager.register('Dinko', '123123')

        sql_manager.cursor.execute('SELECT Count(*)  FROM clients WHERE username = (?) AND password = (?)', ('Dinko', '123123'))
        users_count = sql_manager.cursor.fetchone()

        self.assertEqual(users_count[0], 1)

    def test_login(self):
        logged_user = sql_manager.login('Tester', '123')
        self.assertEqual(logged_user.get_username(), 'Tester')

    def test_login_injection(self):
        logged_user = sql_manager.login('Tester', "' OR 1 = 1 --")
        self.assertFalse(logged_user)

    def test_is_strong(self):
        short_password = "!1Asdf"
        no_caps = "1!adfasfafsfdas"
        no_num = "!@FAFAdfasfs"
        no_special = "ADSDAdasdasd1312"
        strong_pass = "!1Aaaaaa"
        self.assertFalse(sql_manager.is_strong(short_password))
        self.assertFalse(sql_manager.is_strong(no_caps))
        self.assertFalse(sql_manager.is_strong(no_num))
        self.assertFalse(sql_manager.is_strong(no_special))
        self.assertTrue(sql_manager.is_strong(strong_pass))

    def test_login_wrong_password(self):
        logged_user = sql_manager.login('Tester', '123567')
        self.assertFalse(logged_user)

    def test_change_message(self):
        logged_user = sql_manager.login('Tester', '123')
        new_message = "podaivinototam"
        sql_manager.change_message(new_message, logged_user)
        self.assertEqual(logged_user.get_message(), new_message)

    def test_change_password(self):
        logged_user = sql_manager.login('Tester', '123')
        new_password = "12345"
        sql_manager.change_pass(new_password, logged_user)

        logged_user_new_password = sql_manager.login('Tester', new_password)
        self.assertEqual(logged_user_new_password.get_username(), 'Tester')

if __name__ == '__main__':
    unittest.main()

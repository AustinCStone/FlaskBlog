from app import app
import unittest


class BaseTestCase(unittest.TestCase):
   
    #ensure that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type = 'html/text')
        self.assertEqual(response.status_code,200)

    #ensure that login page loads correctly
    def test_login_page_loads(self):
        tester=app.test_client(self)
        response = tester.get('/login',content_type='html/text')
        self.assertTrue("Please login" in response.data)
    
    #ensure that login page behaves correctly given correct credentials
    def test_correct_login(self):
        tester=app.test_client(self)
        response = tester.post('/login',data=dict(username='admin',password='admin'), follow_redirects = True)
        self.assertTrue("you were just logged in" in response.data)

    #incorrect credentials
    def test_incorrect_login(self):
        tester=app.test_client(self)
        response = tester.post('/login',data=dict(username='aasfoh',password='oihafsoh'))
        self.assertTrue("Invalid credentials" in response.data)
    
    #logout functionality
    def test_logout(self):
        tester=app.test_client(self)
        tester.post('/login',data=dict(username='admin',password='admin'), follow_redirects = True)
        response = tester.get('/logout',follow_redirects=True)
        self.assertTrue(" You were just logged out" in response.data)

    #ensure that main page requires login
    def test_main_route_requires_login(self):
        tester=app.test_client(self)
        response = tester.get('/',content_type='html/text',follow_redirects=True)
        self.assertTrue("you need to login first" in response.data)

    #ensure database loads on main page
    def test_load_database(self):
        tester=app.test_client(self)
        tester.post('/login',data=dict(username='admin',password='admin'), follow_redirects = True)
        response = tester.get('/')
        self.assertTrue("Post:" in response.data)
   


if __name__ =='__main__':
    unittest.main()
    
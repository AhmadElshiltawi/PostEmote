import unittest
from unittest.mock import Mock
from django.test import TestCase
from . import backend
from . import views
from django.test import Client
csrf_client = Client(enforce_csrf_checks=True)
# Create your tests here.

class testcredentialnotnull(TestCase):

    def testcredential(self):
        test = False
        self.assertEqual(backend.validate_credential_not_null(credential=""), test)

class testvalidlogin(TestCase): ##FunctionalID 2
    def testvalidlogin(self):
        user = backend.create_user(username="neil",email_address="neilsemail", password= "passwords")
        response = self.client.post('/signin', {'username' : 'neil', 'password' : 'passwords'}, follow = True)
        self.assertEqual(response.status_code, 200)
class testinvalidlogin(TestCase):##FunctionalID 4
    def testinvalidlogin(self):
        response = self.client.post('/signin', {'username' : '', 'password' : 'passwords'}, follow = True)
        self.assertEqual(response.status_code, 200)
class testvalidsignout(TestCase): ##FunctionalID 5
    def testvalidsignout(self):
        user = backend.create_user(username="neil",email_address="neilsemail", password= "passwords")
        response = self.client.post('/signin', {'username' : 'neil', 'password' : 'passwords'}, follow = True)
        response = self.client.post('/signout', follow = True)
        self.assertEqual(response.status_code, 200)
class testsortmostsad(TestCase): ##FunctionalID 10
    def testsortmostsad(self):
        user = backend.create_user(username="neil",email_address="neilsemail", password= "passwords")
        response = self.client.post('/signin', {'username' : 'neil', 'password' : 'passwords'}, follow = True)
        response = self.client.post('/sad_sort', follow = True)
        self.assertEqual(response.status_code, 200)

class testsortmostfunny(TestCase): ##FunctionalID 8
    def testsortmostfunny(self):
        user = backend.create_user(username="neil",email_address="neilsemail", password= "passwords")
        response = self.client.post('/signin', {'username' : 'neil', 'password' : 'passwords'}, follow = True)
        response = self.client.post('/sad_sort', follow = True)
        self.assertEqual(response.status_code, 200)
class testsortmostsurprising(TestCase): ##FunctionalID 7
    def testsortmostsurprising(self):
        user = backend.create_user(username="neil",email_address="neilsemail", password= "passwords")
        response = self.client.post('/signin', {'username' : 'neil', 'password' : 'passwords'}, follow = True)
        response = self.client.post('/surprising_sort', follow = True)
        self.assertEqual(response.status_code, 200)
class testsortmostangering(TestCase): ##FunctionalID 9
    def testsortmostangering(self):
        user = backend.create_user(username="neil",email_address="neilsemail", password= "passwords")
        response = self.client.post('/signin', {'username' : 'neil', 'password' : 'passwords'}, follow = True)
        response = self.client.post('/angry_sort', follow = True)
        self.assertEqual(response.status_code, 200)
class testsortdisablecomment(TestCase): ##Testing disable comments
    def testsortdisablecomment(self):
        user = backend.create_user(username="neil",email_address="neilsemail", password= "passwords")
        response = self.client.post('/signin', {'username' : 'neil', 'password' : 'passwords'}, follow = True)
        response = self.client.post('/disable-comments', follow = True)
        self.assertEqual(response.status_code, 200)


from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class StaffWithoutPermissionsTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        opts = Options()
        opts.add_argument("--headless")
        cls.selenium = webdriver.Firefox(options=opts)
        cls.selenium.implicitly_wait(5)

        # superusuario
        admin = User.objects.create_superuser(
            "isard", "isard@isard.com", "pirineus"
        )

        # usuario staff SIN permisos
        staff = User.objects.create_user(
            "staff1", "staff@staff.com", "staffpass"
        )
        staff.is_staff = True
        staff.save()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_staff_cannot_create_users_or_questions(self):
        # login como staff
        self.selenium.get(f"{self.live_server_url}/admin/login/")
        self.selenium.find_element(By.NAME, "username").send_keys("staff1")
        self.selenium.find_element(By.NAME, "password").send_keys("staffpass")
        self.selenium.find_element(By.XPATH, "//input[@value='Log in']").click()

        # comprobar que NO existe Users
        try:
            self.selenium.find_element(By.LINK_TEXT, "Users")
            assert False, "El usuario staff NO debería ver Users"
        except NoSuchElementException:
            pass

        # comprobar que NO existe Questions
        try:
            self.selenium.find_element(By.LINK_TEXT, "Questions")
            assert False, "El usuario staff NO debería ver Questions"
        except NoSuchElementException:
            pass

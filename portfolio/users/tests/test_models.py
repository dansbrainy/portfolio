from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


def test_user_get_absolute_url(user: User):
    assert user.get_absolute_url() == f"/users/{user.username}/"


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="testuser",
            email="testuser@example.com",
            password="password",
            name="Test User",
            home_address="123 Main St",
            phone_number="555-555-5555",
            bio="I am a test user",
            profession="Tester",
        )

    def test_user_creation(self):
        self.assertIsInstance(self.user, User)
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "testuser@example.com")
        self.assertEqual(self.user.name, "Test User")
        self.assertEqual(self.user.home_address, "123 Main St")
        self.assertEqual(self.user.phone_number, "555-555-5555")
        self.assertEqual(self.user.bio, "I am a test user")
        self.assertEqual(self.user.profession, "Tester")

    def test_get_absolute_url(self):
        url = reverse("users:detail", kwargs={"username": self.user.username})
        self.assertEqual(self.user.get_absolute_url(), url)

from django.test import TestCase
from django.contrib.auth import get_user_model
from datetime import datetime
from network.models import Following
from network.models import Post

# Create your tests here.


class UserTestCase(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create(username="testUserName",
                                   email="test@email.com",
                                   password="testpassword")

        errors = []
        if user.username != 'testUserName':
            errors.append(f"Username should be 'testUserName', but it's {user.username}")
        if user.email != 'test@email.com':
            errors.append(f"Email should be 'test@email.com', but it's {user.email}")
        if not user.is_active:
            errors.append("User should be active, but is not")
        if user.is_superuser:
            errors.append("User should not be a superuser, but is")

        self.assertListEqual(errors, [])


class FollowingModelTestCase(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user1 = User.objects.create_user(
            username='user1', email='user1@example.com', password='password')
        self.user2 = User.objects.create_user(
            username='user2', email='user2@example.com', password='password')

    def test_following_model(self):
        following = Following.objects.create(user=self.user1)
        following.following.add(self.user2)
        self.assertEqual(str(following), f"{self.user1} follows {self.user2.username}")
        self.assertEqual(following.user, self.user1)
        self.assertIn(self.user2, following.following.all())
        self.assertFalse(self.user1 in following.following.all())


class PostModelTestCase(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user1 = User.objects.create_user(
            username='user1', email='user1@example.com', password='password')
        self.user2 = User.objects.create_user(
            username='user2', email='user2@example.com', password='password')
        self.post1 = Post.objects.create(
            user=self.user1, content='Post 1 content', timestamp=datetime.now())
        self.post2 = Post.objects.create(
            user=self.user2, content='Post 2 content', timestamp=datetime.now())

    def test_post_model(self):
        self.assertEqual(str(self.post1), f"{self.user1} {self.post1.timestamp.strftime('%b %d %Y, %I:%M %p')}")
        self.assertEqual(self.post1.user, self.user1)
        self.assertEqual(self.post1.content, 'Post 1 content')
        self.assertEqual(self.post2.content, 'Post 2 content')
        self.assertFalse(self.post1.likes.all())
        self.post1.likes.add(self.user2)
        self.assertIn(self.user2, self.post1.likes.all())


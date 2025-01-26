from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Post, Category
from .serializers import PostSerializer


class CreatePostTests(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username="testuser", password="testpassword123"
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)  # Authenticate the user

        # Create a test category
        self.category = Category.objects.create(name="Test Category")

        # URL for creating a post
        self.url = reverse(
            "create-post"
        )  # Replace 'create-post' with the actual URL name

    def test_create_post_authenticated(self):
        """
        Ensure an authenticated user can create a post.
        """
        data = {
            "title": "Test Post",
            "content": "This is a test post content.",
            "category": self.category.id,
        }

        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().title, "Test Post")

    def test_create_post_unauthenticated(self):
        """
        Ensure an unauthenticated user cannot create a post.
        """
        self.client.logout()  # Log out the authenticated user

        data = {
            "title": "Test Post Unauthenticated",
            "content": "This is a test post content.",
            "category": self.category.id,
        }

        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Post.objects.count(), 0)

    def test_create_post_invalid_data(self):
        """
        Ensure a post cannot be created with invalid data.
        """
        data = {
            "title": "",  # Title is required
            "content": "This is a test post content.",
            "category": self.category.id,
        }

        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Post.objects.count(), 0)

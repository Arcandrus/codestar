from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm
from .models import Post

class TestBlogViews(TestCase):
    # Setup an intial value to test and populate all needed fields
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.post = Post(title="Blog title", author=self.user,
                         slug="blog-title", excerpt="Blog excerpt",
                         content="Blog content", status=1)
        # Save our defaults
        self.post.save()

    # Pull values from our setup
    def test_render_post_detail_page_with_comment_form(self):
        # Create the URL based on blog title
        response = self.client.get(reverse('post_detail', args=['blog-title']))
        # Does URL work
        self.assertEqual(response.status_code, 200)
        # Does Blog title exist in the page
        self.assertIn(b"Blog title", response.content)
        # Does Blog content exist in the page
        self.assertIn(b"Blog content", response.content)
        # Does the comment form render
        self.assertIsInstance(response.context['comment_form'], CommentForm)
        
    def test_successful_comment_submission(self):
        """Test for posting a comment on a post"""
        # Dummy user to submit a comment
        self.client.login(username="myUsername", password="myPassword")
        # Contents of comment
        post_data = {
            'body': 'This is a test comment.'
        }

        # Create a URL for the comment submission based on post_data and post_detail
        response = self.client.post(reverse('post_detail', args=['blog-title']), post_data)
        # Does URL work
        self.assertEqual(response.status_code, 200)
        # Does comment get submitted
        self.assertIn(b'Comment submitted and awaiting approval', response.content)
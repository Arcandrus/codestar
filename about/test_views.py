from django.urls import reverse
from django.test import TestCase
from .models import About
from .forms import CollaborateForm

class TestAboutViews(TestCase):
    # Setup an intial value to test and populate all needed fields
    def setUp(self):
        self.about = About(
            title = "About Me",
            updated_on = "NOW",
            profile_image = "DEFAULT.jpg",
            content = "This is my about me page"
        )
        # Save our defaults
        self.about.save()

    # Pull values from our setup
    def test_render_about_me_page(self):
        # Test the url for the page
        response = self.client.get(reverse('about'))
        # Tests that page loads correctly
        self.assertEqual(response.status_code, 200)
        # Check if About Me has content
        self.assertIn(b'About Me', response.content)
        # Check if there is a collab form present in the render
        self.assertIsInstance(response.context['collaborate_form'], CollaborateForm)

    def test_successful_collab_submission(self):
        """Test for posting a collab request"""
        # Contents of form
        form_data = {
            'name': 'Eric',
            'email': 'email@email.com',
            'message': 'Lets Collab!'
        }

        # Create a URL for the collab submission based on post_data
        response = self.client.post(reverse('about'), form_data)
        # Does URL work
        self.assertEqual(response.status_code, 200)
        # Does comment get submitted
        self.assertIn(b'Collaboration request received! I endeavour to respond within 2 working days.', response.content)
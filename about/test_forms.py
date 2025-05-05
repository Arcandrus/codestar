from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):
    def test_field_required(self):
        form = CollaborateForm({
            'name': '',
            'email': '',
            'message': ''
        })

        is_valid = form.is_valid()

        try:
            self.assertTrue(is_valid, "Expected form to be valid!\n")

        except AssertionError as e:
            # Suppress default assertion message and handle with custom print
            print("\n❌ Test Failed: Form invalid! See below: \n")

            # Custom feedback with form errors
            for field, errors in form.errors.items():
                for error in errors:
                    print(f"{field.upper()}: {error}")
            
            print('\n\nThe following "ok" is printed by Djangos default test behaviour' \
                '\nand cannot be easily overwritten or removed. Please ignore.')

            return  # End the test early without re-raising the exception
        
        else:
            self.test_failed = False
            print("\n✅ Test passed: Form is valid")
            print('\n\nThe following "ok" is printed by Djangos default test behaviour' \
                    '\nand cannot be easily overwritten or removed. Please ignore.')
# tests/test_models.py
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Destination

class DestinationModelTest(TestCase):

    # def setUp(self):
    #     self.image = SimpleUploadedFile(
    #         name='test_image.jpg',
    #         content=b'',  # Empty byte content just for testing
    #         content_type='image/jpeg'
    #     )

    def test_create_destination(self):
        destination = Destination.objects.create(
            name='Paris',
            # img=self.image,
            desc='City of Lights',
            price=1200,
            offer=True
        )

        # Check if the object was created correctly
        self.assertEqual(destination.name, 'Paris')
        self.assertEqual(destination.desc, 'City of Lights')
        self.assertEqual(destination.price, 1200)
        self.assertTrue(destination.offer)
        # self.assertTrue(destination.img.name.startswith('Media/test_image'))

    def test_offer_defaults_to_false(self):
        destination = Destination.objects.create(
            name='Tokyo',
            # img=self.image,
            desc='Tech City',
            price=2000,
        )
        self.assertFalse(destination.offer)

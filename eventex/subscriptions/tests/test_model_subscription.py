from datetime import datetime
from eventex.subscriptions.models import Subscription
from django.test import TestCase

class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name = 'Emerson Henning',
            cpf = '12345678901',
            email='emerson@henning.com.br',
            phone='41-99650-9393'
        )
        self.obj.save()

    def test_create(self):
        
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

    
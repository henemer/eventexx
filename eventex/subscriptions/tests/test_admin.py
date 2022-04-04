from unittest.mock import Mock
from django.test import TestCase
from eventex.subscriptions.admin import SubscriptionModelAdmin, Subscription, admin


class SubscriptionNomdeAdminTest(TestCase):
    def setUp(self):
        Subscription.objects.create(name='Emerson Henning', cpf='12345678901', phone='41-99650-9393', email='emerson@henning.com.br')

        self.model_admin = SubscriptionModelAdmin(Subscription, admin.site)


    def test_has_action(self):
        self.assertIn('mark_as_paid', self.model_admin.actions)

    def test_mark_all(self):
        """It should mark all selected subscription as paid."""
        queryset = Subscription.objects.all()

        self.call_action()

        self.assertEqual(1, Subscription.objects.filter(paid=True).count())

    def test_message(self):
        """It should send a message to the user."""

        mock = self.call_action()
        
        mock.assert_called_once_with(None, '1 inscrição foi marcada como paga.')


    def call_action(self):
        queryset = Subscription.objects.all()

        mock = Mock()
        old_message_user = SubscriptionModelAdmin.message_user
        SubscriptionModelAdmin.message_user = mock

        self.model_admin.mark_as_paid(None, queryset)

        SubscriptionModelAdmin.message_user = old_message_user

        return mock


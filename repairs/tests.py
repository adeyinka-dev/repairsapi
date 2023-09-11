from django.test import TestCase
from django.urls import reverse

from .models import Repair


class RepairTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.repair = Repair.objects.create(
            type="Electricity",
            subtype="Sockets",
        )

    def test_repair_type(self):
        self.assertEqual(self.repair.type, "Electricity")
        self.assertEqual(self.repair.subtype, "Sockets")

    def test_repair_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sockets")
        self.assertTemplateUsed(response, "repairs/repair_types.html")

from django.test import TestCase
from django.utils import timezone
from .models import Question

class IOCBasicTest(TestCase):
    def test_create_question(self):
        Question.objects.create(question_text="Test IOC", pub_date=timezone.now())
        self.assertEqual(Question.objects.count(), 1)

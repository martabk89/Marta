from django.test import TestCase
from django.utils import timezone
from .models import Question, Choice


class IOCBasicTest(TestCase):

    def test_create_question(self):
        """Comprobar que se puede crear una Question"""
        q = Question.objects.create(
            question_text="¿Test IOC?",
            pub_date=timezone.now()
        )
        self.assertEqual(Question.objects.count(), 1)
        self.assertEqual(str(q), "¿Test IOC?")

    def test_create_choice(self):
        """Comprobar que se puede crear una Choice asociada"""
        q = Question.objects.create(
            question_text="¿Test Choice?",
            pub_date=timezone.now()
        )
        c = Choice.objects.create(
            question=q,
            choice_text="Sí",
            votes=0
        )
        self.assertEqual(Choice.objects.count(), 1)
        self.assertEqual(c.question, q)

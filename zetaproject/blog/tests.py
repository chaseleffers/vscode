import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Question


class QuestionModelTest(TestCase):

    def test_was_published_recently_future(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
    
    def test_was_published_recently_old(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        past_question = Question(pub_date=time)
        self.assertIs(past_question.was_published_recently(), False)
    
    def test_was_published_recently_recent(self):
        time = timezone.now()
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

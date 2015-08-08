from django.test import TestCase

import datetime

from django.utils import timezone
from polls.models import Question
from django.core.urlresolvers import reverse

# Create your tests here.

class QuestionMethodTests(TestCase):

  def test_was_published_recently_with_future_question(self):
    """
    was_published_recently() should return False for questions whose pub_Date is in the future 
    """
    time = timezone.now() + datetime.timedelta(days=30)
    future_question = Question(pub_date = time)
    self.assertEqual(future_question.was_published_recently(), False)

  def test_was_published_recently_with_recent_question(self):
    """
    was_published_recently() should return True for q's whose pub_dates are within the last day
    """
    one_hour_ago = timezone.now() - datetime.timedelta(hours=1) #one hour ago
    recent_question = Question(pub_date = one_hour_ago)
    self.assertEqual(recent_question.was_published_recently(), True)
  
def create_question(question_text, days):
  """
  Creates a question with given text, published given days
  offset to now (negative for questions published in past, 
  positive for q's published in the future)
  """
  time = timezone.now() + datetime.timedelta(days=days)
  return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionViewTests(TestCase):
  def test_index_view_with_no_questions(self):
    """
    with no questions, an appropriate message should be displayed
    """
    response = self.client.get(reverse('polls:index'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "No polls are available.")
    self.assertQuerysetEqual(response.context['latest_question_list'], [])

  def test_index_with_past_question(self):
    """
    Questions wtih pubdate in the past should be displayed
    """
    create_question(question_text="Past question.", days=-30)
    response = self.client.get(reverse('polls:index'))
    self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past question.>'])

  def test_index_view_with_a_future_question(self):
      """
      Questions with a pub_date in the future should not be displayed on
      the index page.
      """
      create_question(question_text="Future question.", days=30)
      response = self.client.get(reverse('polls:index'))
      self.assertContains(response, "No polls are available.",
                          status_code=200)
      self.assertQuerysetEqual(response.context['latest_question_list'], [])

  def test_index_view_with_future_question_and_past_question(self):
      """
      Even if both past and future questions exist, only past questions
      should be displayed.
      """
      create_question(question_text="Past question.", days=-30)
      create_question(question_text="Future question.", days=30)
      response = self.client.get(reverse('polls:index'))
      self.assertQuerysetEqual(
          response.context['latest_question_list'],
          ['<Question: Past question.>']
      )

  def test_index_view_with_two_past_questions(self):
      """
      The questions index page may display multiple questions.
      """
      create_question(question_text="Past question 1.", days=-30)
      create_question(question_text="Past question 2.", days=-5)
      response = self.client.get(reverse('polls:index'))
      self.assertQuerysetEqual(
          response.context['latest_question_list'],
          ['<Question: Past question 2.>', '<Question: Past question 1.>']
      )

class QuestionIndexDetailTests(TestCase):
  def test_detail_view_with_a_future_question(self):
      """
      The detail view of a question with a pub_date in the future should
      return a 404 not found.
      """
      future_question = create_question(question_text='Future question.',
                                        days=5)
      response = self.client.get(reverse('polls:detail',
                                 args=(future_question.id,)))
      self.assertEqual(response.status_code, 404)

  def test_detail_view_with_a_past_question(self):
      """
      The detail view of a question with a pub_date in the past should
      display the question's text.
      """
      past_question = create_question(question_text='Past Question.',
                                      days=-5)
      response = self.client.get(reverse('polls:detail',
                                 args=(past_question.id,)))
      self.assertContains(response, past_question.question_text,
                          status_code=200)
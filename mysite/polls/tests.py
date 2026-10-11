from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Choice, Question


class PollsViewTests(TestCase):
	"""Testa a navegação, a exibição e o envio de votos da enquete."""

	def setUp(self):
		self.question = Question.objects.create(
			question_text='Pergunta de teste',
			pub_date=timezone.now(),
		)
		self.choice = Choice.objects.create(
			question=self.question,
			choice_text='Opção de teste',
		)

	def test_home_redirects_to_poll_list(self):
		response = self.client.get('/')

		self.assertRedirects(response, reverse('polls:index'))

	def test_question_detail_displays_question_and_choices(self):
		response = self.client.get(
			reverse('polls:detail', args=[self.question.pk])
		)

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, self.question.question_text)
		self.assertContains(response, self.choice.choice_text)

	def test_vote_without_choice_shows_validation_message(self):
		response = self.client.post(
			reverse('polls:vote', args=[self.question.pk])
		)

		self.assertEqual(response.status_code, 200)
		self.assertEqual(
			response.context['error_message'],
			"You didn't select a choice.",
		)

	def test_vote_increments_choice_and_redirects_to_results(self):
		response = self.client.post(
			reverse('polls:vote', args=[self.question.pk]),
			{'choice': self.choice.pk},
		)

		self.choice.refresh_from_db()
		self.assertEqual(self.choice.votes, 1)
		self.assertRedirects(
			response,
			reverse('polls:results', args=[self.question.pk]),
		)

	def test_results_for_missing_question_return_404(self):
		response = self.client.get(
			reverse('polls:results', args=[self.question.pk + 1])
		)

		self.assertEqual(response.status_code, 404)

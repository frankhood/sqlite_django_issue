from django.test import TestCase

from polls.models import Question, Choice


class PollUnitTest(TestCase):

    def test_create_choices_in_a_question(self):
        question = Question.objects.create(question_text="Test Question")
        [Choice.objects.create(choice_text=f"Choice n° {x}", question=question) for x in range(3)]
        self.assertEqual(
            list(question.choices.all().order_by("choice_text").values_list("choice_text", flat=True)),
            list(Choice.objects.all().order_by("choice_text").values_list("choice_text", flat=True))
        )
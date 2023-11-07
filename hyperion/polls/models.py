from django.db import models

# Create your models here.
class Question(models.Model):
    """
    This model is a data straucture for storing poll questions.
    Each question has a text and a publication date associated with it.

    Attributes:
        question_text (str): The text of the question, limited to 200 characters.
        pub_date (datetime): The date and time when the question was published.

    Methods:
        __str__(): Returns the question text as a string representation
    """

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    """
    A model representing a choice to be selected  for a question in a poll.
    Each choice has a choice text descriptor and a variable to count votes.

    Attributes:
        question (ForeignKey): The question to which this choice belongs.
        choice_text (str): The text of the choice, limited to 200 characters.
        votes (int): The number of votes received for this choice.

    Methods:
        __str__(): Returns the choice text as a string representation.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE )
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
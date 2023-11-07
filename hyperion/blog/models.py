from django.db import models

# Create your models here.
class Post(models.Model):
    """
    Blog Post model.

    This model defines the structure for storing blog posts. Each post has a title,
    category, body text, publication date, and an optional signature.

    Attributes:
        title (str): The title of the blog post, limited to 140 characters.
        category (str): The category or topic of the post, limited to 140 characters.
        body (str): The main content of the blog post.
        date (datetime): The publication date and time of the post.
        signature (str): An optional signature for the post, limited to 140 characters.

    Methods:
        __str__(): Returns the title of the post as a string representation.

    """
    title = models.CharField(max_length =140)
    category = models.CharField(max_length =140)
    body= models.TextField()
    date= models.DateTimeField()
    signature = models.CharField(max_length=140, default="AS ALWAYS - STAY FROSTY!")

    def _str_(self):
        return self.title

from django.db import models

class FAQ(models.Model):
    question = models.CharField(
        verbose_name="Frequently Asked Question",
        max_length=255,
        blank=False,
        null=False,
        default="We wil be Happy to be questioned!"
    )

    answer = models.TextField(
        verbose_name="Answer for the FAQ",
        max_length=500,
        blank=False,
        null=False,
        default="We will be Happy to answer once we have one :)"
    )

    def __str__(self) -> str:
        return self.question

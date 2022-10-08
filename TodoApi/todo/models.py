from django.db import models

class Todo(models.Model):
    class TodoState(models.TextChoices):
        En_cours = "EC"
        Attente = "AT"
        Fini = "FN"
        Abandonne = "AB"

    title = models.fields.CharField(max_length = 255)
    description = models.fields.TextField(max_length=1000)
    date_begin = models.fields.DateField()
    date_end = models.fields.DateField()
    state = models.fields.CharField(choices=TodoState.choices, max_length = 5)

    def __str__(self):
        return self.title
from django.db import models


# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.title


class HelpOffer(models.Model):
    task = models.ForeignKey(to=Task, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    additional_information = models.TextField

    def __str__(self):
        return self.name + " (" + self.task.title + ")"

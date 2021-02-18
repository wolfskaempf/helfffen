from django.db import models


# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=150)
    number_of_helpers_needed = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(blank=True, null=True)
    description = models.TextField()
    contact = models.TextField()

    def __str__(self):
        return self.title


class HelpOffer(models.Model):
    task = models.ForeignKey(to=Task, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    contact = models.TextField()
    additional_information = models.TextField(blank=True)

    def __str__(self):
        return self.name + " (" + self.task.title + ")"

from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=150)
    number_of_helpers_needed = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(blank=True, null=True)
    description = models.TextField()
    contact = models.TextField()

    def __str__(self):
        return self.title

    def helpers_needed(self):
        number_of_helpers = HelpOffer.objects.filter(task=self).count()
        if (self.number_of_helpers_needed - number_of_helpers) > 0:
            return True
        else:
            return False

    def number_of_helpers_needed_remaining(self):
        number_of_helpers = HelpOffer.objects.filter(task=self).count()
        number_of_helpers_needed_remaining = self.number_of_helpers_needed - number_of_helpers
        if number_of_helpers_needed_remaining > 0:
            return number_of_helpers_needed_remaining
        else:
            return 0

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('helfffen:task_show', args=[str(self.id)])


class HelpOffer(models.Model):
    task = models.ForeignKey(to=Task, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    contact = models.TextField()
    additional_information = models.TextField(blank=True)

    def __str__(self):
        return self.name + " (" + self.task.title + ")"

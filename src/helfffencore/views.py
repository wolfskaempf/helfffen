from django.shortcuts import get_object_or_404, render

from .forms import HelpOfferForm
from .models import Task


def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')

    context = {"tasks": tasks}

    return render(request, "task_list.html", context=context)


def task_show(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    # sent_offer indicates whether the person has just submitted an offer to help, used to show contact information
    sent_offer = False

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = HelpOfferForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form_instance = form.save(commit=False)
            form_instance.task = task
            sent_offer = True
            form_instance.save()
            form = HelpOfferForm()
    # if a GET (or any other method) we'll create a blank form
    else:
        form = HelpOfferForm()

    context = {"task": task, "form": form, "sent_offer": sent_offer}
    return render(request, "task_show.html", context=context)

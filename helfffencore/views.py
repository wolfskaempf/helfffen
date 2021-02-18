from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import Task
from .forms import HelpOfferForm


def task_list(request):
    tasks = get_list_or_404(Task)

    context = {"tasks": tasks}

    return render(request, "helfffencore/task_list.html", context=context)


def task_show(request, id):
    task = get_object_or_404(Task, pk=id)

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
    return render(request, "helfffencore/task_show.html", context=context)

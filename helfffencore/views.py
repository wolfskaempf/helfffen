from django.shortcuts import render

def task_list(request):
    context = None
    return render(request, "helfffencore/task_list.html", context=context)


def task_show(request, id):
    context = None
    return render(request, "helfffencore/task_show.html", context=context)
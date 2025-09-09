from django.shortcuts import render,redirect
from app_counter.models import Counter
from django.contrib.auth.decorators import login_required
from django.db.models import F



def index(request):

    counters = Counter.objects.filter(favorite=True)

    return render(
        request=request,
        template_name="app_counter/index.html",
        context={
            "counters": counters
        }
    )

@login_required
def counter(request):

    try:
        counters = Counter.objects.filter(user=request.user)
    except Counter.DoesNotExist:
        counters = None

    return render(request=request,template_name='app_counter/counter.html',context={"counters": counters})

@login_required
def counter_create(request):

    counter = Counter.objects.create(user=request.user)

    return redirect('app_counter:counter')

@login_required
def counter_inc(request,counter_id):
    counter = request.user.counters.filter(id=counter_id).update(value=F('value') + 1)

    return redirect('app_counter:counter')

@login_required
def counter_decr(request,counter_id):
    counter = request.user.counters.filter(id=counter_id).update(value=F('value') - 1)
    return redirect('app_counter:counter')

@login_required
def choose_favorite(request,counter_id):
    counters = request.user.counters.update(favorite=False)
    counter = request.user.counters.filter(id=counter_id).update(favorite=True)

    return redirect('app_counter:counter')


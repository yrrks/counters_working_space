from django.shortcuts import render,redirect
from app_counter.models import Counter
from django.contrib.auth.decorators import login_required
from django.db.models import F



def index(request):

    counters = Counter.objects.all()

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
        counter = Counter.objects.get(user=request.user)
    except Counter.DoesNotExist:
        counter = None

    return render(request=request,template_name='app_counter/counter.html',context={"counter": counter})

@login_required
def counter_create(request):
    if not request.user.counters.all():
        counter = Counter.objects.create(user=request.user)
        counter.save()
    return redirect('app_counter:counter')

@login_required
def counter_inc(request):
    counter = Counter.objects.filter(user=request.user).update(value=F('value') + 1)

    return redirect('app_counter:counter')

@login_required
def counter_decr(request):
    counter = Counter.objects.filter(user=request.user).update(value=F('value') - 1)
    return redirect('app_counter:counter')


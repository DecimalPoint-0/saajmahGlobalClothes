from django.shortcuts import render, get_object_or_404, redirect
from .models import Costume
from .forms import OrderForm


def contact(request):
    if request.method == 'POST':
        # simple contact handling: show thank you (no persistence)
        return render(request, 'store/contact_success.html')
    return redirect('store:index')


def index(request):
    costumes = Costume.objects.filter(available=True)
    return render(request, 'store/index.html', {'costumes': costumes})


def costume_detail(request, slug):
    costume = get_object_or_404(Costume, slug=slug)
    if request.method == 'POST':
        form = OrderForm(request.POST, costume=costume)
        if form.is_valid():
            order = form.save(commit=False)
            order.costume = costume
            order.save()
            return redirect('store:order_success')
    else:
        form = OrderForm(costume=costume)
    return render(request, 'store/detail.html', {'costume': costume, 'form': form})


def order_success(request):
    return render(request, 'store/order_success.html')

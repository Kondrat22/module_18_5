from django.shortcuts import render

def platform(request):
    context = {
        'title': 'Главная страница',
    }
    return render(request, template_name='task4/platform.html', context=context)

def shop(request):
    context = {
        'title': 'Каталог игр',
        'games': ['Герои 3', 'Герои 5', 'Кингс Баунти']
    }

    return render(request, template_name='task4/shop.html', context=context)

def bag(request):
    context = {
        'title': 'Корзина',
    }
    return render(request, template_name='task4/bag.html', context=context)
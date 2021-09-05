from django.shortcuts import render

from pages.models import Product, MyUser
import logging

logging.basicConfig(filename="info.log", level=logging.INFO)

current_user = None


def index(request):
    return render(request, 'index.html', {'current_user': current_user})


def login(request):
    if current_user is None:
        return render(request, 'login.html')
    else:
        logging.error("Неудачная попытка авторизации")
        return index(request)


def search(request):
    text = request.GET['text']
    for product in Product.objects.all():
        if text == product.bar_code:
            return product_page(request, product)
    logging.error("Неудачная попытка поиска bar_code =%s" % text)
    return index(request)


def product_page(request, product):
    return render(request, 'product_page.html', {'item': product})


def authorize(request):
    global current_user
    if current_user is None:
        users = MyUser.objects.all()
        for i in users:
            if i.check_username_and_password(request.POST['username'], request.POST['password']):
                current_user = i
        if current_user is None:
            logging.error("Неудачная попытка входа, неверные данные USERNAME - %s " % request.POST['username'])
            return login(request)
        else:
            return index(request)
    else:
        return index(request)


def registration(request):
    global current_user
    user = MyUser.objects.create(
        username=request.POST['username'], password=request.POST['password'])
    logging.info("Зарегистрирован новый пользователь USERNAME - %s" % request.POST['username'])
    current_user = user
    return login(request)


def profile(request):
    if current_user is None:
        return index(request)
    else:
        return render(request, 'profile.html', {'current_user': current_user})


def catalog_page(request):
    products = Product.objects.all()
    return render(request, 'catalog.html', {'products': products, 'current_user': current_user})


def contact_page(request):
    return render(request, 'contact.html', {'current_user': current_user})

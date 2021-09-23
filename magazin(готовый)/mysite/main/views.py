from django.shortcuts import render
from main.models import *

# Create your views here.

def indexHandler(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    return render(request, 'index.html', {'categories':categories, 'products':products})



def blankHandler(request):


    return render(request, 'blank.html', {})


def checkoutHandler(request):


    return render(request, 'checkout.html', {})



def productHandler(request,product_id):
    categories = Category.objects.all()
    postproduct = Product.objects.get(id=int(product_id))
    product_images = ProductImage.objects.filter(product__id = product_id)
    comment_items = CommentItem.objects.filter(product__id = product_id)


    comment_len = 0
    comment_summa = 0
    reating_orta = 0
    reating_1 = 0
    reating_2 = 0
    reating_3 = 0
    reating_4 = 0
    reating_5 = 0
    reating_1_progress = 0
    reating_2_progress = 0
    reating_3_progress = 0
    reating_4_progress = 0
    reating_5_progress = 0

    for comment in comment_items:
        comment_len += 1
        comment_summa += comment.rating
        if comment.rating == 1:
            reating_1 += 1
        elif comment.rating == 2:
            reating_2 += 1
        elif comment.rating == 3:
            reating_3 += 1
        elif comment.rating == 4:
            reating_4 += 1
        elif comment.rating == 5:
            reating_5 += 1
    if comment_len > 0:
        reating_orta = int(comment_summa / comment_len * 100.0)/100
        reating_1_progress = int(reating_1 / comment_len * 100)
        reating_2_progress = int(reating_2 / comment_len * 100)
        reating_3_progress = int(reating_3 / comment_len * 100)
        reating_4_progress = int(reating_4 / comment_len * 100)
        reating_5_progress = int(reating_5 / comment_len * 100)
    return render(request, 'product.html', {'postproduct': postproduct,
                                            'product_images': product_images,
                                            'comment_items': comment_items,
                                            'reating_orta': reating_orta,
                                            'reating_1': reating_1,
                                            'reating_2': reating_2,
                                            'reating_3': reating_3,
                                            'reating_4': reating_4,
                                            'reating_5': reating_5,
                                            'reating_1_progress': reating_1_progress,
                                            'reating_2_progress': reating_2_progress,
                                            'reating_3_progress': reating_3_progress,
                                            'reating_4_progress': reating_4_progress,
                                            'reating_5_progress': reating_5_progress,
                                            'categories':categories
                                            })
def storeHandler(request):
    search_value = request.GET.get('search', '')
    category_id = int(request.GET.get('category_id', 0))
    active_category = None
    print(request.GET)

    if category_id:
        if search_value:
            products = Product.objects.filter(category__id=category_id).filter(title__contains = search_value)
        else:
            products = Product.objects.filter(category__id=category_id)

        active_category = Category.objects.get(id=category_id)
    else:
        if search_value:
            products = Product.objects.filter(title__contains = search_value)
        else:
            products = Product.objects.all()

    categories = Category.objects.all()
    return render(request, 'store.html', {
        'products': products,
        'categories': categories,
        'active_category':active_category,
        'search_value':search_value
                                          })


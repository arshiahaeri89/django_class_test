from django.db.models import Avg, Max, Min
from django.shortcuts import render, get_object_or_404
from datetime import date
from .models import Product, Karbaran

posts = [
    {
        'slug': 'python-programing',
        'title': 'Python',
        'autor': 'Haeri',
        'image': 'python.jpeg',
        'date': date.today(),
        'short_description': 'Python is High Level Language and Open Source',
        'content': '''Lorem ipsum dolor sit amet, consectetur adipisicing 
                      elit. Atque, dolore fugit impedit inventore 
                      labore minus molestiae officiis quis soluta tempora.'''
    },
    {
        'slug': 'java-programing',
        'title': 'Java',
        'autor': 'Haeri',
        'image': 'java.png',
        'date': date.today(),
        'short_description': 'Java is Fully Object Oriented and has 4 editions: JavaSE, JavaEE, JavaME, Java Card',
        'content': '''Lorem ipsum dolor sit amet, consectetur adipisicing 
                      elit. Atque, dolore fugit impedit inventore 
                      labore minus molestiae officiis quis soluta tempora.'''
    },
    {
        'slug': 'js-programing',
        'title': 'JavaScript',
        'autor': 'Haeri',
        'image': 'js.png',
        'date': date(2021, 6, 8),
        'short_description': 'JavaScript is a object-oriented language using ES Rules',
        'content': '''Lorem ipsum dolor sit amet, consectetur adipisicing 
                      elit. Atque, dolore fugit impedit inventore 
                      labore minus molestiae officiis quis soluta tempora.'''
    },
    {
        'slug': 'cpp-programing',
        'title': 'C++',
        'autor': 'Haeri',
        'image': 'cpp.png',
        'date': date(2022, 5, 20),
        'short_description': 'C++ is Better C and very very very very useful',
        'content': '''Lorem ipsum dolor sit amet, consectetur adipisicing 
                      elit. Atque, dolore fugit impedit inventore 
                      labore minus molestiae officiis quis soluta tempora.'''
    },
    {
        'slug': 'html-programing',
        'title': 'HTML',
        'autor': 'Haeri',
        'image': 'html.png',
        'date': date(2023, 6, 6),
        'short_description': 'HTML is HyperText Markup Language used to transfer pages in HTTP protocol',
        'content': '''Lorem ipsum dolor sit amet, consectetur adipisicing 
                      elit. Atque, dolore fugit impedit inventore 
                      labore minus molestiae officiis quis soluta tempora.'''
    }
]


def get_date(post):
    return post['date']


def all_posts(request):
    return render(request, 'blog/posts.html', {'posts': posts})


def single_post(request, slug):
    post = next(post for post in posts if post['slug'] == slug)
    context = {'post': post}
    return render(request, 'blog/post_details.html', context)


def index(request):
    sorted_post = sorted(posts, key=get_date)
    context = {'posts': sorted_post[-2:]}
    return render(request, 'blog/index.html', context=context)


def karbaran_list(request):
    users = Karbaran.objects.all()
    context = {'users': users}
    return render(request, 'blog/karbaran_list.html', context=context)


def product_list(request):
    products = Product.objects.all()
    number_of_product = products.count()
    info = products.aggregate(Avg('price'), Max('price'), Min('price'), Max('rate'))
    context = {'products': products, 'count': number_of_product, 'info': info}
    return render(request, 'blog/product_list.html', context=context)


def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {'product': product}
    return render(request, 'blog/product_details.html', context=context)

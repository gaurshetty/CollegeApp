from django.shortcuts import render
from .models import *
from .serviceimpl import *


def home(req):
    return render(req, 'home.html')


def home_book(req):
    context = {
        'book': BookCurdOps.get_dummy_book(),
        'books': BookCurdOps.get_book_with_authors(),
        'publications': Publication.objects.all(),
        'authorlist': Author.objects.all(),
    }
    return render(req, 'book.html', context)


def save_update_book(req):
    if req.method == 'POST':
        rd = req.POST
        bk = Book(id=rd['id'], name=rd['name'], price=rd['price'],
                  quantity=rd['quantity'], publication_id=rd['pub'])
        msg = BookCurdOps.save_update_book(bk)
        bid = msg[1]
        b1 = Book.objects.get(id=bid)
        atrs = req.POST.getlist('authorlist')
        for atr in atrs:
            b1.authorsref.add(Author.objects.get(id=int(atr)))
            b1.save()
    context = {
        'book': BookCurdOps.get_dummy_book(),
        'books': BookCurdOps.get_book_with_authors(),
        'publications': Publication.objects.all(),
        'authorlist': Author.objects.all(),
        'actionmsg': msg[0]
    }
    return render(req, 'book.html', context)


def edit_book(req, id):
    context = {
        'book': BookCurdOps.get_single_book(id),
        'books': BookCurdOps.get_book_with_authors(),
        'publications': Publication.objects.all(),
        'authorlist': Author.objects.all(),
    }
    return render(req, 'book.html', context)


def delete_book(req, id):
    msg = BookCurdOps.delete_book(id)
    context = {
        'book': BookCurdOps.get_dummy_book(),
        'books': BookCurdOps.get_book_with_authors(),
        'publications': Publication.objects.all(),
        'authorlist': Author.objects.all(),
        'actionmsg': msg
    }
    return render(req, 'book.html', context)


def home_author(req):
    context = {
        'author': AuthorCurdOps.get_dummy_author(),
        'authors': AuthorCurdOps.get_list_authors(),
    }
    return render(req, 'author.html', context)


def save_update_author(req):
    if req.method == 'POST':
        rd = req.POST
        atr = Author(id=rd['id'], name=rd['name'],
                     age=rd['age'], email=rd['email'])
        msg = AuthorCurdOps.save_update_author(atr)
    context = {
        'author': AuthorCurdOps.get_dummy_author(),
        'authors': AuthorCurdOps.get_list_authors(),
        'actionmsg': msg
    }
    return render(req, 'author.html', context)


def edit_author(req, id):
    context = {
        'author': AuthorCurdOps.get_single_author(id),
        'authors': AuthorCurdOps.get_list_authors(),
    }
    return render(req, 'author.html', context)


def delete_author(req, id):
    msg = AuthorCurdOps.delete_author(id)
    context = {
        'author': AuthorCurdOps.get_dummy_author(),
        'authors': AuthorCurdOps.get_list_authors(),
        'actionmsg': msg
    }
    return render(req, 'author.html', context)


def home_publication(req):
    context = {
        'publication': PublicationCurdOps.get_dummy_publication(),
        'publications': PublicationCurdOps.get_list_publications(),
        'authors': Author.objects.all(),
    }
    return render(req, 'publication.html', context)


def save_update_publication(req):
    if req.method == 'POST':
        rd = req.POST
        atr = Publication(id=rd['id'], name=rd['name'],
                          year=rd['year'], author_id=rd['author'])
        msg = PublicationCurdOps.save_update_publication(atr)
    context = {
        'publication': PublicationCurdOps.get_dummy_publication(),
        'publications': PublicationCurdOps.get_list_publications(),
        'authors': Author.objects.all(),
        'actionmsg': msg
    }
    return render(req, 'publication.html', context)


def edit_publication(req, id):
    context = {
        'publication': PublicationCurdOps.get_single_publication(id),
        'publications': PublicationCurdOps.get_list_publications(),
        'authors': Author.objects.all()
    }
    return render(req, 'publication.html', context)


def delete_publication(req, id):
    msg = PublicationCurdOps.delete_publication(id)
    context = {
        'publication': PublicationCurdOps.get_dummy_publication(),
        'publications': PublicationCurdOps.get_list_publications(),
        'authors': Author.objects.all(),
        'actionmsg': msg
    }
    return render(req, 'publication.html', context)


def home_address(req):
    context = {
        'address': AddressCurdOps.get_dummy_address(),
        'addresses': AddressCurdOps.get_list_addresses(),
        'authors': Author.objects.all(),
    }
    return render(req, 'address.html', context)


def save_update_address(req):
    if req.method == 'POST':
        rd = req.POST
        atr = Address(id=rd['id'], city=rd['city'], state=rd['state'],
                      pincode=rd['pincode'], author_id=rd['author'])
        msg = AddressCurdOps.save_update_address(atr)
    context = {
        'address': AddressCurdOps.get_dummy_address(),
        'addresses': AddressCurdOps.get_list_addresses(),
        'authors': Author.objects.all(),
        'actionmsg': msg
    }
    return render(req, 'address.html', context)


def edit_address(req, id):
    context = {
        'address': AddressCurdOps.get_single_address(id),
        'addresses': AddressCurdOps.get_list_addresses(),
        'authors': Author.objects.all(),
    }
    return render(req, 'address.html', context)


def delete_address(req, id):
    msg = AddressCurdOps.delete_address(id)
    context = {
        'address': AddressCurdOps.get_dummy_address(),
        'addresses': AddressCurdOps.get_list_addresses(),
        'authors': Author.objects.all(),
        'actionmsg': msg
    }
    return render(req, 'address.html', context)

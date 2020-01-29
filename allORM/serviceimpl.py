from .models import *


class BookCurdOps:
    @staticmethod
    def get_book_with_authors():
        books = Book.objects.all()
        all_book_info = []
        for book in books:
            book1 = book.__dict__
            ars = book.authorsref.all()
            pub = book.publication
            book1['publication'] = pub
            arslist = []
            if ars:
                for ar in ars:
                    arslist.append(ar)
            book1['authors'] = arslist
            all_book_info.append(book1)
        return all_book_info

    @staticmethod
    def get_list_books():
        return Book.objects.all()

    @staticmethod
    def get_single_book(id):
        return Book.objects.get(id=id)

    @staticmethod
    def get_dummy_book():
        return Book(id=0, name='', price=0, quantity=0, publication_id=0)

    @staticmethod
    def save_update_book(bk):
        if bk.id == '0':
            Book.objects.create(name=bk.name, price=bk.price,
                                quantity=bk.quantity, publication_id=bk.publication_id)
            return "Record added successfully..!"
        else:
            bk.save()
            return "Record updated successfully..!"

    @staticmethod
    def delete_book(id):
        dbbk = BookCurdOps.get_single_book(id)
        if dbbk:
            dbbk.delete()
            return "Record deleted successfully..!"
        return "Record cannot delete as no record for given id..."


class AuthorCurdOps:
    @staticmethod
    def get_list_authors():
        return Author.objects.all()

    @staticmethod
    def get_single_author(id):
        return Author.objects.get(id=id)

    @staticmethod
    def get_dummy_author():
        return Author(id=0, name='', age=0, email='')

    @staticmethod
    def save_update_author(atr):
        if atr.id == '0':
            Author.objects.create(name=atr.name, age=atr.age, email=atr.email)
            return "Record added successfully..!"
        else:
            atr.save()
            return "Record updated successfully..!"

    @staticmethod
    def delete_author(id):
        dbar = AuthorCurdOps.get_single_author(id)
        if dbar:
            dbar.delete()
            return "Record deleted successfully..!"
        return "Record cannot delete as no record for given id..."


class PublicationCurdOps:
    @staticmethod
    def get_list_publications():
        return Publication.objects.all()

    @staticmethod
    def get_single_publication(id):
        return Publication.objects.get(id=id)

    @staticmethod
    def get_dummy_publication():
        return Publication(id=0, name='', year=0, author_id=0)

    @staticmethod
    def save_update_publication(pub):
        if pub.id == '0':
            Publication.objects.create(
                name=pub.name, year=pub.year, author_id=pub.author_id)
            return "Record added successfully..!"
        else:
            pub.save()
            return "Record updated successfully..!"

    @staticmethod
    def delete_publication(id):
        dbar = PublicationCurdOps.get_single_publication(id)
        if dbar:
            dbar.delete()
            return "Record deleted successfully..!"
        return "Record cannot delete as no record for given id..."


class AddressCurdOps:
    @staticmethod
    def get_list_addresses():
        return Address.objects.all()

    @staticmethod
    def get_single_address(id):
        return Address.objects.get(id=id)

    @staticmethod
    def get_dummy_address():
        return Address(id=0, city='', state='', pincode=0, author_id=0)

    @staticmethod
    def save_update_address(adr):
        if adr.id == '0':
            dbart = Address.objects.filter(author_id=adr.author_id)
            if dbart:
                return "Cannot save...! Author already asigned to other address"
            Address.objects.create(
                city=adr.city, state=adr.state, pincode=adr.pincode, author_id=adr.author_id)
            return "Record added successfully..!"
        else:
            upadr = Address.objects.get(id=adr.id)
            if upadr.author_id != adr.author_id and Address.objects.filter(author_id=adr.author_id):
                return "Cannot update...! Author already asigned to other address"
            adr.save()
            return "Record updated successfully..!"

    @staticmethod
    def delete_address(id):
        dbar = AddressCurdOps.get_single_address(id)
        if dbar:
            dbar.delete()
            return "Record deleted successfully..!"
        return "Record cannot delete as no record for given id..."

    @staticmethod
    def unsigned_authors():
        adrlist = Address.objects.all()
        authorlist = Author.objects.all()

        assigned_authors = []
        for adr in adrlist:
            assigned_authors.append(adr.author_id)

        unsigned = []
        for author in authorlist:
            if author.id not in assigned_authors:
                unsigned.append(author)

        return unsigned

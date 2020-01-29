from django.db import models

'''
11 author - address *
1M pub - book *
M1 author * - pub
MM book - author *
'''


class Book(models.Model):
    name = models.CharField('name', max_length=100)
    price = models.FloatField('price')
    quantity = models.IntegerField('quantity')
    publication = models.ForeignKey(
        'Publication', on_delete=models.CASCADE, null=True, related_name='booksref')

    def __str__(self):
        return f'{self.__dict__}'
        # return f'Id : {self.id}, Name : {self.name}, Price : {self.price}, Quantity : {self.quantity}, Publication_id : {self.Publication_id}'

    def __repr__(self):
        return str(self)

    # def as_dict(self):
    #     return dict((f.name, getattr(self, f.name)) for f in self._meta.fields)
# Book(id=101, name='BXE', price=350.00, quantity=200, publication_id=11)


class Author(models.Model):
    name = models.CharField('name', max_length=100)
    age = models.IntegerField('age')
    email = models.EmailField('email')
    books = models.ManyToManyField(Book, related_name='authorsref')

    def __str__(self):
        return f'{self.__dict__}'
        # return f'Id : {self.id}, Name : {self.name}, Age : {self.age}, Email : {self.email}'

    def __repr__(self):
        return str(self)

# Author(id=1, name='shetty', age=26, email='shetty@gmail.com')


class Publication(models.Model):
    name = models.CharField('name', max_length=100)
    year = models.IntegerField('year')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='pubref')

    def __str__(self):
        return f'{self.__dict__}'
        # return f'Id : {self.id}, Name : {self.name}, Year : {self.year}, author_id : {self.author_id}'

    def __repr__(self):
        return str(self)

# Publication(id=11, name='TechOne', year=2008, author_id=1)


class Address(models.Model):
    city = models.CharField('city', max_length=100)
    state = models.CharField('state', max_length=100)
    pincode = models.IntegerField('pincode')
    author = models.OneToOneField(Author, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.__dict__}'
        # return f'Id : {self.id}, City : {self.city}, State : {self.state}, Pincode : {self.pincode}, Author_id : {self.author_id}'

    def __repr__(self):
        return str(self)

# Address(id=201, city='Pune', state='MH', pincode=411041, author_id=1)

# a1 = Author.objects.get(id=1)
# b1 = Book.objects.get(id=101)
# a1.books.add(b1)
# a1.save()
# allorm_author_books(id=301, author_id=1, book_id=101)

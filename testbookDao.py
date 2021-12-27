from BookDao import bookDao


book = {
    'ISBN':1234567,
    'price': 12,
    'author': 'Stephen King',
    'title': 'The Shining'

}
returnvalue = bookDao.create(book)
print(returnvalue)
from flask import Blueprint, jsonify, request

router = Blueprint('books', 'books', url_prefix='/books')

DATAS = {}

@router.get('/')
def get_book_list():
    book_list = []
    for key, book in DATAS.items():
        book_list.append(book)

    return jsonify({'result': book_list})

@router.post('/')
def create_book():
    data = request.get_json()
    bookname = data.get('bookname')
    author = data.get('author')
    year = data.get('year')
    DATAS[f'{bookname} {author}'] = {'bookname':bookname, 'author': author, 'year':year}
    return jsonify({'result': 'success'})
from flask import Blueprint, jsonify

router = Blueprint('users', 'users', url_prefix='/users')

@router.get('/')
def get_user_list():
    return jsonify({'result': []})

@router.post('/')
def create_user_list():
    return jsonify({'result': 'success'})
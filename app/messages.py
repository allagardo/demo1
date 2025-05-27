from flask import Blueprint, jsonify

router = Blueprint('messages', 'messages', url_prefix='/messages')

@router.get('/')
def get_messages_list():
    return jsonify({'result': []})

@router.post('/')
def create_messages_list():
    return jsonify({'result': 'success'})

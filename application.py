from flask import Flask, Response, jsonify
from app import users_router
from app import messages_router
from app import books_router
import logging

logging.


app = Flask(__name__)
app.register_blueprint(users_router)
app.register_blueprint(messages_router)
app.register_blueprint(books_router)

@app.errorhandler(ZeroDivisionError)
def zero_div_error(error):
    return jsonify({'error': 'Не удалось получить ответ'}), 403
app.register_error_handler(403,zero_div_error )


if __name__ =='__main__':
    app.run()

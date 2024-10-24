from flask import Flask, render_template
from models import db, Book, Genre
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Инициализация базы данных
db.init_app(app)

with app.app_context():
    db.create_all()
# Главная страница: вывод последних 15 книг

@app.route('/book/<int:book_id>')
def book_detail(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template('book_detail.html', book=book)


@app.route('/')
def index():
    books = Book.query.order_by(Book.created_at.desc()).limit(15).all()
    return render_template('index.html', books=books)

# Страница жанра: вывод книг по жанру
@app.route('/genre/<int:genre_id>')
def genre(genre_id):
    genre = Genre.query.get_or_404(genre_id)
    books = Book.query.filter_by(genre_id=genre.id).order_by(Book.created_at.desc()).all()
    return render_template('genre.html', genre=genre, books=books)

if __name__ == '__main__':


    # with app.app_context():
    # db.create_all()  # Создать таблицы, если их нет
    app.run(debug=True)
from flask import Flask, render_template, flash, redirect, url_for
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Главная страница
@app.route('/')
@app.route('/home')  # Добавляем альтернативный маршрут
def home():
    flash('Добро пожаловать на главную страницу!', 'info')
    news = [
        {'title': 'Новый продукт', 'text': 'Мы запустили новый продукт...', 'date': '15.10.2023'},
        {'title': 'Обновление сайта', 'text': 'Мы обновили дизайн сайта...', 'date': '10.10.2023'}
    ]
    return render_template('home.html', news=news, current_year=datetime.now().year)

# Страница "О нас"
@app.route('/about')
def about():
    team = [
        {'name': 'Иван Иванов', 'position': 'Основатель и CEO', 'bio': 'Опыт работы 15 лет...'},
        {'name': 'Петр Петров', 'position': 'Технический директор', 'bio': 'Специалист в области...'},
        {'name': 'Сергей Сергеев', 'position': 'Дизайн-директор', 'bio': 'Эксперт в UX/UI...'}
    ]
    return render_template('about.html',
                         team=team,
                         current_year=datetime.now().year,
                         company_info={
                             'founded': 2010,
                             'employees': 50,
                             'clients': 200
                         })

# Обработчик 404 ошибки
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
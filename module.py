import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    try:
        books = pd.read_csv(file_path)
        return books
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None
    except pd.errors.EmptyDataError:
        print("Файл порожній.")
        return None
    except pd.errors.ParserError:
        print("Некоректний формат CSV файлу.")
        return None

def add_new_book(books, book):
    try:
        books.loc[len(books)] = book
        return books
    except Exception as e:
        print(f"Невірний тим введення даних: {str(e)}")

def remove_book_by_name(books, name):  
    try:
        if name not in books['Назва'].values:
            print("Продукт не знайдено.")
            return books
        books = books.drop(books[books['Назва'] == name].index)
        return books
    except Exception as e:
        print(f"Помилка при видаленні книги: {str(e)}")
        
def plot_histogram_books_by_year(books):
    try:
        books['Рік видання'].plot(kind='hist', bins=20)
        plt.xlabel("Рік видання")
        plt.ylabel("Частота")
        plt.title("Гістограма кількості книг за роками видання")
        plt.show()
    except Exception as e:
        print(f"Помилка при створенні гістограми {str(e)}")
        
def calculate_all_books_in_library(books):
    if books is not None:
        total_quantity = books['Кількість примірників'].sum() 
        print(f"Загальна кількість продуктів: {total_quantity}")
    else:
        print("Помилка: бібліотека порожня.")

def display_info(books):
    if books is not None:
        print(books)
    else:
        print("Бібліотека порожня!")

def load_data_from_file(): 
    file_path = "C:/Users/Vlad/Desktop/PYTHON/pandas/books.csv" 
    books = load_data(file_path)
    if books is not None:
        display_info(books)
    return books

def save_data(books, file_path): 
    try:
        books.to_csv(file_path, index=False)
        print(f"Дані збережено у  {file_path}!")
    except Exception as e:
        print(f"помилка, дані не збережено: {str(e)}")
        
def save_data_to_file(books): 
    if books is not None:
        file_path = "C:/Users/Vlad/Desktop/PYTHON/pandas/books.csv"  
        save_data(books, file_path)
    else:
        print("Помилка при зберіганні даних!")
        
def add_product(books): 
    if books is not None:
        try:
            name = input("Введіть назву книги: ")
            author = input("Введіть автора книги: ")
            year = int(input("Введіть рік видання: "))
            genre = input("Введіть жанр книги: ")
            quantity = float(input("Введіть кількість примірників: "))
            book = {'Назва': name, 'Автор': author, 'Рік видання': year, 'Жанр': genre, 'Кількість примірників': quantity}
            books = add_new_book(books, book)
            display_info(books)
            save_data_to_file(books)
        except ValueError:
            print("Невірні дані")
    else:
        print("Пуста бібліотека")

def remove_product(books):
    if books is not None:
        name = input("Введіть назву продукту для видалення: ")
        books = remove_book_by_name(books, name)
        display_info(books)
        save_data_to_file(books)
    else:
        print("Помилка")

def plot_price_histogram(books):  
    if books is not None:
        plot_histogram_books_by_year(books)
    else:
        print("Помилка")

def find_book_by_name(books):
    if books is not None:
        name = input("Введіть назву книги для пошуку: ")
        if name in books['Назва'].values:
            print(books[books['Назва'] == name])
        else:
            print("Книга не знайдена")
    else:
        print("Помилка")
        
def most_popular_genres(books):
    if books is not None:
        genres = books.groupby('Жанр')['Кількість примірників'].sum().sort_values(ascending=False)
        print("Список найпопулярніших жанрів:")
        print(genres)
    else:
        print("Помилка")

def most_popular_genres(books):
    if books is not None:
        genres = books.groupby('Жанр')['Кількість примірників'].sum().sort_values(ascending=False)
        print("Список найпопулярніших жанрів:")
        print(genres)
    else:
        print("Помилка")

def plot_pie_chart_books_by_genre(books):
    if books is not None:
        genres = books.groupby('Жанр')['Кількість примірників'].sum().sort_values(ascending=False)
        plt.pie(genres, labels=genres.index, autopct='%1.1f%%')
        plt.title('Розподіл книг за жанрами')
        plt.show()
    else:
        print("Помилка")

def main():
    books = load_data_from_file()
    
    while True:
        print("\nМеню:")
        print("1. Додати книгу")
        print("2. Видалити книгу")
        print("3. Показати список книг")
        print("4. Знайти книгу по назві")
        print("5. Обчислити загальну кількість книг")
        print("6. Вивести список найпопулярніших жанрів")
        print("7. Намалювати гістограму кількості книг за роками видання")
        print("8. Намалювати кругову діаграму розподілу книг за жанрами")
        print("9. Вийти і зберегти дані")
        
        choice = input("Виберіть пункт меню: ")

        if choice == "1":
            add_product(books)
        elif choice == "2":
            remove_product(books)
        elif choice == "3":
            display_info(books)
        elif choice == "4":
            find_book_by_name(books)
        elif choice == "5":
            calculate_all_books_in_library(books)
        elif choice == "6":
            most_popular_genres(books)
        elif choice == "7":
            plot_histogram_books_by_year(books)
        elif choice == "8":
            plot_pie_chart_books_by_genre(books)
        elif choice == "9":
            break
        else:
            print("Невірний вибір.")

if __name__ == "__main__":
    main()
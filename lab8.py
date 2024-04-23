import requests
from bs4 import BeautifulSoup

# Функция для отправки GET-запроса на веб-страницу и получения HTML-кода
def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Не удалось получить HTML с {url}")
        return None

# Функция для извлечения данных из HTML-кода с использованием BeautifulSoup
def extract_data(html):
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        # Извлекаем заголовок страницы и все абзацы
        title = soup.title.text
        paragraphs = [p.text for p in soup.find_all('p')]
        return title, paragraphs
    else:
        return None, None

# Функция для подсчета количества слов в абзацах
def count_words(paragraphs):
    if paragraphs:
        word_counts = [len(p.split()) for p in paragraphs]
        return word_counts
    else:
        return None

# Функция для вывода данных на экран
def display_data(title, paragraphs, word_counts):
    if title and paragraphs and word_counts:
        print("Заголовок:", title)
        print("Абзацы:")
        for i, p in enumerate(paragraphs):
            print(f"{i + 1}. {p} (Количество слов: {word_counts[i]})")
    else:
        print("Нет данных для отображения")

def main():
    url = 'https://example.com'  # Замените URL на адрес нужной вам веб-страницы
    html = fetch_html(url)
    title, paragraphs = extract_data(html)
    word_counts = count_words(paragraphs)
    display_data(title, paragraphs, word_counts)

if __name__ == "__main__":
    main()


import requests

def fetch_random_book():
    url = 'https://api.freeapi.app/api/v1/public/books/book/random'
    response = requests.get(url)
    data = response.json()

    if data['success'] and 'data' in data:
        book_data = data['data']
        book_id = book_data['id']
        book_title = book_data['volumeInfo']['title']
        book_subtitle = book_data['volumeInfo']['subtitle']
        book_author = book_data['volumeInfo']['authors'][0]
        return book_id, book_title, book_subtitle, book_author
    else:
        raise Exception('Failed to fetch book details')



def main():
    try:
        book_id, book_title, book_subtitle, book_author = fetch_random_book()
        print(f'''
            Book ID: {book_id}.
            Book Title: {book_title}.
            Book Subtitle: {book_subtitle}.
            Book Author: {book_author}
            ''')
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    main()
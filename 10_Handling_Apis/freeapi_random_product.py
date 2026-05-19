import requests

def random_prodcut_api():
    url = 'https://api.freeapi.app/api/v1/public/randomproducts/product/random'

    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data['data']
        product_id = user_data['id']
        product_title = user_data['title']
        product_desc = user_data['description']
        product_price = user_data['price']
        return product_id, product_title, product_desc, product_price
    else:
        raise Exception('Failed to fetch product details')

def main():
    try:
        product_id, product_title, product_desc, product_price = random_prodcut_api()
        print(f'Product ID: {product_id}.\nProduct Title: {product_title}.\nProduct Description: {product_desc}.\nProduct Price: RS-{product_price}')
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    main()
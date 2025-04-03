import requests

def img_upload(url:str="http://127.0.0.1:8080/upload", filename:str="image.jpeg"):
    files = {"image": open(filename, "rb")}
    response = requests.post(url, files=files)
    if response.status_code == 201:
        print("Файл завантажен")
    else:
        print("Помилка завантаження:", response.status_code, response.text)


def img_url_request(filename:str="image.jpeg"):
    url = f"http://127.0.0.1:8080/image/{filename}"
    headers = {"Content-Type": "text"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print (f"Лінк запитуємого файлу {(response.json()).get('image_url')}")
    else:
        print("Помилка запиту:", response.status_code, response.text)


def img_delleting(filename:str="image.jpeg"):
    url = f"http://127.0.0.1:8080/delete/{filename}"
    response = requests.delete(url)
    if response.status_code == 200:
        print (f"Файл видален")
    else:
        print("Помилка запиту:", response.status_code, response.text)


if __name__ == "__main__":
    img_upload()
    img_url_request()
    img_delleting()
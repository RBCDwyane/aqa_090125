'''
Є вiдкритий API NASA який дозволяє за певними параметрами отримати данi у виглядi JSON про
фото зробленi ровером “Curiosity” на Марсi. Серед цих даних є посилання на фото якi потрiбно
розпарсити i потiм за допомогою додаткових запитiв скачати i зберiгти цi фото як локальнi файли
mars_photo1.jpg , mars_photo2.jpg . Завдання потрiбно зробити використовуючи модуль requests
'''

import requests

def img_download(url, params):
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print(f"Помилка запиту: {response.status_code}")
        return

    for photo in response.json().get("photos", []):
        img_url = photo["img_src"]
        filename = img_url.split("/")[-1]
        img_response = requests.get(img_url)

        if img_response.status_code == 200:
            with open(filename, "wb") as file:
                file.write(img_response.content)
            print(f"{filename} збережено")
        else:
            print(f"Помилка при скачуванні: {img_url}")


if __name__ == "__main__":
    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
    params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}
    img_download(url, params)



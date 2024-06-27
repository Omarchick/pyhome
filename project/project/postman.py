import requests

class GoogleRequest:
    def __init__(self):
        self.base_url = "https://www.google.com"

    def send_get_request(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, params=params)
        return response

    def send_post_request(self, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, data=data)
        return response

# Пример использования
if __name__ == "__main__":
    google = GoogleRequest()

    # Отправка GET запроса на главную страницу Google
    response = google.send_get_request("/")
    print("GET запрос:")
    print(response.status_code)
    print(response.text[:500])  # Вывод первых 500 символов текста ответа

    # Пример отправки POST запроса (что не является стандартной практикой для Google)
    # Здесь, как правило, POST запросы на главную страницу Google будут отклонены или перенаправлены.
    response = google.send_post_request("/", data={"key": "value"})
    print("POST запрос:")
    print(response.status_code)
    print(response.text[:500])  # Вывод первых 500 символов текста ответа

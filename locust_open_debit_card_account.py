from locust import HttpUser, between, task

from tools.fakers import fake  # генератор случайных данных


class OpenDebitCardAccountScenarioUser(HttpUser):
    # Пауза между запросами для каждого виртуального пользователя (в секундах)
    wait_time = between(1, 3)

    user_id: str = None

    def on_start(self) -> None:
        """
        Метод on_start вызывается один раз при запуске каждой сессии виртуального пользователя.
        Здесь мы создаем нового пользователя, отправляя POST-запрос к /api/v1/users.
        """
        request = {
            "email": fake.email(),
            "lastName": fake.last_name(),
            "firstName": fake.first_name(),
            "middleName": fake.middle_name(),
            "phoneNumber": fake.phone_number()
        }
        response = self.client.post("/api/v1/users", json=request)

        # Сохраняем полученные данные, включая ID пользователя
        response_data = response.json()
        self.user_id = response_data["user"]["id"]

    @task
    def open_debit_card_account(self):
        """
        Основная нагрузочная задача: открытие дебетового счёта для пользователя.
        Отправляет POST-запрос к /api/v1/accounts/open-debit-card-account,
        передавая user_id в теле запроса.
        """

        account_data = {
            "user_id": self.user_id,
            "account_type": "debit"
        }

        self.client.post(
            "/api/v1/accounts/open-debit-card-account",
            json=account_data,
            name="accounts/open-debit-card-account"
        )




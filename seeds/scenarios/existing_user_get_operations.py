from seeds.scenario import SeedsScenario
from seeds.schema.plan import SeedOperationsPlan, SeedAccountsPlan, SeedUsersPlan, SeedsPlan


class ExistingUserGetOperationsSeedsScenario(SeedsScenario):
    """
    Сценарий сидинга для существующего пользователя, который:
    - открывает кредитный счёт
    - выполняет 5 операций покупки
    - выполняет операцию пополнения счёта
    - выполняет операцию снятия наличных
    Создаём 300 пользователей, каждому из которых открываются дебетовый счёт.
    """

    @property
    def plan(self) -> SeedsPlan:
        """
        Возвращает план сидинга для создания пользователей и их счетов.
        Мы создаём 300 пользователей, каждый получит кредитный счёт.
        """
        return SeedsPlan(
            users=SeedUsersPlan(
                count=300, # Создаём 300 пользователей
                credit_card_accounts=SeedAccountsPlan(count=1), # У каждого пользователя создаётся 1 кредитный счёт.
                purchase_operations=SeedOperationsPlan(count=5), # генерируются 5 операций покупки.
                top_up_operations=SeedOperationsPlan(count=1), # генерируются 1 операция пополнения счёта
                cash_withdrawal_operations=SeedOperationsPlan(count=1) # генерируются 1 операция снятия наличных.
            )
        )

    @property
    def scenario(self) -> str:
        """
        Возвращает название сценария сидинга.
        Это имя будет использоваться для сохранения данных сидинга.
        """
        return "existing_user_get_operations"


if __name__ == '__main__':
    """
    Запуск сценария сидинга вручную.
    Создаём объект сценария и вызываем метод build для создания данных.
    """
    seeds_scenario = ExistingUserGetOperationsSeedsScenario()
    seeds_scenario.build() # Запуск сидинга

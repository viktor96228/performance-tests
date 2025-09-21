from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient


class CreateCardsIssueCardRequestDict(TypedDict):
    """
        Структура данных для создания  карты.
        """
    userId: str
    accountId: str

class CardsGatewayHTTPClient(HTTPClient):

    def create_issue_virtual_card_api(self, request: CreateCardsIssueCardRequestDict) -> Response:
        """
        Метод для создания виртуальной карты.

        return: Ответ сервера
        """
        return self.post("/api/v1/cards/issue-virtual-card", json=request)

    def issue_physical_card_api(self, request: CreateCardsIssueCardRequestDict) -> Response:
        """
        Метод для выпуска физической карты.

        return: Ответ сервера
        """
        return self.post("/api/v1/cards/issue-physical-card", json=request)

from typing import TypedDict

from httpx import Response, QueryParams

from clients.http.client import HTTPClient




class GetOperationsQueryDict(TypedDict):
    accountId: str

class MakeFeeOperationRequestDict(TypedDict):
    status: str
    amount: str
    cardId: str
    accountId: str
    """
    Создание операции комиссии
    """
class MakeTopUpOperationRequestDict(TypedDict):
    status: str
    amount: str
    cardId: str
    accountId: str
    """
    Создание операции пополнения.
    """
class MakeCashbackOperationRequestDict(TypedDict):
    status: str
    amount: str
    cardId: str
    accountId: str
    """
    Создание операции кэшбэка.
    """
class MakeTransferOperationRequestDict(TypedDict):
    status: str
    amount: str
    cardId: str
    accountId: str
    """
    Создание операции перевода.
    """
class MakePurchaseOperationRequestDict(TypedDict):
    status: str
    amount: str
    cardId: str
    accountId: str
    category: str
    """
    Создание операции покупки.
    """
class MakeBillPaymentOperationRequestDict(TypedDict):
    status: str
    amount: str
    cardId: str
    accountId: str
    """
    Создание операции оплаты по счету
    """
class MakeCashWithdrawalOperationRequestDict(TypedDict):
    status: str
    amount: str
    cardId: str
    accountId: str
    """
    Создание операции снятия наличных денег.
    """

class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Получение информации об операции по operation_id..

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получение чека по операции по operation_id.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Получение списка операций для определенного счета.

        :param account_id: Идентификатор счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get("/api/v1/operations", params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Получение статистики по операциям для определенного счета.

        :param account_id: Идентификатор счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get("/api/v1/operations/operations-summary",params=QueryParams(**query))

    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        """
        Post запрос создание операции комиссии.
        :param request: Идентификатор учетной записи
        :return:Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """
        Post запрос создание операции пополнения.
        :param request: Идентификатор учетной записи
        :return:Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        """
        Post запрос создание операции кэшбэка.
        :param request: Идентификатор учетной записи
        :return:Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        """
        Post запрос создание операции перевода.
        :param request: Идентификатор учетной записи
        :return:Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Post запрос создание операции покупки.
        :param request: Идентификатор учетной записи
        :return:Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict) -> Response:
        """
        Post запрос создание операции оплаты по счету.
        :param request: Идентификатор учетной записи
        :return:Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestDict) -> Response:
        """
        Post запрос создание операции снятия наличных денег.
        :param request: Идентификатор учетной записи
        :return:Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)









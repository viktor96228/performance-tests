from enum import StrEnum

from pydantic import BaseModel, HttpUrl, Field, ConfigDict
from unicodedata import category


class OperationType(StrEnum):
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class OperationStatus(StrEnum):
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"

# Добавили описание структуры операций
class OperationSchema(BaseModel):
    id: str
    type: OperationType
    status: OperationStatus
    amount:float
    card_Id: str = Field(alias="cardId")
    category: str = Field(alias="category")
    createdAt: str = Field(alias="createdAt")
    account_Id: str = Field(alias="accountId")

# Добавили описание структуры квитанции заданной операции
class OperationReceiptSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    url: str = Field(alias="url")
    document: str = Field(alias="document")

# Добавили описание структуры статистики по операциям
class OperationsSummarySchema(BaseModel):
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float


# Добавили описание структуры получения  операции.
class GetOperationResponseSchema(BaseModel):
    operations: OperationSchema


class GetOperationsQuerySchema(BaseModel):
    """
    Структура query параметров запроса для получения списка операций по счёту.
    """
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")


class GetOperationsResponseSchema(BaseModel):
    """
    Описание структуры ответа получения списка операций.
    """
    operations: list[OperationSchema]


class GetOperationsSummaryQuerySchema(BaseModel):
    """
    Структура query параметров запроса для получения статистики по операциям счёта.
    """
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")


class GetOperationsSummaryResponseSchema(BaseModel):
    """
    Описание структуры ответа получения статистики по операциям.
    """
    summary: OperationsSummarySchema


class GetOperationReceiptResponseSchema(BaseModel):
    """
    Описание структуры ответа получения чека по операции.
    """
    receipt: OperationReceiptSchema


class MakeOperationRequestSchema(BaseModel):
    """
    Базовая структура тела запроса для создания финансовой операции.
    """
    status: OperationStatus
    amount: float
    card_Id: str = Field(alias="cardId")
    account_Id: str = Field(alias="accountId")


class MakeFeeOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура запроса для создания операции комиссии.
    """
    pass


class MakeFeeOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа на создание операции комиссии.
    """
    operation: OperationSchema


class MakeTopUpOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура запроса для создания операции пополнения.
    """
    pass


class MakeTopUpOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа на создание операции пополнения.
    """
    operation: OperationSchema


class MakeCashbackOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура запроса для создания операции кэшбэка.
    """
    pass


class MakeCashbackOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа на создание операции кэшбэка.
    """
    operation: OperationSchema


class MakeTransferOperationRequestDict(MakeOperationRequestSchema):
    """
    Структура запроса для создания операции перевода.
    """
    pass


class MakeTransferOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа на создание операции перевода.
    """
    operation: OperationSchema


class MakePurchaseOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура запроса для создания операции покупки.

    Дополнительное поле:
    - category: категория покупки.
    """
    category: str = Field(alias="category")


class MakePurchaseOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа на создание операции покупки.
    """
    operation: OperationSchema


class MakeBillPaymentOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура запроса для создания операции оплаты по счёту.
    """
    pass


class MakeBillPaymentOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа на создание операции оплаты по счёту.
    """
    operation: OperationSchema


class MakeCashWithdrawalOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура запроса для создания операции снятия наличных.
    """
    pass


class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа на создание операции снятия наличных.
    """
    operation: OperationSchema

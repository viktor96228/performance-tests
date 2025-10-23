from pydantic import BaseModel, HttpUrl, Field, ConfigDict

# Добавили описание структуры DocumentSchema
class DocumentSchema(BaseModel):
    """
    Описание структуры документа.
    """
    url: HttpUrl
    document: str

# Добавили тип GetTariffDocumentResponseSchema
class GetTariffDocumentResponseSchema(BaseModel):
    """
    Описание структуры ответа получения документа тарифа.
    """
    tariff: DocumentSchema

# Добавили тип GetContractDocumentResponseSchema
class GetContractDocumentResponseSchema(BaseModel):
    """
    Описание структуры ответа получения документа контракта.
    """
    contract: DocumentSchema

from clients.http.gateway.users.client import build_users_gateway_http_client
from clients.http.gateway.cards.client import build_cards_gateway_http_client
from clients.http.gateway.accounts.client import build_accounts_gateway_http_client
from clients.http.gateway.documents.client import build_documents_gateway_http_client
from httpx_get_documents import get_tariff_document_response, get_tariff_document_response_data, \
    get_contract_document_response_data
from httpx_get_documents import get_contract_document_response

users_gateway_client = build_users_gateway_http_client()
accounts_gateway_client = build_accounts_gateway_http_client()
documents_gateway_client = build_documents_gateway_http_client()

# Создаем пользователя
create_user_response = users_gateway_client.create_user()
print('Create user response:', create_user_response)

# Открываем кредитный счет
open_credit_card_account_response = accounts_gateway_client.open_credit_card_account(
    user_id=create_user_response['user']['id']
)
print('Open credit card account response:', open_credit_card_account_response)

# Получаем документ тарифа
get_tariff_document_response = get_tariff_document_response.json()

print('Get tariff document response:',get_tariff_document_response)

# Получаем документ контракта
get_contract_document_response = get_contract_document_response.json()

print('tariff_document:',get_contract_document_response)



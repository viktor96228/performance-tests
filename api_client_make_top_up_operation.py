from api_client_issue_physical_card import cards_gateway_client
from clients.http.gateway.users.client import build_users_gateway_http_client
from clients.http.gateway.accounts.client import build_accounts_gateway_http_client
from clients.http.gateway.operations.client import build_operations_gateway_http_client
from httpx_make_top_up_operation import make_top_up_operation_response

users_gateway_client = build_users_gateway_http_client()
accounts_gateway_client = build_accounts_gateway_http_client()
operations_gateway_client = build_operations_gateway_http_client()

# Создаем пользователя
create_user_response = users_gateway_client.create_user()
print('Create user response:', create_user_response)

# Открываем дебетовый счет
open_debit_card_account_response = accounts_gateway_client.open_debit_card_account(
    user_id=create_user_response['user']['id']
)
print('Open debit card account response:', open_debit_card_account_response)

# Создаём операцию пополнения
make_top_up_operation_request = make_top_up_operation_response.json()
print('OperationsGatewayHTTPClient.make_top_up_operations:', make_top_up_operation_request)

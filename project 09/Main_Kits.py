import sender_stand_request
import data
import requests
import configuration

# Получение token пользователя
def get_user_token():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=data.user_body,
                         headers=data.headers
                         )
response_token = get_user_token()
data.auth_token["Authorization"] = "Bearer " + response_token.json()["authToken"]

# Функция для изменения значения в параметре name в теле запроса
def get_kit_body(name):
    # Копируется словарь с телом запроса из файла data
    current_body = data.kit_body.copy()
    # Изменение значения в поле name
    current_body["name"] = name
    # Возвращается новый словарь с нужным значением name
    return current_body

# Функция для позитивной проверки
def positive_assert(name):
    # В переменную kit_body сохраняется обновленное тело запроса
    kit_body = get_kit_body(name)
    # В переменную kit_respons сохраняется результат запроса на создание набора:
    kit_respons = sender_stand_request.post_new_client_kit(kit_body, data.auth_token)
    # Проверяется, что код ответа равен 201
    assert kit_respons.status_code == 201
    # Проверяется, что в ответе есть поле name и оно не пустое
    assert kit_respons.json()["name"] == name

#Функция для негативной проверки
def negative_assert_code_400(kit_body):
    #kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit_body, data.auth_token)
    assert response.status_code == 400

# Тест 1. Успешное создание набора пользователя
# Параметр name состоит из 1 символа
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")

# Тест 2. Успешное создание набора пользователя
# Параметр name состоит из 551 символов
def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" +
            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" +
            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" +
            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcd" +
            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" +
            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" +
            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Тест 3. Набор пользователя не создан:
# Параметр name состоит из 0 символов
def test_create_kit_empty_name_get_error_response():
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body)

# Тест 4. Набор пользователя не создан:
# Параметр name состоит из 512 символов
def test_create_kit_512_letter_in_name_get_error_response():
    kit_body = get_kit_body("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" +
            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" +
            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" +
            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcd" +
            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" +
            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" +
            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert_code_400(kit_body)

# Тест 5. Успешное создание набора пользователя
# Параметр name состоит из английских букв
def test_create_kit_english_letter_in_name_get_success_response():
    positive_assert("QWErty")

# Тест 6. Успешное создание набора пользователя
# Параметр name состоит из русских букв
def test_create_kit_russian_letter_in_name_get_success_response():
    positive_assert("Мария")

# Тест 7. Успешное создание набора пользователя
# Параметр name состоит из спецсимволов
def test_create_kit_has_special_symbol_in_name_get_success_response():
    positive_assert("\"№%@\",")

# Тест 8. Успешное создание набора пользователя
# Параметр name с пробелами внутри
def test_create_kit_has_space_in_name_get_success_response():
    positive_assert("Человек и Ко")

# Тест 9. Успешное создание набора пользователя
# Параметр name состоит цифр
def test_create_kit_has_number_in_name_get_success_response():
    positive_assert("123")

# Тест 10. Набор пользователя не создан:
# Передан пустой JSON
def test_create_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_code_400(kit_body)

# Тест 11. Набор пользователя не создан:
# Передан другой тип параметра (число):
def test_create_kit_number_type_name_get_error_response():
    kit_body = get_kit_body(123)
    negative_assert_code_400(kit_body)
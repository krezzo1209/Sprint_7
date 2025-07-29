import random
import string

def generate_random_string(length=8):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def generate_courier():
    return {
        "login": f"courier_{generate_random_string(6)}",
        "password": generate_random_string(10),
        "firstName": f"courier_name_{generate_random_string(4)}"  # Замена имени на случайную строку
    }

def generate_invalid_courier(missing_field=None):
    courier = generate_courier()
    if missing_field:
        courier.pop(missing_field, None)
    return courier

def generate_duplicate_courier(base_courier):
    return {
        "login": base_courier["login"],
        "password": generate_random_string(10),
        "firstName": f"dup_name_{generate_random_string(4)}"
    }
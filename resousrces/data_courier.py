from resousrces.create_new_courier import generate_random_string

DATA = {
    "test_create_courier_without_login": {
        "password": "1234",
        "firstName": "saske"
    },

    "test_create_courier_without_password": {
        "login": "ninja",
        "firstName": "saske"
    },

    "create_courier_without_first_name": {
        "login": generate_random_string(10),
        "password": generate_random_string(10)
    },

    "create_courier_re_registration": {
        "login": "pavlova_32",
        "password": "1234",
        "firstName": "saske"
    },

    "test_login_courier": {
        "login": "pavlova_18",
        "password": "1234"
    },

    "test_login_courier_incorrect_pass": {
        "login": "pavlova_18",
        "password": "4321"
    },

    "test_login_courier_without_login": {
        "password": "4321"
    },

    "test_login_courier_without_password": {
        "password": "4321"
    },

    "test_login_courier_not_found": {
        "login": "ruiwrow",
        "password": "rwioeerk"
    },

    "test_create_courier_re_registration": {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "firstName": generate_random_string(10)
    }
}

Python function to validate the regular expression for the following

import code
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_bangladesh_mobile_number(number):
    pattern = r'^01[3-9]\d{8}$'
    return bool(re.match(pattern, number))

def validate_usa_telephone_number(number):
    pattern = r'^\(?([0-9]{3})\)?[-.●]?([0-9]{3})[-.●]?([0-9]{4})$'
    return bool(re.match(pattern, number))

def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}$'
    return bool(re.match(pattern, password))

# Testing the functions
email = "test@example.com"
mobile_number = "01712345678"
telephone_number ="(123)456-7890"
password = "Abc123@!Password"

print("Email Validation:", validate_email(email))
print("Bangladesh Mobile Number Validation:", validate_bangladesh_mobile_number(mobile_number))
print("USA Telephone Number Validation:", validate_usa_telephone_number(telephone_number))


Python Lambda function to create a fibonacci:
  from functools import reduce
fibonacci = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])

fib_series = fibonacci(50)
print(fib_series)
"""
This module contains utility functions for validating Brazilian document numbers.
This includes functions for validating CPF, CNPJ, CIC, RNE, and RG numbers.
This site helps to generate test values: https://www.4devs.com.br/
"""
import re
from .constants import AREA_CODES


def is_cic_valid(cic):
    """
    Validate a CIC number based on assumed check digit rules similar to CPF.

    Parameters
    ----------
    cic : str
        CIC number as a string, possibly including any non-numeric characters.

    Returns
    -------
    bool
        True if the CIC is valid, False otherwise.
    """
    cic = re.sub(r'[^0-9]', '', cic)

    if len(cic) != 11:
        return False

    # Calculate the first check digit (10th digit)
    first_weights = list(range(10, 1, -1))  # weights from 10 to 2
    first_check_sum = sum(int(digit) * weight for digit, weight in zip(cic[:9], first_weights))
    first_check_digit = 11 - (first_check_sum % 11)
    if first_check_digit >= 10:
        first_check_digit = 0

    # Calculate the second check digit (11th digit)
    second_weights = list(range(11, 1, -1))  # weights from 11 to 2
    second_check_sum = sum(int(digit) * weight for digit, weight in zip(cic[:10], second_weights))
    second_check_digit = 11 - (second_check_sum % 11)
    if second_check_digit >= 10:
        second_check_digit = 0

    # Check if the calculated digits match the provided digits
    return int(cic[9]) == first_check_digit and int(cic[10]) == second_check_digit


def is_cnpj_valid(cnpj):
    """
    Validates a CNPJ number.

    Parameters
    ----------
    cnpj : str
        CNPJ number as a string, possibly including dots, slashes, and hyphens.

    Returns
    -------
    bool
        True if the CNPJ is valid, False otherwise.
     """
    # Clean the CNPJ string by removing special characters
    cnpj = re.sub(r'[^0-9]', '', cnpj)

    # The CNPJ must be 14 digits long
    if len(cnpj) != 14:
        return False

    # Validate first check digit
    first_weights = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    sum_of_products = sum(int(digit) * weight for digit, weight in zip(cnpj[:12], first_weights))
    first_check_digit = 11 - (sum_of_products % 11)

    if first_check_digit >= 10:
        first_check_digit = 0
    if int(cnpj[12]) != first_check_digit:
        return False

    # Validate second check digit
    second_weights = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    sum_of_products = sum(int(digit) * weight for digit, weight in zip(cnpj[:13], second_weights))
    second_check_digit = 11 - (sum_of_products % 11)

    if second_check_digit >= 10:
        second_check_digit = 0
    if int(cnpj[13]) != second_check_digit:
        return False

    return True


def is_rne_valid(rne):
    """
    Validates a Brazilian RNE ID number.

    Parameters
    ----------
    rne : str
        RNE ID number as a string.

    Returns
    -------
    bool
        True if the RNE ID number is valid, False otherwise.
    """
    # Define the regex pattern for RNE numbers: Letter (typically V or W), 6-8 digits, and a check character
    pattern = r'^[VW]\d{6,8}-[A-Z]$'
    # Check if the RNE number matches the pattern
    return bool(re.fullmatch(pattern, rne))


def is_rg_valid(rg):
    """
    Validates a Brazilian RG number.

    Parameters
    ----------
    rg : str
        RG number as a string, possibly including dots, slashes, and hyphens.

    Returns
    -------
    bool
        True if the RG number is valid, False otherwise.
    """
    rg = re.sub(r'[^A-Z0-9]', '', rg.upper())
    digits = map(int, rg[:-1])
    totals = []
    for i, digit in enumerate(digits):
        totals.append(digit * (2 + i))

    total = sum(totals)
    remainder = total % 11
    verification_digit = 11 - remainder

    if verification_digit == 10:
        return rg[-1] == 'X'
    elif verification_digit == 11:
        verification_digit = 0

    return verification_digit == int(rg[-1])


def is_old_cnh_pgus_valid(cnh):
    """
    Validates an old Brazilian CNH number based on PGU-S checksum calculations.

    Parameters
    ----------
    cnh : str
        CNH number as a string.

    Returns
    -------
    bool
        True if the CNH is valid, False otherwise.
    """

    if len(cnh) != 9:
        return False

    weights = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    sum_digits = sum(int(c) * w for c, w in zip(cnh, weights))
    remainder = sum_digits % 11
    verify_one = 0 if remainder > 9 else 11 - remainder
    return str(verify_one) == cnh[-1]

    _


def is_cnh_valid(cnh):
    """
    Validates a Brazilian CNH number based on checksum calculations.

    Parameters
    ----------
        cnh: Is a str - CNH number as a string

    Returns
    -------
       bool: True if the CNH is valid, False otherwise

    resources: https://www.devmedia.com.br/forum/validacao-de-cnh/372972
    """
    cnh = re.sub(r'[^0-9]', '', cnh)

    if len(cnh) == 9:
        return is_old_cnh_pgus_valid(cnh)

    length = len(cnh)

    if length != 11:
        filler = '0' * (11 - length)
        cnh = cnh[0:length - 2] + filler + cnh[length - 2:]

    weights1 = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    sum_digits = 0
    for i in range(9):
        sum_digits += int(cnh[i]) * weights1[i]

    remainder = sum_digits % 11
    verify_one = 0 if remainder > 9 else 11 - remainder

    if cnh[9] != str(verify_one):
        return False

    weights2 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 2]
    sum_digits = 0
    for i in range(10):
        sum_digits += int(cnh[i]) * weights2[i]

    remainder = sum_digits % 11
    verify_two = 1 if remainder == 10 else 11 - remainder

    return str(verify_two) == cnh[10]


def validate_cnh(cnh):
    """
    Validate Brazilian CNH (Carteira Nacional de Habilitação) number.

    Args:
    cnh (str): A string representing the CNH number to validate.

    Returns:
    bool: True if the CNH is valid, False otherwise.
    """
    if not (cnh.isdigit() and len(cnh) == 11):
        return False

    # Getting the first 9 digits and reversing them for processing
    cnh_reversed = cnh[:9][::-1]
    first_digit, second_digit = int(cnh[9]), int(cnh[10])

    # Calculating the first check digit
    sum1 = sum((i + 2) * int(num) for i, num in enumerate(cnh_reversed))
    calculated_first_digit = sum1 % 11
    calculated_first_digit = 0 if calculated_first_digit == 10 else calculated_first_digit

    # Calculating the second check digit
    sum2 = sum((i + 2) * int(num) for i, num in enumerate(cnh[:10][::-1]))
    calculated_second_digit = sum2 % 11
    calculated_second_digit = 0 if calculated_second_digit == 10 else calculated_second_digit

    # Compare calculated digits with the provided last two digits
    return (calculated_first_digit == first_digit) and (calculated_second_digit == second_digit)


def is_phone_number_valid(phone_number):
    """
    Validate a Brazilian phone number.

    Parameters
    ----------
    phone_number : str
        Phone number as a string, possibly including parentheses, hyphens, and spaces.

    Returns
    -------
    bool
        True if the phone number is valid, False otherwise.
    """
    # Remove all non-numeric characters from the phone number
    phone_number = re.sub(r'\D', '', phone_number)

    # Check if the phone number has the correct length and starts with a valid area code
    return len(phone_number) == 11 and phone_number[2:4] in AREA_CODES


def is_license_plate_valid(license_plate):
    """
    Validates a Brazilian license plate number.

    Parameters
    ----------
    license_plate:  License plate number as a string.

    Returns
    -------
        Bool: True if the license plate is valid, False otherwise.
    """
    # Remove any non-alphanumeric characters and convert to uppercase
    license_plate = re.sub(r'[^A-Z0-9]', '', license_plate.upper())
    return re.match(r'^[A-Z]{3}\d{4}$|^[A-Z]{3}\d[A-Z]\d{2}$', license_plate) is not None


if __name__ == '__main__':
    cnh = """58316794534 2324146 2730470 3079329 3081207 3398603 3412165 3779387 4626843 4805301 4847786 4966090 5177094 5388225""".split()

    print('is_cnh_valid', is_cnh_valid('86157911791'))
    print('is_cnh_valid', is_cnh_valid('70273812743'))
    print('is_cnh_valid', is_cnh_valid('05626223124'))
    print('is_cnh_valid', is_cnh_valid('74545188472'))
    print('is_cnh_valid', is_cnh_valid('81452553802'))
    print('is_cnh_valid', is_cnh_valid('62816710724'))
    print('is_cnh_valid', is_cnh_valid('86291284022'))
    print('is_cnh_valid', is_cnh_valid('89513811062'))
    print('is_cnh_valid', is_cnh_valid('89513811062'))

    for c in cnh:
        print(is_cnh_valid(c))

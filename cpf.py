import re

def isCpfValid(cpf):
    """ If cpf in the Brazilian format is valid, it returns True, otherwise, it returns False. """

    # Check if type is str
    if not isinstance(cpf,str):
        return False

    # Remove some unwanted characters
    cpf = re.sub("[^0-9]",'',cpf)

    # Checks if string has 11 characters
    if len(cpf) != 11:
        return False

    sum = 0
    weight = 10

    """ Calculating the first cpf check digit. """
    for n in range(9):
        sum = sum + int(cpf[n]) * weight

        # Decrement weight
        weight = weight - 1

    verifyingDigit = 11 -  sum % 11

    if verifyingDigit > 9 :
        firstVerifyingDigit = 0
    else:
        firstVerifyingDigit = verifyingDigit

    """ Calculating the second check digit of cpf. """
    sum = 0
    weight = 11
    for n in range(10):
        sum = sum + int(cpf[n]) * weight

        # Decrement weight
        weight = weight - 1

    verifyingDigit = 11 -  sum % 11

    if verifyingDigit > 9 :
        secondVerifyingDigit = 0
    else:
        secondVerifyingDigit = verifyingDigit

    if cpf[-2:] == "%s%s" % (firstVerifyingDigit,secondVerifyingDigit):
        return True
    return False


def isCnpjValid(cnpj):
    """ If cnpf in the Brazilian format is valid, it returns True, otherwise, it returns False. """

    # Check if type is str
    if not isinstance(cnpj,str):
        return False

    # Remove some unwanted characters
    cpf = re.sub("[^0-9]",'',cnpj)

    # Checks if string has 11 characters
    if len(cpf) != 14:
        return False

    sum = 0
    weight = [5,4,3,2,9,8,7,6,5,4,3,2]

    """ Calculating the first cpf check digit. """
    for n in range(12):
        value =  int(cpf[n]) * weight[n]
        sum = sum + value


    verifyingDigit = sum % 11

    if verifyingDigit < 2 :
        firstVerifyingDigit = 0
    else:
        firstVerifyingDigit = 11 - verifyingDigit

    """ Calculating the second check digit of cpf. """
    sum = 0
    weight = [6,5,4,3,2,9,8,7,6,5,4,3,2]
    for n in range(13):
        sum = sum + int(cpf[n]) * weight[n]

    verifyingDigit = sum % 11

    if verifyingDigit < 2 :
        secondVerifyingDigit = 0
    else:
        secondVerifyingDigit = 11 - verifyingDigit

    if cpf[-2:] == "%s%s" % (firstVerifyingDigit,secondVerifyingDigit):
        return True
    return False



print(isCpfValid("806.945.357-53"))
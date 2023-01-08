import math
import sys

args = sys.argv

type_ = False
principal = False
periods = False
interest = False
payment = False

# Credits to todeus
for i in range(len(args)):
    if args[i].split("=")[0] == "--type":
        type_ = args[i].split("=")[1]
    elif args[i].split("=")[0] == "--principal":
        principal = int(args[i].split("=")[1])
    elif args[i].split("=")[0] == "--periods":
        periods = int(args[i].split("=")[1])
    elif args[i].split("=")[0] == "--interest":
        interest = float(args[i].split("=")[1])
    elif args[i].split("=")[0] == "--payment":
        payment = int(args[i].split("=")[1])


# functions
# calculate number of monthly payments
def number_mth(m_loan, m_mth_payment, m_interest):
    number = math.log(m_mth_payment / (m_mth_payment - m_interest / 12 / 100 * m_loan), 1 + m_interest / 12 / 100)
    number = math.ceil(number)
    year = number / 12
    if number < 12:
        print('It will take ' + str(number) + ' months to repay this loan!')
    elif number == 12:
        print('It will take 1 year to repay this loan!')
    elif number > 12:
        months = math.ceil(number % 12)
        year = math.floor(year)
        if months == 0:
            print('It will take ' + str(year) + ' years to repay this loan!')
        else:
            print('It will take ' + str(year) + ' years and ' + str(months) + ' months to repay this loan!')
    return number


# calculate the monthly payment
def month_payment(m_loan, m_period, m_interest):
    month_pay = m_loan * (m_interest / 12 / 100 * math.pow(1 + m_interest / 12 / 100, m_period)) / (
            math.pow(1 + m_interest / 12 / 100, m_period) - 1)
    print("Your monthly payment = " + str(math.ceil(month_pay)) + '!')
    return math.ceil(month_pay)


def loan_principle(m_annuity, m_period, m_interest):
    principle = m_annuity / ((m_interest / 12 / 100 * math.pow(1 + m_interest / 12 / 100, m_period)) / (
            math.pow(1 + m_interest / 12 / 100, m_period) - 1))
    print("Your loan principle = " + str(int(principle)) + '!')
    return int(principle)


def diff_payment(m_loan, m_period, m_interest):
    i = m_interest / 12 / 100
    sum = 0
    for j in range(1, m_period + 1):
        temp = math.ceil(m_loan / m_period + i * (m_loan - (m_loan * (j - 1) / m_period)))
        sum += temp
        print("Month " + str(j) + ": payment is " + str(temp))
    print("\nOverpayment = " + str(sum - m_loan))


def over_payment(m_loan, m_period, m_annuity):
    difference = int(m_annuity * m_period - m_loan)
    print("Overpayment = " + str(difference))


def print_incorrect():
    print("Incorrect parameters.")


# main
if type_ == "diff":
    if principal and periods and interest:
        diff_payment(principal, periods, interest)
    else:
        print_incorrect()
elif type_ == "annuity":
    if principal and periods and interest:
        over_payment(principal, periods, month_payment(principal, periods, interest))
    elif payment and periods and interest:
        over_payment(loan_principle(payment, periods, interest), periods, payment)
    elif principal and payment and interest:
        over_payment(principal, number_mth(principal, payment, interest), payment)
    else:
        print_incorrect()
else:
    print_incorrect()

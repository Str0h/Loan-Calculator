import math
import argparse


def calc_diff(principal_, periods_, interest_):
    i = interest_ / (12 * 100)
    total = 0
    for m in range(1, periods_ + 1):
        diff = math.ceil(principal_ / periods_ + i * (principal_ - (principal_ * (m - 1)) / periods_))
        total += diff
        print(f'Month {m}: payment is {diff}')
    print(f'\nOverpayment = {total - principal_}')


def calc_annuity(principal_, periods_, interest_):
    i = interest_ / (12 * 100)
    annuity_payment = math.ceil(principal_ * ((i * math.pow((1 + i), periods_)) / (math.pow((1 + i), periods_) - 1)))
    print(f'Your annuity payment = {annuity_payment}!')
    print(f'\nOverpayment = {annuity_payment * periods_ - principal_}')


def calc_principal(payment_, periods_, interest_):
    i = interest_ / (12 * 100)
    principal_ = math.floor(payment_ / ((i * math.pow((1 + i), periods_)) / (math.pow((1 + i), periods_) - 1)))
    print(f'Your loan principal = {principal_}!')
    print(f'\nOverpayment = {payment_ * periods_ - principal_}')


def calc_time(principal_, payment_, interest_):
    i = interest_ / (12 * 100)
    periods_ = math.ceil(math.log((payment_ / (payment_ - i * principal_)), (1 + i)))
    yrs, mnts = periods_ // 12, periods_ % 12
    if yrs == 0:
        print(f'It will take {mnts} months to repay this loan!')
    elif mnts == 0:
        print(f'It will take {yrs} years to repay this loan!')
    else:
        print(f'It will take {yrs} years and {mnts} months to repay this loan!')
    print(f'\nOverpayment = {payment_ * periods_ - principal_}')


parser = argparse.ArgumentParser()

parser.add_argument("--type")
parser.add_argument("--principal", default=False, type=int)
parser.add_argument("--payment", default=False, type=int)
parser.add_argument("--periods", default=False, type=int)
parser.add_argument("--interest", default=False, type=float)

args = parser.parse_args()

type_ = args.type
principal = args.principal
periods = args.periods
interest = args.interest
payment = args.payment

if type_ not in ['diff', 'annuity']:
    print("Incorrect parameters")
elif type_ == 'diff' and payment:
    print("Incorrect parameters")
elif not interest:
    print("Incorrect parameters")
elif principal < 0 or periods < 0 or interest < 0 or payment < 0:
    print("Incorrect parameters")
elif type_ == 'diff' and principal and periods and interest:
    calc_diff(principal, periods, interest)
elif type_ == 'annuity' and principal and periods and interest:
    calc_annuity(principal, periods, interest)
elif type_ == 'annuity' and payment and periods and interest:
    calc_principal(payment, periods, interest)
elif type_ == 'annuity' and principal and payment and interest:
    calc_time(principal, payment, interest)

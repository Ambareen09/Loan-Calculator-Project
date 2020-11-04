import math
import argparse
 
# Initialize the parser
parser = argparse.ArgumentParser(description="Credit Calculator Project")
 
# Add the parameters positional/optional
 
parser.add_argument('--type', help = "Type of Payment (Annuity or Differential")
parser.add_argument('--payment', help = "Monthly payment", type = int)
parser.add_argument('--principal', help = "Credit principal", type = int)
parser.add_argument('--periods', help = "Count of months", type = int)
parser.add_argument('--interest', help = "Credit interest (rate of interest)", type = float)
 
# Parse the arguments
args = parser.parse_args()
 
if args.type not in ['annuity', 'diff']:
    print('Incorrect Parameters')
    exit(0)
 
if args.type == 'diff' and args.payment != None:
    print('Incorrect Parameters')
    exit(0)
 
args_list = [args.type, args.payment, args.principal, args.periods, args.interest]
# print(args_list)
 
count = 0
for item in args_list:
    if item == None:
        count += 1
 
if count > 1:
    print('Incorrect Parameters')
    exit(0)
 
if args_list[1] != None and args_list[1] < 0 or args_list[2] != None and args_list[2] < 0 or args_list[3] != None and args_list[3] < 0 or args_list[4] != None and args_list[4] < 0.0:
    print('Incorrect Ha ha')
    exit(0)
 
 
if args.type == 'annuity' and args.payment != None and args.principal != None and args.interest != None:
 
    nominal_interest = args.interest / (12 * 100)
 
    months = math.ceil(math.log (args.payment
                                 / (args.payment - nominal_interest * args.principal), (1 + nominal_interest)))
 
    overpayment = months * args.payment - args.principal
 
    year = months // 12
    months = months % 12
 
    if months == 0:
        print('You need', year, 'years to repay this credit!')
    elif year == 0:
        print('You need', months, 'months to repay this credit!')
    else:
        print('You need', year, 'years and', months, 'months to repay this credit!')
    print('Overpayment = ', overpayment)
 
 
elif args.type == 'annuity' and args.periods != None and args.payment != None and args.interest != None:
 
    nominal_interest = args.interest / (12 * 100)
 
    complex_value = (nominal_interest * math.pow(1 + nominal_interest, args.periods)) / (math.pow(1 + nominal_interest, args.periods) - 1)
    credit_principal = int(args.payment / complex_value)
 
    overpayment = args.periods * args.payment - credit_principal
 
    print('Your credit principal =', str(credit_principal) + '!')
    print('Overpayment = ', overpayment)
 
elif args.type == 'annuity' and args.periods != None and args.principal != None and args.interest != None:
 
    nominal_interest = args.interest / (12 * 100)
 
    complex_value = (nominal_interest * math.pow(1 + nominal_interest, args.periods)) / (math.pow(1 + nominal_interest, args.periods) - 1)
 
    monthly_payment = math.ceil(args.principal * complex_value)
    overpayment = abs(args.periods * monthly_payment - args.principal)
 
    print(('Your annuity payment = {}!').format((monthly_payment)))
    print('Overpayment = ', overpayment)
 
elif args.type == 'diff' and args.periods != None and args.principal != None and args.interest != None:
    nominal_interest = args.interest / (12 * 100)
    diff_total_amount = 0
    for i in range(1, args.periods+1):
        diff_amount = math.ceil(args.principal/args.periods + nominal_interest * args.principal * (1 - (i -1) / args.periods))
        diff_total_amount += diff_amount
        print(('Month {}: paid out {}').format(i, diff_amount))
    overpayment = diff_total_amount - args.principal
    print('Overpayment = ', overpayment)

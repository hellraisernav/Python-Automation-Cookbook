# inputdata

data=[
    (1000,10),
    (2000,17),
    (2500,170),
    (2500,-170),
    ]

# print the header for reference

print('Revenue | Profit | Percent')

# this template aligns and displays the data in proper format

TEMPLATE = '{revenue:>7,} | {profit:>+6} | {percent:>7.2%}'

# print the data rows
for revenue,profit in data:
    row= TEMPLATE.format(revenue=revenue, profit=profit, percent=(profit/revenue))
    print(row)


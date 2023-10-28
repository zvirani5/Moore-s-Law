'''
CS1026a 2023
Assignment 01 Project 01 - Part C
Zanan Virani
zvirani5
09/30/2023
'''

'''
Moore's Law: The number of transistors in an integrated circuit (IC) doubles every two years.
This program outputs the computing power in FLOPS of the IC when the number of transistors doubles. 
'''
# Opening, as in the assignment
print("Project One (01) - Part C : The Moore the Merrier")

# Starting number of transistors. As said in the assignment, no input validation is required,
# so if negative value is entered, program will still run.
transistors = int(input("Starting Number of transistors: "))

# Starting year
year = int(input("Starting Year: "))

# Number of years
number_years = int(input("Total Number of Years: "))

# Starting flops is set as transistors * 50 to account for the very first line of the output.
flops = transistors * 50

# Initializing variable which will be used as the number for unit definition.
unit_value = 0

# Initializing the variable for the unit definitions.
prefix = ""

print("\nYEAR : TRANSISTORS : FLOPS:")

# Range explanation: Cycles every two years, convert to int to round down,
# Adding one at the end to include the last value.
for i in range(int(number_years / 2 + 1)):
    '''
    This next part section is a series of 'if' statements that serve two functions all in all:
    1) It will decide what the unit value is, making sure that the value stays between 1 (inclusive)
    and 1000 (exclusive). 
    2) It will decide what prefix to use based on the number of flops.
    '''

    if flops / 1000 < 1:
        prefix = ""
        unit_value = round(flops, 2)
    elif flops / 1000 < 1000:
        prefix = "kilo"
        unit_value = flops / 1000
    elif flops / 1000 < 1000000:
        prefix = "mega"
        unit_value = flops / 1000000
    elif flops / 1000 < 1000000000:
        prefix = "giga"
        unit_value = flops / 1000000000
    elif flops / 1000 < 1000000000000:
        prefix = "tera"
        unit_value = flops / 1000000000000
    elif flops / 1000 < 1000000000000000:
        prefix = "peta"
        unit_value = flops / 1000000000000000
    elif flops / 1000 < 1000000000000000000:
        prefix = "exa"
        unit_value = flops / 1000000000000000000
    elif flops / 1000 < 1000000000000000000000:
        prefix = "zetta"
        unit_value = flops / 1000000000000000000000
    elif flops / 1000 < 1000000000000000000000:
        prefix = "yotta"
        unit_value = flops / 1000000000000000000000

    # Printing all necessary information at the end of the if statements, but before the values update to
    # account for very first line.
    print(f"{year} {format(transistors, ',d')} %.2f {prefix}FLOPS {format(flops, ',d')}" % (unit_value))

    # Updates all the values to prepare for next iteration.
    year += 2
    transistors *= 2
    flops = transistors * 50

print("\nEND: Project One (01) - Part C\nZanan Virani zvirani5 251346220")
# Closing, like assignment



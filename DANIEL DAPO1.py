
#PLEASE NOTE:THIS CODE WAS REVIEWED BY COPILOT
# Define a constant for the tax year
    """
    Calculate tax based on 2009 federal tax brackets.

    Parameters:
    filing_status (int): The filing status of the taxpayer. 
                         Expected values are:
                         0 = Single
                         1 = Married Filing Jointly or Qualifying Widow(er)
                         2 = Married Filing Separately
                         3 = Head of Household
    income (float): The taxable income of the taxpayer. Must be a non-negative number.

    Returns:
    float: The calculated tax based on the provided filing status and income.
    """
    """
    Calculate tax based on 2009 federal tax brackets.
    """
    brackets = {
        0: [  # Single
            (8350, 0.10),
            (33950, 0.15),
            (82250, 0.25),
            (171550, 0.28),
            (372950, 0.33),
            (float("inf"), 0.35)
        ],
        1: [  # Married Filing Jointly / Widow(er)
            (16700, 0.10),
            (67900, 0.15),
            (137050, 0.25),
            (208850, 0.28),
            (372950, 0.33),
            (float("inf"), 0.35)
        ],
        2: [  # Married Filing Separately
            (8350, 0.10),
            (33950, 0.15),
            (68525, 0.25),
            (104425, 0.28),
            (186475, 0.33),
            (float("inf"), 0.35)
        ],
        3: [  # Head of Household
            (11950, 0.10),
            (45500, 0.15),
            (117450, 0.25),
            (190200, 0.28),
            (372950, 0.33),
            (float("inf"), 0.35)
    tax = 0
    previous_limit = 0
    
    # Assign brackets for the given filing status to a local variable
    filing_brackets = brackets[filing_status]
    
    # Calculate tax for each bracket
    for limit, rate in filing_brackets:
    
    # Calculate tax for each bracket
    for limit, rate in brackets[filing_status]:
        if income > limit:
            # Tax the full bracket
            tax += (limit - previous_limit) * rate
            previous_limit = limit
        else:
            # Tax the remaining income
            tax += (income - previous_limit) * rate
            break
    
    return tax


def main():
    """
    Main function to run the tax calculator program.
    """
    # Display program header
    print("=" * 60)
    print(f"US Federal Income Tax Calculator - {TAX_YEAR}")
    while True:
        try:
            filing_status = int(input(
                "\nEnter filing status:\n"
                "  0 = Single\n"
                "  1 = Married Filing Jointly or Qualifying Widow(er)\n"
                "  2 = Married Filing Separately\n"
                "  3 = Head of Household\n"
                "Your choice: "
            ))
            if filing_status in range(4):
                break
    # Get taxable income from user
    while True:
        try:
            taxable_income = float(input("\nEnter your taxable income: $"))
            if taxable_income < 0:
                print("Taxable income cannot be negative. Please enter a non-negative value.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        "  3 = Head of Household\n"
        "Your choice: "
    ))
    
    # Get taxable income from user
    taxable_income = float(input("\nEnter your taxable income: $"))
    
    # Calculate tax
    tax = calculate_income(filing_status, taxable_income)
    
    # Display results
    print("\n" + "=" * 60)
    print("RESULTS")
    print("=" * 60)
    print(f"Taxable Income: ${taxable_income:,.2f}")
    print(f"Total Tax Owed: ${tax:,.2f}")
    print("=" * 60)


# Run the program
if __name__ == "__main__":
    main()
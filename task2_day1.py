def main():

    standard_wall_space = 115
    gallons_required = 1
    hours_required = 8
    labor_per_hour = 20

    try:
        square_feet_entered = float(
            input('Enter the Square Feet of the Wall Space to be Painted: '))
        price_paint_gallon = float(
            input('Enter the Price of the Paint Per Gallon: '))
    except ValueError:
        print('Values Enter Must Be Figures!')
        main()
    else:
        gallons_required = square_feet_entered/standard_wall_space
        total_hours_required = square_feet_entered / hours_required
        cost_of_paint = gallons_required * price_paint_gallon
        total_labor_charges = total_hours_required * labor_per_hour
        total_job_cost = cost_of_paint + total_labor_charges

        print(f'The Number of Gallons Required:\n{gallons_required:,.1f} gal.')
        print(
            f'The Hours of Labor Required:\n{int(total_hours_required)} Hours')
        print(f'The Cost of the Paint:\n${cost_of_paint:.2f}')
        print(f'The Labor Charges:\n${total_labor_charges:,.2f}')
        print(f'The Total Cost of the Paint Job:\n${total_job_cost:,.2f}')


main()

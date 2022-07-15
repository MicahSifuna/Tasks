def main():
    member_name = input('Enter Name of Fitness Club Member: ')
    try:
        fat_grams = int(
            input("Enter Number of Fat Grams Consumed (in grams): "))
        carb_grams = int(
            input("Enter Number of Carbohydrates Consumed (in grams): "))
    except ValueError:
        print('ERROR: Value Should Be a Whole Number')
        main()
    else:
        fat_calories = fat_grams * 9
        carbs_calories = carb_grams * 4

    print(f"\nDear {member_name}, \nYour Calories from Fat are {fat_calories:,} cal. \nYour Calories from Carbohydrates are {carbs_calories:,} cal.")


main()

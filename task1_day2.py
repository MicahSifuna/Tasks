import time


class BookClub():

    def __init__(self, name='customer', books_owned=0, point_total=0):
        self.customer_name = name
        self.books_owned = books_owned
        self.points_earned = point_total

    def purchased_books(self):
        try:
            books_purchased = int(input(
                f'Hello {self.customer_name}, Enter the Number of Books Bought This Month: '))
        except ValueError:
            print('ERROR: Enter Only a Number, like 1, 3, or 7.')
            self.purchase_books()
        else:
            self.books_owned += books_purchased

        if self.books_owned == 0:
            self.points_earned += 0
        elif self.books_owned == 1:
            self.points_earned += 6
        elif self.books_owned == 2:
            self.points_earned += 16
        elif self.books_owned == 3:
            self.points_earned += 32
        elif self.books_owned >= 4:
            self.points_earned += 60

        print(f'Books Purchased: {self.books_owned}')
        print(f'Points Earned: {self.points_earned}')


andrew = BookClub('Andrew')

andrew.purchased_books()

import random


class Card:
    def __init__(self):
        self.rows = []
        self.generate_card()

    # Генерация карточки
    def generate_card(self):
        numbers = random.sample(range(1, 91), 15)
        numbers.sort()

        for i in range(0, 15, 5):
            row = numbers[i:i + 5]
            empty_cells = random.sample(range(0, 9), 4)
            row_str = ''
            for j in range(9):
                if j in empty_cells:
                    row_str += '   '
                else:
                    if row:
                        row_str += str(row.pop(0)).rjust(2) + ' '
            self.rows.append(row_str)

    # Вычеркивание чисел из карточки
    def mark_number(self, number):
        for i in range(3):
            if str(number).rjust(2) in self.rows[i]:
                self.rows[i] = self.rows[i].replace(str(number).rjust(2), '-')
                return True
        return False

    # Проверяет все ли числа вычеркнуты из карточки
    def has_won(self):
        for row in self.rows:
            if ' ' in row:
                return False
        return True

    def __str__(self):
        card_string = '-' * 26 + '\n'
        card_string += '\n'.join(row for row in self.rows)
        card_string += '\n' + '-' * 26
        return card_string

    def __repr__(self):
        return f'Card(rows={self.rows})'

    def __eq__(self, other):
        return self.rows == other.rows

    def __ne__(self, other):
        return not self == other


class Player:
    def __init__(self, name):
        self.name = name
        self.card = Card()

    #Определение наличия числа в карточки пользователем
    def mark_or_continue(self, number):
        print(f"Ваша карточка, {self.name}:\n{self.card}")
        choice = input(f"Число {number} есть на вашей карточке, зачеркнуть? (Y/N) ").lower()
        if choice == 'y':
            return self.card.mark_number(number)
        elif choice == 'n':
            return True
        else:
            print("Пожалуйста, введите 'Y' или 'N'.")
            return self.mark_or_continue(number)

    def has_won(self):
        return self.card.has_won()

    def __eq__(self, other):
        return self.name == other.name and self.card == other.card

    def __ne__(self, other):
        return not self == other


class LottoGame:
    def __init__(self):
        self.player = Player(input("Введите ваше имя: "))
        self.computer = Player("Computer")
        self.remaining_numbers = list(range(1, 91))

    #Выбор случайного числа из "мешка"
    def draw_number(self):
        return self.remaining_numbers.pop(random.randint(0, len(self.remaining_numbers) - 1))

    def play(self):
        print("Игра Лото!")
        print(f"Вы ({self.player.name}) играете против компьютера.")

        while True:
            drawn_number = self.draw_number()
            print(f"Выпал бочонок с номером: {drawn_number}")

            player_marked = self.player.mark_or_continue(drawn_number)
            if not player_marked:
                print("Вы проиграли!")
                break

            print("Карточка компьютера:")
            print(self.computer.card)

            computer_marked = self.computer.card.mark_number(drawn_number)
            print("Компьютер зачеркивает число." if computer_marked else "Компьютер продолжает игру.")

            if self.player.has_won():
                print(f"Поздравляем! {self.player.name} выиграл!")
                break
            elif self.computer.has_won():
                print("Компьютер выиграл!")
                break

    def __eq__(self, other):
        return self.player == other.player and self.computer == other.computer and self.remaining_numbers == other.remaining_numbers

    def __ne__(self, other):
        return not self == other


if __name__ == "__main__":
    game = LottoGame()
    game.play()

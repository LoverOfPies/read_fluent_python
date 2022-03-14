import collections

# отметим использование collections.namedtuple для конструирования простого класса
Card = collections.namedtuple('Card', ['rank', 'suit'])
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    # Получение карты из колоды, например первой или последней, не должно
    # быть сложнее обращения deck[0] или deck[-1], и именно это обеспечивает метод
    def __getitem__(self, position):
        return self._cards[position]


# Функция ранжирует карты, следуя
# этому правилу: 0 означает двойку треф, а 21 – туза пик
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


beer_card = Card('7', 'diamonds')
print(beer_card)

deck = FrenchDeck()
print(len(deck))
print(deck[12])

# Поскольку метод __getitem__ делегирует выполнение оператору [] объекта
# self._cards, колода автоматически поддерживает срезы
print(deck[:12])

# Расположить колоду в порядке возрастания
for card in sorted(deck, key=spades_high):
    print(card)

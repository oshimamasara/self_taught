
from random import shuffle


class Card:
    suits = ["♠",
             "❤",
             "♦",
             "♣"]

    values = [None, None,"2", "3",
              "4", "5", "6", "7",
              "8", "9", "10",
              "ジャック(11)", "クイーン(12)",
              "キング(13)", "エース(1)"]

    def __init__(self, v, s):
        """マークも値も整数値"""
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.suits[self.suit] + " の " + self.values[self.value]
#        v = self.values[self.value] + \ " of " + \ self.suits[self.suit]
        return v


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards\
                    .append(Card(i,
                                 j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name


class Game:
    def __init__(self):
        name1 = input("プレーヤー 1 の名前を入力してください： ")
        name2 = input("プレーヤー 2 の名前を入力してください： ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = "このラウンドは、 {} が勝ちました！\n"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "プレーヤー：{} は {}、 プレーヤー：{} は drew {} を引きました。"
        d = d.format(p1n,
                     p1c,
                     p2n,
                     p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("ゲームスタート！")
        while len(cards) >= 2:
            m = "（キーボードの q で終了）\n " + \
                "何かキーボードを押して下さい："
            response = input(m)
            if response == 'q':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n,
                      p1c,
                      p2n,
                      p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1,
                         self.p2)
        print("勝者： {} ".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "引き分け"

game = Game()
game.play_game()

class Cats:
    def __init__(self, cat_1="Рыжик", cat_2="Tom"):
        self.cat_1 = cat_1
        self.cat_2 = cat_2
        pass

    def height(self, ch_1=0, ch_2=0):
        if ch_1 > ch_2:
            return print(f"{self.cat_1} выше чем {self.cat_2} на {ch_1 - ch_2}см")
        else:
            return print(f"{self.cat_2} выше чем {self.cat_1} на {ch_2 - ch_1}см")
        

Cats("Леопольд").height(34, 21)
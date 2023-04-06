import time

from quna_po.base.bs import Base


class Booklist(Base):
    def book_buy(self):
        return self.fxpath('//*[@id="list_listInfo"]/ul[2]/li[1]/div/div[7]/a[1]')
    def book_list(self):
        self.book_buy().click()
        time.sleep(2)
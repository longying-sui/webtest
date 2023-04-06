import time

from selenium.webdriver import ActionChains, Keys
from quna_po.common.function import date_n
from quna_po.base.bs import Base
class Bookticket(Base):
    def book_start(self):
        return self.fname("fromStation")
    def book_end(self):
        return self.fname("toStation")
    def move_click(self):
        action = ActionChains(self.driver)
        time.sleep(1)
        action.move_by_offset(5, 5)
        action.click()
        action.perform()
        time.sleep(1)
    def book_button(self):
        return self.fname("stsSearch")
    def book_date(self,n):
        self.fname("date").send_keys(Keys.CONTROL, "a")
        self.fname("date").send_keys(Keys.BACKSPACE)
        self.fname("date").send_keys(date_n(n))

    def book_ticket(self,start,end,n):
        self.book_start().clear()
        self.book_start().send_keys(start)
        self.move_click()

        self.book_end().clear()
        self.book_end().send_keys(end)
        self.move_click()

        self.book_date(n)
        self.move_click()

        self.book_button().click()
        time.sleep(2)
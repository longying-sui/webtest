import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from quna_po.common.function import read_excel
from quna_po.po.book_list_page import Booklist
from quna_po.po.book_order_page import Bookorder
from quna_po.po.book_ticket_page import Bookticket

data=read_excel("../data/data.xlsx")

class Test_Book():
    def setup(self):
        # s = Service("../chromedriver.exe")
        self.driver=webdriver.Chrome("../chromedriver.exe")
        url = "https://train.qunar.com/"
        self.driver.get(url)
        self.driver.maximize_window()

    @pytest.mark.parametrize(["start","end","n","name","id"],data)
    def test_01(self,start,end,n,name,id):
        ticket=Bookticket(self.driver)
        ticket.book_ticket(start,end,n)

        list_b=Booklist(self.driver)
        list_b.book_list()

        order=Bookorder(self.driver)
        order.book_list(name,id)

    def teardown(self):
        self.driver.quit()

if __name__ == '__main__':
    pytest.main(["-s","test_book.py"])


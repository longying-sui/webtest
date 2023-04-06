import time

from quna_po.base.bs import Base


class Bookorder(Base):
    def book_name(self):
        return self.fname("pName_0")
    def book_id(self):
        return self.fname("pCertNo_0")
    def book_list(self,name,id):
        self.book_name().send_keys(name)
        self.book_id().send_keys(id)
        time.sleep(2)
class Employee:
    raise_am=1.04
    def __init__(self,firstname,lastname,pay):
        self.firstname=firstname
        self.lastname=lastname
        self.pay=pay
    def fullname(self):
        return '{} {}'.format(self.firstname,self.lastname)
    def apply_raise(self):
        self.pay=int(self.pay+self.raise_am)

    @classmethod
    def set_raise_am(cls,amount):
        cls.raise_am=amount
    @classmethod
    def from_string(cls,emp_str):
        f,l,p=emp_str.split('-')
        return cls(f,l,p)
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
                                                          


employ=Employee('Shubham','Kumar',24000000)
import datetime
my_date= datetime.date(2019,1,17)
print(Employee.is_workday(my_date))

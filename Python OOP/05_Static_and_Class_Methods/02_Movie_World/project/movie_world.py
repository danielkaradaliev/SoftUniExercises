from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name: str):
        self.name = name
        self.customers = list()
        self.dvds = list()

    @classmethod
    def dvd_capacity(cls):
        return cls.DVD_CAPACITY

    @classmethod
    def customer_capacity(cls):
        return cls.CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def __get_customer_by_id(self, customer_id: int):
        for customer in self.customers:
            if customer.id == customer_id:
                return customer
        return None

    def __get_dvd_by_id(self, dvd_id: int):
        for dvd in self.dvds:
            if dvd.id == dvd_id:
                return dvd
        return None

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer_to_rent = self.__get_customer_by_id(customer_id)
        dvd_to_be_rented = self.__get_dvd_by_id(dvd_id)

        if dvd_id in [x.id for x in customer_to_rent.rented_dvds]:
            return f"{customer_to_rent.name} has already rented {dvd_to_be_rented.name}"
        for customer in [x for x in self.customers if x.id != customer_id]:
            if dvd_id in [x.id for x in customer.rented_dvds]:
                return "DVD is already rented"
        if customer_to_rent.age < dvd_to_be_rented.age_restriction:
            return f"{customer_to_rent.name} should be at least {dvd_to_be_rented.age_restriction} to rent this movie"

        dvd_to_be_rented.is_rented = True
        customer_to_rent.rented_dvds.append(dvd_to_be_rented)
        return f"{customer_to_rent.name} has successfully rented {dvd_to_be_rented.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        rented_customer = self.__get_customer_by_id(customer_id)
        rented_dvd = self.__get_dvd_by_id(dvd_id)
        if dvd_id not in [x.id for x in rented_customer.rented_dvds]:
            return f"{rented_customer.name} does not have that DVD"
        rented_dvd.is_rented = False
        rented_customer.rented_dvds.remove(rented_dvd)
        return f"{rented_customer.name} has successfully returned {rented_dvd.name}"

    def __repr__(self):
        linesep = "\n"
        result = linesep.join([str(x) for x in self.customers]) + linesep + linesep.join([str(x) for x in self.dvds])
        return result

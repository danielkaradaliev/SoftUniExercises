from project.customer import Customer
from project.trainer import Trainer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription


class Gym:
    def __init__(self):
        self.customers = list()
        self.trainers = list()
        self.equipment = list()
        self.plans = list()
        self.subscriptions = list()

    def __get_customer_by_id(self, customer_id: int):
        for customer in self.customers:
            if customer_id == customer.id:
                return customer

    def __get_trainer_by_id(self, trainer_id: int):
        for trainer in self.trainers:
            if trainer_id == trainer.id:
                return trainer

    def __get_equipment_by_id(self, equipment_id: int):
        for equipment in self.equipment:
            if equipment_id == equipment.id:
                return equipment

    def __get_plan_by_id(self, plan_id: int):
        for plan in self.plans:
            if plan_id == plan.id:
                return plan

    def __get_subscription_by_id(self, subscription_id: int):
        for subscription in self.subscriptions:
            if subscription_id == subscription.id:
                return subscription

    def add_customer(self, customer: Customer):
        if customer.id not in [x.id for x in self.customers]:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer.id not in [x.id for x in self.trainers]:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment.id not in [x.id for x in self.equipment]:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan.id not in [x.id for x in self.plans]:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription.id not in [x.id for x in self.subscriptions]:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        linesep = "\n"
        result = linesep.join((str(x) for x in (self.__get_subscription_by_id(subscription_id),
                                                self.__get_customer_by_id(subscription_id),
                                                self.__get_trainer_by_id(subscription_id),
                                                self.__get_equipment_by_id(subscription_id),
                                                self.__get_plan_by_id(subscription_id))))
        return result

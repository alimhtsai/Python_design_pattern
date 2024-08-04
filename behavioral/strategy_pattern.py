from abc import ABC, abstractmethod


class DiscountStrategy(ABC):

    @abstractmethod
    def apply_discount(self, total: float) -> float:
        pass


class NoDiscount(DiscountStrategy):
    def apply_discount(self, total: float) -> float:
        return total


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float):
        self.percentage = percentage

    def apply_discount(self, total: float) -> float:
        return total * (1 - self.percentage / 100)


class FixedAmountDiscount(DiscountStrategy):
    def __init__(self, fixed_amount: float):
        self.fixed_amount = fixed_amount

    def apply_discount(self, total: float) -> float:
        return max(0, total - self.fixed_amount)


class ShoppingCart:

    def __init__(self, discount_strategy):
        '''initialize the shopping cart with the given discount_strategy and an empty items dictionary'''
        self.discount_strategy = discount_strategy
        self.shopping_cart = {}

    def add_item(self, item: str, price: float):
        '''add the item with its price to the items dictionary'''
        if item not in self.shopping_cart:
            self.shopping_cart[item] = 0
        self.shopping_cart[item] += price

    def remove_item(self, item: str):
        '''remove the item from the items dictionary if it exists'''
        if item in self.shopping_cart:
            del self.shopping_cart[item]

    def get_total(self) -> float:
        '''calculate and return the total price of the items in the cart'''
        return sum(self.shopping_cart.values())

    def get_total_after_discount(self) -> float:
        '''calculate and return the total price of the items in the cart after applying the discount'''
        total = self.get_total()
        return self.discount_strategy.apply_discount(total)


if __name__ == "__main__":
    cart = ShoppingCart(PercentageDiscount(10))

    cart.add_item("Item 1", 10.0)
    cart.add_item("Item 2", 20.0)
    cart.add_item("Item 3", 30.0)

    print("Total before discount:", cart.get_total())

    print("Total after discount:", cart.get_total_after_discount())

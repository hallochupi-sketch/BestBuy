from typing import List, Tuple
import products


class Store:
    def __init__(self, products_list: List[products.Product]):
        self._products = list(products_list)

    def add_product(self, product: products.Product) -> None:
        self._products.append(product)

    def remove_product(self, product: products.Product) -> None:
        if product in self._products:
            self._products.remove(product)

    def get_total_quantity(self) -> int:
        return sum(p.quantity for p in self._products)

    def get_all_products(self) -> List[products.Product]:
        # assuming Product has is_active() that returns bool
        return [p for p in self._products if p.is_active()]

    def order(self, shopping_list: List[Tuple[products.Product, int]]) -> float:
        total_price = 0.0

        # First check that all quantities are available
        for product, quantity in shopping_list:
            if quantity > product.quantity:
                raise ValueError(
                    f"Not enough quantity for product {product.name}: "
                    f"requested {quantity}, available {product.quantity}"
                )

        # If all good, perform purchase
        for product, quantity in shopping_list:
            total_price += product.price * quantity
            product.buy(quantity)

        return total_price


def main():
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)
    active_products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(active_products[0], 1), (active_products[1], 2)]))


if __name__ == "__main__":
    main()

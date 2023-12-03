from typing import List

# Інтерфейс для пошукових операцій
class ISearchable:
    def search_by_price(self, min_price: float, max_price: float) -> List['Product']:
        pass

    def search_by_category(self, category: str) -> List['Product']:
        pass

    def search_by_rating(self, min_rating: int) -> List['Product']:
        pass

# Клас Товар
class Product:
    def __init__(self, name: str, price: float, description: str, category: str, rating: int):
        self.name = name
        self.price = price
        self.description = description
        self.category = category
        self.rating = rating

# Клас Користувач
class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.purchase_history = []

# Клас Замовлення
class Order:
    def __init__(self, products: List[Product], quantity: int, total_price: float, status: str):
        self.products = products
        self.quantity = quantity
        self.total_price = total_price
        self.status = status

# Клас Магазин
class Store(ISearchable):
    def __init__(self):
        self.products = []
        self.users = []
        self.orders = []

    def add_product(self, product: Product):
        self.products.append(product)

    def add_user(self, user: User):
        self.users.append(user)

    def display_products(self):
        for product in self.products:
            print(f"{product.name} - {product.price}$ - {product.category} - Rating: {product.rating}")

    # Реалізація пошукових операцій інтерфейсу ISearchable
    def search_by_price(self, min_price: float, max_price: float) -> List[Product]:
        return [p for p in self.products if min_price <= p.price <= max_price]

    def search_by_category(self, category: str) -> List[Product]:
        return [p for p in self.products if p.category.lower() == category.lower()]

    def search_by_rating(self, min_rating: int) -> List[Product]:
        return [p for p in self.products if p.rating >= min_rating]

if __name__ == "__main__":
    store = Store()

    # Додавання декількох продуктів у магазин
    store.add_product(Product("Laptop", 1200, "High-performance laptop", "Electronics", 5))
    store.add_product(Product("Smartphone", 800, "Latest smartphone model", "Electronics", 4))
    store.add_product(Product("Headphones", 150, "Noise-canceling headphones", "Electronics", 4))
    store.add_product(Product("Coffee Maker", 50, "Automatic coffee maker", "Appliances", 3))

    # Виведення інформації про продукти
    print("Available Products:")
    store.display_products()

    # Додавання користувача та замовлення
    user = User("john_doe", "password123")
    store.add_user(user)

    user_products = store.search_by_category("Electronics")
    order_total_price = sum(p.price for p in user_products)
    order = Order(user_products, len(user_products), order_total_price, "Pending")
    user.purchase_history.append(order)

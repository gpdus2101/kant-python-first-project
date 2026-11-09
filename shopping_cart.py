# shopping cart 클래스 선언
# 상품 목록 저장 기능
# 메서드
# - 장바구니 담기
# - 장바구니 빼기
# - 상품 목록 조회
class ShoppingCart:
    def __init__ (self):a
        self.bucket = []

    def add_item (self, item):
        self.bucket.append(item)

    def remove_item (self, item):
        self.bucket.remove(item)

    def show_items(self):
        return self.bucket

# 상품 클래스
# 속성
# - 제품명
# - 가격
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# 쇼핑 카드 생성
cart = ShoppingCart()

# 상품 3개 생성
item1 = Item("가방", 50_000)
item2 = Item("신발", 70_000)
item3 = Item("패딩", 100_000)


# 상품 1개 장바구니 담기
cart.add_item(item1)
# 상품 1개 장바구니 담기
cart.add_item(item2)
# 상품 1개 장바구니 담기
cart.add_item(item3)
# 상품 1개 장바구니 빼기
cart.remove_item(item2)
# 장바구니에 담긴 상품 목록 조회
for item in cart.show_items():
    print(item.name, item.price)
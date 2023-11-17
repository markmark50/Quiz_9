class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def 주문의_총_가격(self, 수량):
        return self.price * 수량

Coffee = Beverage("커피", 3000)
GreenTea = Beverage("녹차", 2500)
IceTea = Beverage("아이스티", 3000)

def main():
    while True:
        selected_beverage = input("음료를 선택하세요 (커피, 녹차, 아이스티): ")
        if selected_beverage == "커피":
            beverage_obj = Coffee
        elif selected_beverage == "녹차":
            beverage_obj = GreenTea
        elif selected_beverage == "아이스티":
            beverage_obj = IceTea
        else:
            print("올바른 음료를 다시 선택하세요.")
            continue
        try:
            수량 = int(input("수량을 입력하세요: "))
        except ValueError:
            print("올바른 수량을 다시 입력하세요.")
            continue

        주문의_총_가격 = beverage_obj.주문의_총_가격(수량)
        print(f"{selected_beverage} {수량}잔의 주문의 총 가격은 {주문의_총_가격}원 입니다.")
        break

if __name__ == "__main__":
    main()


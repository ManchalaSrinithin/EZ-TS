class Siva:
    def gold(warangal):
        print("Price 5L")
    def car(warangal):
        print("Price 3L")
class Baby1(Siva):
    def bank(warangal):
        print("deposited 2L")
class Baby2(Siva):
    def jewels(warangal):
        print("price 10L")
class gbaby(Baby1,Baby2):
    def silver(warangal):
        print("price 20L")
b3=gbaby()
b3.jewels()
b3.gold()
b3.car()
b3.silver()
b3.bank()
b3.gold()
b3.car()
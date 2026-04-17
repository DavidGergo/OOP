from src import dataManager
from pathlib import Path

order_path = Path(__file__).parent / "data" / "order.csv"
order_file = dataManager.DataBase(order_path).beolvas()

dressing_path = Path(__file__).parent / "data" / "dressing.csv"
dressing_file = dataManager.DataBase(dressing_path).beolvas()

review_path = Path(__file__).parent / "data" / "review.csv"
review_file = dataManager.DataBase(review_path).beolvas()

for ord in order_file:
    if (ord['rendeles_id'] == '1'):
        print(ord)
print("\n")
print("----")
print("\n")
for dres in dressing_file:
    print(dres)
print("\n")
for rev in review_file:
    print(rev)
print("\n")
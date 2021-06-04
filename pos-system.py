import pandas as pd

### 商品クラス
class Item:
    def __init__(self,item_code,item_name,price,quantity=0):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
        self.quantity=quantity
    
    def get_price(self):
        return self.price

### オーダークラス
class Order:
    def __init__(self,item_master):
        self.item_order_list=[]
        self.item_quantity_list=[]
        self.item_master=item_master

    def take_order(self):
        while True:
            item_code = ""
            input_text=input("商品コードを入力してください。終了する場合はendと入力してください：")
            if input_text == "end":
                break
            for row in self.item_master:
                if row.item_code == input_text:
                    item_code = input_text
            if not item_code:
                print('登録されている商品コードを入力してください')
                continue
            item_quantity=input("個数を入力してください:")
            self.add_item_order(item_code,item_quantity)

    
    def add_item_order(self,item_code,item_quantity):
        self.item_order_list.append(item_code)
        self.item_quantity_list.append(item_quantity)
        
    def view_item_list(self):
        for item in self.item_order_list:
            print("商品コード:{}".format(item))

    def view_order_list(self):
        total_price=0
        for row in self.item_master:
            for item_code,item_quantity in zip(self.item_order_list,self.item_quantity_list):
                if row.item_code == item_code:
                    price=row.price*int(item_quantity) 
                    print(f"商品名：{row.item_name}")
                    print(f"{item_quantity}個")
                    print(f"{price}円")
                    total_price+=price
        print(f"合計金額：{total_price}")
    
def add_item_master_from_csv(csv_path):
    # マスタ登録
    item_master=[]
    item_master_df = pd.read_csv(csv_path, dtype={"code":object})
    for row in item_master_df.itertuples():
        item_master.append(Item(row.code,row.name,row.price))
    return item_master
    
### メイン処理
def main():
    item_master = add_item_master_from_csv('./item_master.csv')
    # オーダー登録
    order=Order(item_master)
    order.take_order()
    
    # オーダー表示
    order.view_item_list()

    order.view_order_list()
    
if __name__ == "__main__":
    main()
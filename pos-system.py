import pandas as pd

### 商品クラス
class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
    
    def get_price(self):
        return self.price

### オーダークラス
class Order:
    def __init__(self,item_master):
        self.item_order_list=[]
        self.item_master=item_master
    
    def add_item_order(self,item_code):
        self.item_order_list.append(item_code)
        
    def view_item_list(self):
        for item in self.item_order_list:
            print("商品コード:{}".format(item))

    def view_order_list(self):
        for row in self.item_master:
            for item in self.item_order_list:
                if row.item_code == item:
                    print("商品名：{} 価格：{}円".format(row.item_name,row.price))
    
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
    order_input = input('ほしい商品の商品コードをいれてください：')
    order.add_item_order(order_input)
    
    # オーダー表示
    order.view_item_list()

    order.view_order_list()
    
if __name__ == "__main__":
    main()
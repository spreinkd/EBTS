import time

buyorder = 33687
sellorder = buyorder+1
symbol, quantity, profit='NVDA', 500, 1.02

order_manager.place_order(
    symbol=symbol, 
    quantity=quantity, 
    action="BUY", 
    # order_type="MKT",
    order_type="LMT",
    limit_price=round(client.get_current_price(symbol), 2), 
    order_id=buyorder, 
    tif="GTC", 
    outside_rth=True
)

while True:
    fill_price_buy = client.get_fill_price(buyorder)
    if fill_price_buy:
        fill_price_buy = fill_price_buy[1]
        order_manager.place_order(
            symbol=symbol, 
            quantity=quantity, 
            action="SELL", 
            order_type="LMT", 
            limit_price=round(fill_price_buy * profit, 2), 
            order_id=sellorder, 
            tif="GTC", 
            outside_rth=False
        )
        break
    time.sleep(1)

while True:
    fill_price_buy = client.get_fill_price(buyorder)
    fill_price_sell = client.get_fill_price(sellorder)
    if fill_price_buy and fill_price_sell:
        pl = (fill_price_sell[1] - fill_price_buy[1]) * 500
        print(f"P/L: ${pl:.2f}")
        break
    time.sleep(1)

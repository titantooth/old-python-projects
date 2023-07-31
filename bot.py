import websocket, pprint , json , talib , numpy
from binance.client import Client
from binance.enums import *

import config

SOCKET = "wss://stream.binance.com:9443/ws/btcusdt@kline_1m"

client = Client(api_key=config.API_KEY,api_secret=config.API_SECRET, testnet=True)

closes = []
RSI_period = 14
RSI_overbuy = 70
RSI_oversell = 30
trade_symbol = "BTCUSDT"
trade_qty = 0.001
in_position = False

def order(Side ,Qty, Symbol, order_type=ORDER_TYPE_MARKET):
    try:
        print('sending order to binance')
        order = client.create_order(
            symbol = Symbol,
            side = Side,
            type = order_type,
            quantity =Qty)
        print(order)
    except Exception as e:
        return False
    return True




def on_open(ws):
    print("connection opened")
def on_close(ws):
    print("connection closed")
def on_message(ws,message ):
    global closes
    message_json = json.loads(message)
    pprint.pprint(message_json)

    candle = message_json['k']
    is_candle_closed = candle['x']
    close = candle['c']

    if is_candle_closed:
        print("candle closed at {}".format(close))
        closes.append(float(close))
        print("closes")
        print(closes)

        if len(closes) > RSI_period:
            np_closes = numpy.array(closes)
            rsi = talib.RSI(np_closes,RSI_period)
            print("all rsis calculated so far are:")
            print(rsi)
            last_rsi = rsi[-1]
            print('the current rsi is {}'.format(last_rsi))

            if last_rsi > RSI_overbuy:
                if in_position:
                    print("overbought sell" )
                    #sell logic here
                    order_success = order(SIDE_SELL, trade_qty, trade_symbol)
                    if order_success:
                        in_position = False
                else:
                    print('overbought but we dont have any nothing to do here')

            if last_rsi < RSI_oversell:
                if in_position:
                    print('oversold but we have some already nothing to do here')
                else:
                    print("oversold buy")
                    #buy logic
                    order_success = order(SIDE_BUY, trade_qty, trade_symbol)
                    if order_success:
                        in_position = True

ws = websocket.WebSocketApp(SOCKET, on_open=on_open , on_close=on_close , on_message=on_message  )
ws.run_forever()

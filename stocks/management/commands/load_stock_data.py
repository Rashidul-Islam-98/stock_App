import json
from decimal import Decimal
from django.core.management.base import BaseCommand
from stocks.models import Stock

class Command(BaseCommand):
    help = 'Load stock data from JSON file into the database'

    def handle(self, *args, **kwargs):
        with open('stock_market_data.json', 'r') as file:
            data = json.load(file)
            for entry in data:
                date = entry['date']
                trade_code = entry['trade_code']
                high = Decimal(entry['high'].replace(',', ''))
                low = Decimal(entry['low'].replace(',', ''))
                open_price = Decimal(entry['open'].replace(',', ''))
                close = Decimal(entry['close'].replace(',', ''))
                volume = entry['volume']

                Stock.objects.create(
                    date=date,
                    trade_code=trade_code,
                    high=high,
                    low=low,
                    open=open_price,
                    close=close,
                    volume=volume
                )
        self.stdout.write(self.style.SUCCESS('Stock data loaded successfully'))

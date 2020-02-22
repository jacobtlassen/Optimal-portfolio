import numpy as np
from yahoofinancials import YahooFinancials

def convert_list_of_dict(xlist, return_numpy=True):
    if return_numpy:
        return {key: np.array([item[key] for item in xlist]) for key in xlist[0]}
    else:
        return {key: [item[key] for item in xlist] for key in xlist[0]}

class Instrument(YahooFinancials):
    def __init__(self, tickers, start_date='1900-01-01', end_date='2100-01-01', time_interval='daily'):
        super().__init__(tickers)
        hist_data = self.get_historical_price_data(start_date, end_date, time_interval)
        self.hist_data = convert_list_of_dict(hist_data)

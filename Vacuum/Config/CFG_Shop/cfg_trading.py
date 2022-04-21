class cfg_trading:

    def __init__(self, trading):
        self.trading = trading

    @property
    def coef_sell(self):
        return (30 + 2 * int(self.trading ** 1.15)) / 100 # 0.3 + 0.34 # 0.64

    @property
    def coef_buy(self):
        return (130 - 2 * int(self.trading ** 1.15)) / 100 # 1.3 - 0.34 = 0.96
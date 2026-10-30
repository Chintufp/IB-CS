class newspaper:
    def __init__(self, name:str, year:int, month:int, day_of_month:int, is_finnish:bool):
        self.name = name
        self.year = year
        self.month = month
        self.day_of_month = day_of_month
        self.is_finnish = is_finnish

    def get_name(self):
        return self.name

    def __str__(self):
        return f'{self.name} ({self.year}-{self.month}-{self.day_of_month})'


dailyBugle = newspaper('Daily Bugle', 2024, 6, 5, False)

print(dailyBugle)
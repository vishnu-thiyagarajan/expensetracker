from django.db import models
# Create your models here.


class Client(models.Model):
    name = models.CharField(primary_key=True, max_length=120, blank=False)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.name

    def details(self):
        return {'name': self.name,
                'active': self.active,
                # 'timestamp':self.timestamp
                }


class Expense(models.Model):
    choice = [("CAD", "CAD"),
              ("HKD", "HKD"),
              ("LVL", "LVL"),
              ("PHP", "PHP"),
              ("DKK", "DKK"),
              ("HUF", "HUF"),
              ("CZK", "CZK"),
              ("AUD", "AUD"),
              ("RON", "RON"),
              ("SEK", "SEK"),
              ("IDR", "IDR"),
              ("INR", "INR"),
              ("BRL", "BRL"),
              ("RUB", "RUB"),
              ("LTL", "LTL"),
              ("JPY", "JPY"),
              ("THB", "THB"),
              ("CHF", "CHF"),
              ("SGD", "SGD"),
              ("PLN", "PLN"),
              ("BGN", "BGN"),
              ("TRY", "TRY"),
              ("CNY", "CNY"),
              ("NOK", "NOK"),
              ("NZD", "NZD"),
              ("ZAR", "ZAR"),
              ("USD", "USD"),
              ("MXN", "MXN"),
              ("EEK", "EEK"),
              ("GBP", "GBP"),
              ("KRW", "KRW"),
              ("MYR", "MYR"),
              ("HRK", "HRK")]
    clientname = models.ForeignKey(Client)
    timestampOfExpense = models.DateTimeField(auto_now_add=True,
                                              auto_now=False)
    amount = models.IntegerField()
    currency = models.CharField(max_length=3, choices=choice)
    title = models.CharField(max_length=120, blank=False)
    description = models.TextField()

    def __str__(self):
        obj_str = str(self.clientname) + ' | ' + str(self.timestampOfExpense)
        return obj_str

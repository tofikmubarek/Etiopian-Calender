"""
Ethiopian Date Converter

Author: Abdulaziz Ali
Original Java code by Abdulaziz Ali, Python adaptation by GitHub Copilot

This file provides Ethiopian <-> Gregorian calendar conversion logic.

License: MIT (or specify your own)
"""

from datetime import date

class EthiopianDate:
    def __init__(self, year=None, month=None, day=None, local_date=None):
        if local_date is not None:
            # Conversion from Gregorian to Ethiopian will be handled by EthiopianDateConverter
            ethiopian_date = EthiopianDateConverter.to_ethiopian_date(local_date)
            self.year = ethiopian_date.year
            self.month = ethiopian_date.month
            self.day = ethiopian_date.day
            self.local_date = local_date
        elif year is not None and month is not None and day is not None:
            # Conversion from Ethiopian to Gregorian will be handled by EthiopianDateConverter
            self.local_date = EthiopianDateConverter.to_gregorian_date(year, month, day)
            self.year = year
            self.month = month
            self.day = day
        else:
            raise Exception("Invalid arguments for EthiopianDate initialization.")

    def from_gregorian_date(self, local_date):
        ethiopian_date = EthiopianDateConverter.to_ethiopian_date(local_date)
        self.year = ethiopian_date.year
        self.month = ethiopian_date.month
        self.day = ethiopian_date.day
        self.local_date = local_date

    def to_gregorian_date(self):
        return self.local_date

    # Properties for year, month, day, local_date
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        self._month = value

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        self._day = value

    @property
    def local_date(self):
        return self._local_date

    @local_date.setter
    def local_date(self, value):
        self._local_date = value

class EthiopianDateConverter:
    JdOffset = 1723856

    @staticmethod
    def to_ethiopian_date(local_date):
        jdn = EthiopianDateConverter._to_jdn(local_date)
        return EthiopianDateConverter._to_ethiopian_date(jdn)

    @staticmethod
    def to_gregorian_date(year, month, day):
        EthiopianDateConverter._validate(year, month, day)
        jdn = EthiopianDateConverter._from_ethiopian_date_to_jdn(year, month, day)
        return EthiopianDateConverter._to_gregorian_date(jdn)

    @staticmethod
    def _to_jdn(local_date):
        a = (14 - local_date.month) // 12
        y = local_date.year + 4800 - a
        m = local_date.month + 12 * a - 3
        return local_date.day + (153 * m + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045

    @staticmethod
    def _to_ethiopian_date(jdn):
        r = (jdn - EthiopianDateConverter.JdOffset) % 1461
        n = r % 365 + 365 * (r // 1460)
        year = 4 * ((jdn - EthiopianDateConverter.JdOffset) // 1461) + r // 365 - r // 1460
        month = n // 30 + 1
        day = n % 30 + 1
        return EthiopianDate(year, month, day)

    @staticmethod
    def _to_gregorian_date(jdn):
        from datetime import date
        r = jdn + 68569
        n = 4 * r // 146097
        r = r - (146097 * n + 3) // 4
        year = 4000 * (r + 1) // 1461001
        r = r - 1461 * year // 4 + 31
        month = 80 * r // 2447
        day = r - 2447 * month // 80
        r = month // 11
        month = month + 2 - 12 * r
        year = 100 * (n - 49) + year + r
        return date(year, month, day)

    @staticmethod
    def _validate(year, month, day):
        if (month < 1 or month > 13 or
            (month == 13 and year % 4 == 3 and day > 6) or
            (month == 13 and year % 4 != 3 and day > 5) or
            day < 1 or day > 30):
            raise Exception("Year, Month, and Day parameters describe an un-representable EthiopianDateTime.")

    @staticmethod
    def _from_ethiopian_date_to_jdn(year, month, day):
        return (EthiopianDateConverter.JdOffset + 365) + 365 * (year - 1) + year // 4 + 30 * month + day - 31

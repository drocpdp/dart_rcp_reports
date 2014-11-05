import datetime
from dateutil import tz
from dateutil.relativedelta import relativedelta
import os


class DateTimeOperations(object):
    
    TIME_ZONES_FILE = os.path.dirname(os.path.realpath(__file__)) + '/../config/timezones.txt'
    
    KOREAN_TZ = 'Asia/Seoul'
    
    def main(self):
        a = self.get_current_time_timezone(self.KOREAN_TZ)
        print a
        print self._decrement_by_months(a, 2)
        print self._increment_by_months(a, 2)
        
    def get_dart_specific_date_format_from_dt_object(self, datetime_object):
        """Used for DART API functionality - YYYYMMDD"""
        return datetime_object.strftime("%Y%m%d")
    
    def _increment_by_months(self, datetime, months):
        return datetime + relativedelta(months=months)
    
    def _decrement_by_months(self, datetime, months):
        return datetime - relativedelta(months=months)
    
    def get_current_time_timezone(self, timezone=KOREAN_TZ):
        return datetime.datetime.now(tz.gettz(timezone))
    
    def create_timestamp_timezone(self, timezone=KOREAN_TZ, year=0, month=0, day=0, hour=0, minute=0, second=0, microsecond=0):
        dt = datetime.datetime(year, month, day, hour, minute, second, microsecond, tzinfo=tz.gettz(timezone))
        return dt 
    
    def create_timestamp_korean_tz(self, year,month,day):
        dt = self.create_timestamp_timezone(timezone=self.KOREAN_TZ, year=year, month=month, day=day)
        return dt

    def is_timezone_valid(self, timezone):
        tz_file = open(self.TIME_ZONES_FILE, 'r')
        for tz in tz_file:
            tz = tz.strip().split(',')
            if timezone in tz:
                return True
        tz_file.close()
        return False
    
    def is_time_past(self, time1, time2):
        if time1 > time2:
            return True
        if time1 < time2:
            return False
        
if __name__=="__main__":
    DateTimeOperations().main()
    
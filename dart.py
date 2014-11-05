import ConfigParser
import json
import urllib2
from utils.date_time_operations import DateTimeOperations


class Dart(object):
    
    """
    http://dart.fss.or.kr/api/search.json?auth=%s&start_dt=20140101&end_dt=20140401&bsn_tp=E001&page_set=100
    """
        
    def main(self):
        print 'ok'
        config = ConfigParser.ConfigParser()
        config.read('/Users/davidreynon/Desktop/dart_finance/auth.properties')
        key = config.get('default', 'auth_key')        
        dt = DateTimeOperations()
        start_date_report = dt.create_timestamp_korean_tz(2001,1,1)
        print 'start_date_report=%s' % (dt.get_dart_specific_date_format_from_dt_object(start_date_report))
        end_dt_increment = dt._increment_by_months(start_date_report, 2)
        print 'end_dt_increment=%s' % (dt.get_dart_specific_date_format_from_dt_object(end_dt_increment))
        while dt.is_time_past(dt.get_current_time_timezone(), end_dt_increment):
            print '-------'
            start_date_report = end_dt_increment
            #print 'start_date_report=%s' % (dt.get_dart_specific_date_format_from_dt_object(start_date_report))
            end_dt_increment = dt._increment_by_months(start_date_report, 2)
            #print 'end_dt_increment=%s' % (dt.get_dart_specific_date_format_from_dt_object(end_dt_increment))
            dart_start_date_report = dt.get_dart_specific_date_format_from_dt_object(start_date_report)
            dart_end_dt_increment = dt.get_dart_specific_date_format_from_dt_object(end_dt_increment)
            url_base = 'http://dart.fss.or.kr/api/search.json?auth=%s&start_dt=%s&end_dt=%s&bsn_tp=E001&page_set=100'
            full_url = url_base % (key, dart_start_date_report, dart_end_dt_increment)
            print full_url
            resp = urllib2.urlopen(full_url)
            json_res = json.load(resp)
            #print json_res
            entries = json_res['list']
            for entry in entries:
                recp_no = entry['rcp_no']                
                print 'rcp_no = %s' % recp_no

                
            

if __name__=="__main__":
    Dart().main()
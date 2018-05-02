import csv
import gzip

def open_csv(name, delimiter=','):
    return csv.writer(gzip.open('{}'.format(name), 'wt'), doublequote=True, quoting=csv.QUOTE_ALL, delimiter=delimiter, escapechar='\\')


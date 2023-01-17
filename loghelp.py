
from datetime import datetime
from os import mkdir

########################################################################

class Logger:

## ------------------------------------------------------------------ ##
    def createLogsFile(self):

        if
        try:
            print('Attempting to create log file')
            self.log_file = open('\\LOGS\\Log_%s.txt' %
                             self.timestamp_log_created_at, 'w')
        except:
            print('Couldnot create log file.')

## ------------------------------------------------------------------ ##
    def replaceSpacesWithUnderscore(self, string):

        print('replaceSpacesWithUnderscore')
        list_string = list(string)

        for char in list_string:
            if char == ' ' or char == '-' or char == ':' or char == '.':
                space_at = list_string.index(char)
                list_string[space_at] = '_'

        new_string = ''

        for char in list_string:
            new_string = new_string + char

        return new_string

## ------------------------------------------------------------------ ##
    def createTimestamp(self):

        print('createTimestamp')
        timestamp = datetime.now()
        timestamp = self.replaceSpacesWithUnderscore(str(timestamp))

        return timestamp

## ------------------------------------------------------------------ ##
    def createStatement(self, level, statement):

        print('createStatement')
        log = str(self.createTimestamp()) + ' ' + level + ' ' + statement

        return log

## ------------------------------------------------------------------ ##
    def printToLog(self, level, statememt):

        print('printToLog')
        log_to_print = self.createStatement(level, statememt)
        self.log_file.write(log_to_print)

## ------------------------------------------------------------------ ##
    def prepare(self):

        print('prepare')
        self.createLogsFile()

## ------------------------------------------------------------------ ##
    def __init__(self):

        print('__init__')

        self.log_file = None
        self.timestamp_log_created_at = self.createTimestamp()
        print('Log file created at:self.timestamp_log_created_at:' +
              self.timestamp_log_created_at)

        pass


########################################################################

# example
logger_obj = Logger()
logger_obj.prepare()
level = 'TEST'
statement = 'Test statement'
logger_obj.printToLog(level, statement)

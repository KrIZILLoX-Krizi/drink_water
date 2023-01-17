
import time
from getpass import getuser

##################################################################

class Drink_Water:

## ------------------------------------------------------------ ##

    def openLog(self, m_date):

        log_file = 'logs_' + m_date + '.log'
        log_path = 'logs/'
        try:
            log_file = open(log_path + log_file, 'a+')
            return log_file
        except:
            print('Logfile couldnot be opened')

        return self.LOG_FILE_OPEN_ERROR

## ------------------------------------------------------------ ##

    def createDateTime(self):

        time_struct = time.localtime()

        m_day = time_struct.tm_mday
        m_mon = time_struct.tm_mon
        m_year = time_struct.tm_year
        m_hour = time_struct.tm_hour
        m_mins = time_struct.tm_min
        m_secs = time_struct.tm_sec

        if (m_day / 10) <= 1:
            m_day = '0' + str(m_day)
            # print('day: ' + m_day)
        if (m_mon / 10) <= 1:
            m_mon = '0' + str(m_mon)
        if m_year / 10 <= 1:
            m_year = '0' + str(m_year)
        if m_hour / 10 <= 1:
            m_hour = '0' + str(m_hour)
        if m_mins / 10 <= 1:
            m_mins = '0' + str(m_mins)
        if m_secs / 10 <= 1:
            m_secs = '0' + str(m_secs)

        m_date = str(m_day) + '_' + str(m_mon) + '_' + str(m_year)
        print('Date: ' + m_date)

        m_time = str(m_hour) + '_' + str(m_mins) + '_' + str(m_secs)
        print('Time: ' + m_time)

        return m_date, m_time

## ------------------------------------------------------------ ##

    def askUser(self):

        print('Hey ' + getuser() + '!\n' +
              'Drink some water please.\nTime: ' + self.m_time)
        return input('Drank yet? (y/n)\n' or 'n')

## ------------------------------------------------------------ ##

    def writeLog(self, log_file, drank_water):

        line = self.m_time + ': \t\t ' + drank_water + '\n'
        log_file.write(line)

        return

## ------------------------------------------------------------ ##

    def printSummary(self, log_file):

        # reset seek on file
        # ------------------
        log_file.seek(0)

        count_yes = 0
        count_no = 0
        timestamps = []

        # loop over the logs
        # ------------------
        for line in log_file:
            line = line.rstrip('\n')
            # add timestamp to list
            # ---------------------
            timestamps.append(line[0:8])
            # if yes increment count
            # ----------------------
            # print('-' + line[-1] + '-')
            if line[-1] == 'y':
                count_yes += 1
            # if no increment count
            # ---------------------
            elif line[-1] == 'n':
                count_no += 1

        print('No. of Entries: ' + str(len(timestamps)))
        print('Reminders at:')
        print(timestamps)
        print('Times hydrated: ' + str(count_yes))
        print('Times skipped: ' + str(count_no))

        return

## ------------------------------------------------------------ ##

    def __init__(self):

        # ERROR CODES
        # -----------
        self.LOG_FILE_OPEN_ERROR = 404

        # creating time and date
        # ----------------------
        m_date, self.m_time = self.createDateTime()

        # open logs
        # ---------
        self.log_file = self.openLog(m_date)

        # prompt user
        # -----------
        drank_water = self.askUser()

        # write to logs
        # -------------
        self.writeLog(self.log_file, drank_water)

        # print summary
        # -------------
        self.printSummary(self.log_file)

        # close log file
        # --------------
        self.log_file.close()

        pass

##################################################################

# example
obj = Drink_Water()

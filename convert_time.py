
#Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
class solution:
    def convert_time(time):
        if time[8:10] == 'PM' and time[:2] == '12':
            return time[:8]
        elif time[8:10] == 'PM' and time[:2] != '12':
            return str(int(time[:2]) + 12) + time[2:8]
        elif time[8:10] == 'AM' and time[:2] == '12':
            return '00' + time[2:8]
        else:
            return time[:8]

print(solution.convert_time('12:44:50AM'))
print(solution.convert_time('12:44:50PM'))
print(solution.convert_time('05:40:00AM'))
print(solution.convert_time('05:40:00PM'))

class Employee:
    start_time="10 am "
    end_time = "5 pm "

class Techer(Employee):
    def __init__(self, subject):
        self.subject = subject

t1 = Techer('math')
print(t1.subject,t1.start_time, t1.end_time)
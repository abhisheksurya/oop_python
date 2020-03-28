"""This class is a logical conception of Employee"""


class Employee:

    """
    Description -
    Constructor to initialize employee attributes
    Parameters -
    first_name: string, required
    last_name: string, required
    Returns -
    NA
    """

    def __init__(self, first_name, last_name):
        self.employee_first_name = first_name
        self.employee_last_name = last_name
        self.employee_email = first_name + "." + last_name + "@abhisheksurya.dev"

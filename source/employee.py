"""This class is a logical conception of Employee"""


class Employee:

    """Constructor to initialize employee attributes
    
    :param first_name: string, required last_name: string, required
    :param [ParamName]: [ParamDescription], defaults to [DefaultParamVal]
    :type [ParamName]: [ParamType](, optional)
    :raises [ErrorType]: [ErrorDescription]
    :return: [ReturnDescription]
    :rtype: [ReturnType]
    """

    def __init__(self, first_name, last_name):
        self.employee_first_name = first_name
        self.employee_last_name = last_name
        self.employee_email = first_name + "." + last_name + "@abhisheksurya.dev"

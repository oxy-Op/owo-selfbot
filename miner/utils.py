from datetime import datetime


class OxeratorException(Exception):
    def __init__(self, error, error_des, extra=""):
        super(OxeratorException, self).__init__(error, error_des, extra)
        self.error = error
        self.error_des = error_des
        self.extra = extra

    def __str__(self) -> str:
        return "[{}] -> {} | {}".format(self.error, self.error_des, self.extra)


def exit_():
    input("Press any key to exit... ")


def log(info=None, warning=None, error=None):
    file = open('./logs.log', 'a')
    try:
        if info:
            file.write("[{}]:INFO => {} \n".format(
                datetime.now().strftime("%m-%d-%Y %I:%M:%S %p"), info))
        if warning:
            file.write("[{}]:WARNING => {} \n".format(
                datetime.now().strftime("%m-%d-%Y %I:%M:%S %p"), warning))
        if error:
            file.write("[{}]:ERROR => {} \n".format(
                datetime.now().strftime("%m-%d-%Y %I:%M:%S %p"), error))
    except Exception as e:
        raise e
    finally:
        file.close()

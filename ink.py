import os


class Ink:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    @staticmethod
    def warning(x):
        return (Ink.WARNING + x + Ink.ENDC)

    @staticmethod
    def header(x):
        return (Ink.HEADER + x + Ink.ENDC)

    @staticmethod
    def ok(x):
        return (Ink.OKBLUE + x + Ink.ENDC)

    @staticmethod
    def good(x):
        return (Ink.OKGREEN + x + Ink.ENDC)

    @staticmethod
    def fail(x):
        return (Ink.FAIL + x + Ink.ENDC)

    @staticmethod
    def bold(x):
        return (Ink.BOLD + x + Ink.ENDC)


    @staticmethod
    def underline(x):
        return (Ink.UNDERLINE + x + Ink.ENDC)

    def info(x):
        return (x + "\n")


if __name__ == '__main__':
    print(Ink.good("Hello\tGood"))
    print(Ink.ok("Hello\tOk"))
    print(Ink.header("Hello\tHeader"))
    print(Ink.warning("Hello\tWarning"))
    print(Ink.fail("Hello\tFail"))
    print(Ink.bold("Hello\tBold"))
    print(Ink.underline("Hello\tUnderline"))
    print(Ink.info("Hello\tPlain"))


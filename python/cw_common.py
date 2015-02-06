# coding=utf-8
"""
Common code.
"""
import os
import sys
from datetime import datetime


def parse_args(args):
    """
    Parses command line arguments into switches, parameters and commands.
    Switches look like "-switch"
    Parameters look like "param=value"
    Commands look like "command" (no initial "-")

    :param args: List of strings straight from the console.
    :return switches: list of strings which are switches, leading "-" trimmed
    :return parameters: dictionary of parameters
    :return commands: list of strings which are commands
    """

    # Switches look like "-switch"
    switches = [
        arg
        for arg in args
        if arg[0] == "-"
    ]

    # Parameters look like "parameter=value"
    parameters = dict([
        (
            arg.split("=")[0],
            arg.split("=")[1]
        )
        for arg in args
        if arg[0] != "-" and "=" in arg
    ])

    # commands look like "command"
    commands = [
        arg
        for arg in args
        if arg[0] != "-" and "=" not in arg
    ]

    return switches, parameters, commands


def get_parameter(parameters, param_name, required=False, usage_text=None):
    """
    Gets parameters from a parameter list
    :param parameters:
    :param param_name:
    :param required:
    :param usage_text:
    :return: :raise ValueError:
    """
    if param_name in parameters:
        param = parameters[param_name]
    elif required:
        if usage_text is not None:
            print(usage_text)
        raise ValueError("Require {0} parameter.".format(param_name))
    else:
        return ""
    return param


def get_log_filename(filepath):
    """
    Generates a log file path from a given file path.
    :param filepath:
    :return:
    """
    (log_dirname, log_filename) = os.path.split(filepath)
    log_filename = "{date}-{filename}.log".format(date=datetime.now().strftime("%Y-%m-%d"), filename=log_filename)
    log_filename = os.path.join(log_dirname, log_filename)
    return log_filename


def prints(*args, sep=' ', end='\n', file=None):
    """
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.

    Attaches a local timestamp to the start of the output.

    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
    """
    timestamp = "[{0}]".format(datetime.now())
    print(timestamp, *args, sep=sep, end=end, file=file)


class ApplicationError(Exception):
    """
    Represents an error in which the executing code is in a logically invalid
    state. This means that a programmer error has occurred.
    :param value:
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class InvalidOperationError(Exception):
    """
    Represents an error in which the operation is invalid given the state of things.
    :param value:
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class RedirectStdoutTo:

    """
    For redirecting stdout to a file.
    Copied from Dive Into Python.

    Use like:

    with open('log.txt', mode="w", encoding="utf-8") as log_file, RedirectStdoutTo(log_file):
        # do stuff here

    :param out_new:
    """

    def __init__(self, out_new):
        self.out_new = out_new

    def __enter__(self):
        self.out_old = sys.stdout
        sys.stdout = self.out_new

    def __exit__(self, *args):
        sys.stdout = self.out_old


if __name__ == "__main__":
    raise InvalidOperationError("Library code shouldn't be run directly.")
"""
Custom exceptions
"""


def exception_intercept(exception: Exception, **extra: dict) -> None:
    """ Interceptor to overwrite unhlanded exceptions in high-failure locations """
    raise exception


class BadStation(Exception):
    """ Station does not exist """


class InvalidRequest(Exception):
    """ Unable to fetch data """


class SourceError(Exception):
    """ Source servers returned an error code"""

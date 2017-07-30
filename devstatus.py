import re
import psutil
import misc
import socket
from mylogger import iotlogger

logger = iotlogger(loggername="DevStatus")

def handle_exception(function):
    def wrapper_function(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as e:
            logger.error("Error with " + str(function.func_name) + ":" + str(e), exc_info=True)
            return {}
    return wrapper_function

@handle_exception
def cpuStats():
    logger.debug('Obtaining cpustats')
    cpu_load = {'cpu_load': psutil.cpu_percent(percpu=False)}
    return cpu_load

def stats():
    cpu_stats = cpuStats()
    status_ping = {}
    status_ping.update(cpu_stats)
    return status_ping

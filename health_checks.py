#!/usr/bin/env python3

import shutil
import psutil
import socket
import os
import emails

def check_disk_usage(disk):
        du=shutil.disk_usage(disk)
        free=du.free/du.total*100
        print("free:"+str(free>20))
        return free>20

def check_cpu_usage():
        cpu_usage=psutil.cpu_percent(1)
        print("cpu_usage:"+str(cpu_usage<80))
        return cpu_usage<80

def check_memory_usage():
        memory_usage=psutil.virtual_memory()
        mb=1024*1024 #500MB
        mem_available_mb=memory_usage.available/mb
        print("memory_usage:"+str(memory_usage))
        return mem_available_mb>500

def check_hostname():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        IP=socket.gethostbyname('localhost')
        if IP  == '127.0.0.1' or IP  == '::1':
                return True
        else:
                return False


if __name__=='__main__':
        sender = "automation@example.com"
        receiver = "{}@example.com".format(os.environ.get('USER'))
        body = "Please check your system and resolve the issue as soon as possible."

        if not check_disk_usage("/"):
                print("ERROR")
                subject="Error - Available disk space is less than 20%"
                message=emails.generate_error_report(sender, receiver, subject, body)
                emails.send_email(message)

        elif not check_cpu_usage():
                print("ERROR")
                subject="Error - CPU usage is over 80%"
                message=emails.generate_error_report(sender, receiver, subject, body)
                emails.send_email(message)

        elif not check_memory_usage():
                print("ERROR")
                subject="Error - Available memory is less than 500MB"
                message=emails.generate_error_report(sender, receiver, subject, body)
                emails.send_email(message)

        elif not check_hostname():
                print("ERROR")
                subject="Error - localhost cannot be resolved to 127.0.0.1"
                message=emails.generate_error_report(sender, receiver, subject, body)
                emails.send_email(message)
        else:
                print("Everything is OK!")

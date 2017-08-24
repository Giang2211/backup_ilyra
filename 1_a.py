#!/usr/bin/env python
from socketIO_client import SocketIO, LoggingNamespace
import time
import datetime
import os
from apscheduler.schedulers.background import BackgroundScheduler
import logging
import json
import RPi.GPIO as GPIO  
from time import sleep  

GPIO.setmode(GPIO.BCM)  
GPIO.setwarnings(False)  	       # Disable Warnings
OutputPins = [22, 23, 24, 25, 26, 27]  # Set the GPIO pins that are required

#Set our GPIO pins to outputs and set them to off
for i in OutputPins:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, False)
print ('Default for gpio ports are False \n')

#------------------------------------------------------------
logging.getLogger('socketIO-client').setLevel(logging.DEBUG)
logging.basicConfig()

DEBUG = True
def log(message):
    if DEBUG:
	print str(message)
def on_connect():
    print('connect')
    print datetime.datetime.now()
def on_disconnect():
    print('disconnect')
    print datetime.datetime.now()
def on_reconnect():
    print('reconnect')
    print datetime.datetime.now()
    socketIO.emit("get",emit_data)

def on_aaa_response(*args):
    print('on_aaa_response', str(args))
    print '\nXXXX'
    print datetime.datetime.now()
    gpio = args[0]['port']
    status = args[0]['status']
    print ("decode json done!\n")
    
    for i in range (0,10): 	
    	if gpio == i or gpio == '1':
		print 'Port %d check commnad !\n'%i
		if status == 1 or status == '1':
			print "===================ON======================\nexec"
			GPIO.output(i+21, True)
	        if status == 0  or status == '0':
			print "===================OFF======================\nexec"
			GPIO.output(i+21, False)
	
def command_task(messageID,gpio,time):
    if gpio == '22':
        GPIO_22(messageID,time)
    
def schedule_task(messageID,gpio,time):
    print "schedule task"

def update_state(messageID):
    print "update state"

def GPIO_22(message,interval):
    print "--------  GPIO_22 -----------"
    log(datetime.datetime.now())   
    #command = 'python /home/pi/actuator/GPIO_22.py'+' '+message+' '+str(interval)
    #procs = subprocess.Popen(command,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,)
    #stdout,stderrs = procs.communicate('through stdin to stdout\n')
    #procs.wait()
    #log(stdout)
def GPIO_23(message,interval):
    print "--------  GPIO_23 -----------"
    log(datetime.datetime.now())
    #command = 'python /home/pi/actuator/GPIO_23.py'+' '+message+' '+str(interval)
    #procs = subprocess.Popen(command,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,)
    #stdout,stderrs = procs.communicate('through stdin to stdout\n')
    #procs.wait()
    #log(stdout)
def GPIO_24(message,interval):
    print "--------  GPIO_24 -----------"
    log(datetime.datetime.now())
    command = 'python /home/pi/actuator/GPIO_24.py'+' '+message+' '+str(interval)
    procs = subprocess.Popen(command,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,)
    stdout,stderrs = procs.communicate('through stdin to stdout\n')
    procs.wait()
    log(stdout)
def GPIO_25(message,interval):
    print "--------  GPIO_25 -----------"
    log(datetime.datetime.now())
    command = 'python /home/pi/actuator/GPIO_25.py'+' '+message+' '+str(interval)
    procs = subprocess.Popen(command,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,)
    stdout,stderrs = procs.communicate('through stdin to stdout\n')
    procs.wait()
    log(stdout)
def GPIO_26(message,interval):
    print "--------  GPIO_26 -----------"
    log(datetime.datetime.now())
    command = 'python /home/pi/actuator/GPIO_26.py'+' '+message+' '+str(interval)
    procs = subprocess.Popen(command,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,)
    stdout,stderrs = procs.communicate('through stdin to stdout\n')
    procs.wait()
    log(stdout)
def GPIO_27(message,interval):
    print "--------  GPIO_27 -----------"
    log(datetime.datetime.now())
    command = 'python /home/pi/actuator/GPIO_27.py'+' '+message+' '+str(interval)
    procs = subprocess.Popen(command,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,)
    stdout,stderrs = procs.communicate('through stdin to stdout\n')
    procs.wait()
    log(stdout)
def timeout():
    print " -----  Rewaiting --------"
    socketIO.wait(20)

#emit_data = {"url": "/actuator/34/communicate"}
emit_data = "cambien2"

query = {
    "__sails_io_sdk_version": "0.13.8",
    "__sails_io_sdk_platform": "browser",
    "__sails_io_sdk_language": "javascript"
}
def pushData():
    headers = {'Authorization': 'Basic aWx5cmE6NzAzZmMxNDUwMDk2MTg1ZDZmYzAwMzQ5YzhlOGQ2ZjU='}
    payload = {
               "name":"SS_DATA",
                "nodeId":'SACSYCHY778483477873YHSH',
                "data":str(type)+""+str(Message),
                "time":str(datetime.datetime.utcnow().isoformat())
               }
    socketIO.emit(headers)
	
#scheduler = BackgroundScheduler()
#socketIO = SocketIO('192.168.5.74:3484')
socketIO = SocketIO('io.ilyra.vn:80')

#    params=query)
socketIO.on('connect', on_connect)
socketIO.on('disconnect', on_disconnect)
socketIO.on('reconnect', on_reconnect)
#socketIO.emit("get",emit_data)
socketIO.emit("join",emit_data)
socketIO.on('controlDevice', on_aaa_response)
socketIO.wait()
#scheduler.add_job(timeout, 'interval', seconds=20)
# Wait for some seconds
#scheduler.start()
try:
        # This is here to simulate application activity (which keeps the main thread alive).
    while True:
        time.sleep(0.1)
	#socketIO.emit("join",emit_data)
	#socketIO.on('command', on_aaa_response)
	#socketIO.wait()

except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
    scheduler.shutdown()


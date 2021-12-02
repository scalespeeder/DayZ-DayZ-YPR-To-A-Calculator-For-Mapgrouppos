#!/usr/bin/env python3
# python script written by t0y shop for Scalespeeder
# maths supplied by Scalespeeder
import json
import sys
from os.path import exists

if len(sys.argv) != 2:
    print ("You must provide a valid file path")
    exit(1)

filepath = sys.argv.pop()

if (exists(filepath) == False):
    print(f"file {filepath} does not exist")
    exit(1) 

def convert_y_to_a(yaw):
    if yaw < -90:
        return (-180 - yaw) - 90
    elif yaw < 0:
        return (180 - yaw) - 90
    else:
        return (360 - yaw) - 270

f = open(filepath)
try:
    data = json.load(f)
    for object in data['Objects']:

        outputString = f"<group name=\"{object['name']}\" pos=\"{object['pos'][0]} {object['pos'][1]} {object['pos'][2]}\""
        outputString += f" rpy=\"{object['ypr'][2]} {object['ypr'][1]} {object['ypr'][0]}\"" 
        outputString += f" a=\"{convert_y_to_a(object['ypr'][0])}\" />"
        print(outputString)
except:
    print ("Could not parse the supplied file")
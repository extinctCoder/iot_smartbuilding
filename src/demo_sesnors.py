import paho.mqtt.publish as publish
from time import sleep
from random import random

if __name__ == "__main__":
    while True:
        print("publising data")
        publish.single("l1/101/current", random(), hostname="127.0.0.1")
        publish.single("l1/101/voltage", random(), hostname="127.0.0.1")
        publish.single("l1/101/power", random(), hostname="127.0.0.1")
        publish.single("l1/101/control", random(), hostname="127.0.0.1")
        publish.single("l1/102/current", random(), hostname="127.0.0.1")
        publish.single("l1/102/voltage", random(), hostname="127.0.0.1")
        publish.single("l1/102/power", random(), hostname="127.0.0.1")
        publish.single("l1/102/control", random(), hostname="127.0.0.1")
        publish.single("l1/103/current", random(), hostname="127.0.0.1")
        publish.single("l1/103/voltage", random(), hostname="127.0.0.1")
        publish.single("l1/103/power", random(), hostname="127.0.0.1")
        publish.single("l1/103/control", random(), hostname="127.0.0.1")
        publish.single("l2/101/current", random(), hostname="127.0.0.1")
        publish.single("l2/101/voltage", random(), hostname="127.0.0.1")
        publish.single("l2/101/power", random(), hostname="127.0.0.1")
        publish.single("l2/101/control", random(), hostname="127.0.0.1")
        publish.single("l2/102/current", random(), hostname="127.0.0.1")
        publish.single("l2/102/voltage", random(), hostname="127.0.0.1")
        publish.single("l2/102/power", random(), hostname="127.0.0.1")
        publish.single("l2/102/control", random(), hostname="127.0.0.1")
        publish.single("l2/103/current", random(), hostname="127.0.0.1")
        publish.single("l2/103/voltage", random(), hostname="127.0.0.1")
        publish.single("l2/103/power", random(), hostname="127.0.0.1")
        publish.single("l2/103/control", random(), hostname="127.0.0.1")
        sleep(0.5)

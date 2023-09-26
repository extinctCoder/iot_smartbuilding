import paho.mqtt.publish as publish
from time import sleep
from random import random

if __name__ == "__main__":
    while True:
        print("publishing data")
        publish.single("/room/101/current", random(), hostname="127.0.0.1")
        publish.single("/room/101/voltage", random(), hostname="127.0.0.1")
        publish.single("/room/101/power", random(), hostname="127.0.0.1")
        publish.single("/room/101/alert", f"Alert: {random()}", hostname="127.0.0.1")
        # publish.single("room/101/control", random(), hostname="127.0.0.1")
        publish.single("/room/102/current", random(), hostname="127.0.0.1")
        publish.single("/room/102/voltage", random(), hostname="127.0.0.1")
        publish.single("/room/102/power", random(), hostname="127.0.0.1")
        publish.single("/room/102/alert", f"Alert: {random()}", hostname="127.0.0.1")
        # publish.single("room/102/control", random(), hostname="127.0.0.1")
        publish.single(
            "/room/103/current", f"{random()}: {random()}", hostname="127.0.0.1"
        )
        publish.single("/room/103/voltage", random(), hostname="127.0.0.1")
        publish.single("/room/103/power", random(), hostname="127.0.0.1")
        publish.single("/room/103/alert", random(), hostname="127.0.0.1")
        # publish.single("room/103/control", random(), hostname="127.0.0.1")
        publish.single("/room/201/current", random(), hostname="127.0.0.1")
        publish.single("/room/201/voltage", random(), hostname="127.0.0.1")
        publish.single("/room/201/power", random(), hostname="127.0.0.1")
        publish.single("/room/201/alert", random(), hostname="127.0.0.1")
        # publish.single("room/201/control", random(), hostname="127.0.0.1")
        publish.single("/room/202/current", random(), hostname="127.0.0.1")
        publish.single("/room/202/voltage", random(), hostname="127.0.0.1")
        publish.single("/room/202/power", random(), hostname="127.0.0.1")
        publish.single("/room/202/alert", random(), hostname="127.0.0.1")
        # publish.single("room/202/control", random(), hostname="127.0.0.1")
        publish.single("/room/203/current", random(), hostname="127.0.0.1")
        publish.single("/room/203/voltage", random(), hostname="127.0.0.1")
        publish.single("/room/203/power", random(), hostname="127.0.0.1")
        publish.single("/room/203/alert", random(), hostname="127.0.0.1")
        # publish.single("room/203/control", random(), hostname="127.0.0.1")
        sleep(0.5)

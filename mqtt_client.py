# # Copyright (c) 2010,2011 Roger Light <roger@atchoo.org>
# # All rights reserved.
# #
# # Redistribution and use in source and binary forms, with or without
# # modification, are permitted provided that the following conditions are met:
# #
# # 1. Redistributions of source code must retain the above copyright notice,
# #   this list of conditions and the following disclaimer.
# # 2. Redistributions in binary form must reproduce the above copyright
# #   notice, this list of conditions and the following disclaimer in the
# #   documentation and/or other materials provided with the distribution.
# # 3. Neither the name of mosquitto nor the names of its
# #   contributors may be used to endorse or promote products derived from
# #   this software without specific prior written permission.
# #
# # THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# # AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# # IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# # ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# # LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# # CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# # SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# # INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# # CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# # ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# # POSSIBILITY OF SUCH DAMAGE.
#
# import socket
#
# import paho.mqtt.client as mqtt
# import os
# from urllib.parse import urlparse
#
#
# # Define event callbacks
# def on_connect(client, userdata, flags, rc):
#     print("Connected with result code " + str(rc))
#     # Subscribing in on_connect() means that if we lose the connection and
#     # reconnect then subscriptions will be renewed.
#     client.subscribe("sensor/motion")
#     client.subscribe("sensor/light")
#     client.subscribe("sensor/moisture")
#
#
# def on_message(client, obj, msg):
#     if msg.topic == "sensor/motion":
#         pass
#
#     print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
#
#
# def on_publish(client, obj, mid):
#     print("mid: " + str(mid))
#
#
# def on_subscribe(client, obj, mid, granted_qos):
#     print("Subscribed: " + str(mid) + " " + str(granted_qos))
#
#
# def on_log(client, obj, level, string):
#     print(string)
#
#
# mqttc = mqtt.Client(transport="websockets")
# mqttc.tls_set()
# # Assign event callbacks
# mqttc.on_message = on_message
# mqttc.on_connect = on_connect
# mqttc.on_publish = on_publish
# mqttc.on_subscribe = on_subscribe
#
# # Uncomment to enable debug messages
# # mqttc.on_log = on_log
#
# mqttc.username_pw_set("pljcjeom", "pCWWNWHzPsBk")
# # Connect
# mqttc.connect("driver.cloudmqtt.com", 38893)
#
# # Continue the network loop, exit when an error occurs
#
# mqttc.loop_start()
#
# while True:
#     pass

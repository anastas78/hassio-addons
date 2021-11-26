import eventlet
import socketio
from paho.mqtt import client as mqtt_client

eventlet.monkey_patch()

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': '/config/weewx/html/'
})

def emit_msg (sid, msg, data) :
    sio.emit(msg, data, to=sid)
    
@sio.event
def mqtt_conf(sid, data): 
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
            emit_msg(userdata, "mqtt_data", "Connected to MQTT" )
        else:
            print("Failed to connect, return code %d\n", rc)
    def on_message(client, userdata, msg):
        emit_msg(userdata, "mqtt_data", msg.payload.decode())
    
    broker = data['broker']
    port = data['port']
    topic = data['topic']
    username = data['username']
    password = data['password']
    
    global client
 
    client = mqtt_client.Client()
    client.username_pw_set(username, password)
    client.user_data_set(sid)
    client.connect(broker, port)
    client.on_connect = on_connect
    client.on_message = on_message
    client.subscribe(topic)
    client.loop_start()
 
if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 80)), app)
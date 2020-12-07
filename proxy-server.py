import socket, sys, logging
from _thread import *
import os
import time
import random

logging.basicConfig(filename='proxy.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
try:
    image_dir = os.system("mkdir /root/images")
    if(image_dir == 0):
        print("--- Checkpoint Image directory created")
    else:
        print("--- [Error] image directory exists")    
except:
    print("Some other error occured. Please run this script again")

os.system("docker stop $(docker ps -aq)")

def create_main_webserver():
    os.system("docker stop -f $(docker ps -aq) && docker rm /main_web")
    os.system("docker-compose build")
    time.sleep(5)
    os.popen("docker run -dit --name main_web root_web-server")



# Creating vulnerable docker images if none exist
image_list = os.popen("docker images --format \"{{.Repository}}\"").read().split("\n")

if(image_list == '' or ('root_web-server' not in image_list)):
    print('--- Main webserver image does not exist.\n---Creating and running')
    print('root_web-server' not in image_list)
    create_main_webserver()


else:
    print("--- Main webserver image exists. Continuing execution")
    ## Running webserver
    print("--- Running Main webserver.")

    if('root_web-server' in os.popen("docker ps --format \"{{.Image}}\"").read().split("\n")):
        print("--- Main webserver is already running")
    else:
        print("--- Removing previous container")
        os.system("docker rm /main_web")
        print("--- Starting main webserver container")
        os.popen("docker run -dit --name main_web root_web-server")
        time.sleep(5)

webserver_exists = True




try:
    listening_port = int(input("#-------------------\n\t Enter a port number to listen on: "))
    # listening_port = 9000
    # listening_port_1 = 9001
except KeyboardInterrupt:
    print("\n#-------------------\nProxy shutdown command received...")
    print("Shutting down proxy server...Goodbye!")
    sys.exit()

max_connections = 100
buffer_size = 81920000

## This is the listener socket code
def start():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("--- Initializing socket")

        # try:
        s.bind(('', listening_port))
        print("--- Binding socket to port :"+str(listening_port))
        # except:
        #     s.bind(('', listening_port_1))
        #     print("--- Binding socket to port :"+str(listening_port_1))
        
        s.listen(max_connections)
        print("--- Proxy server started")

    except Exception as e:
        print("--- ERROR ---\nSocket Initialization failed. Server could not be started")
        logging.error("--- ERROR ---\nSocket Initialization failed. Server could not be started")
        logging.error(e)
        sys.exit(2)

    # while True:
    try:
        connection_socket, addr = s.accept()
        # print("Printing address#########")
        print(connection_socket)
        data = connection_socket.recv(buffer_size)
        ## Start new thread for the connection, and send con
        
        ## Check for malicious connection.
        temp = data.decode("utf-8")
        temp = temp.split(" ")[1]

        # Malicious connection ----------------
        if(temp == "/malicious"):
            ### ALL REDIRECT SOCKET CODE HERE -------------------------------------------
            print("\n--- Malicious attack attempt. Redirecting connection to decoy container.")
            os.system("echo ---BASH--- Starting docker checkpoint and restore script")

            decoy_uid = random.random()
            # Take checkpoint of main_webserver
            checkpoint_cmd = "docker checkpoint create --checkpoint-dir=/images main_web "+str(decoy_uid)+"_decoy --leave-running=true"
            checkpoint_created = os.popen(checkpoint_cmd).read()
            print(checkpoint_created)
            # Start the decoy container
            exit(0)

            
            # Getting the IP address out
            ip_address_decoy = os.popen("docker inspect $(docker ps -q) | grep IPA").read()
            ip_address_decoy = ip_address_decoy.split("\n")[1].split("\"")[-2]
            
            
            # socket_to_decoy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # socket_to_decoy.connect((ip_address_decoy, 80))

        # Benign connection ----------------
        else:
            ## Start new thread
            start_new_thread(conn_string, (connection_socket, data, addr))

        

        
    except KeyboardInterrupt:
        s.close()
        print("\nKeyboard Interrupt received.\nShutting down proxy server...Goodbye!")
        sys.exit(1)

    except Exception as e:
        print(e)
        pass
    s.close()

## conn_string would decide where the packet should be sent.
def conn_string(connection_socket, data, addr):
    try:
        # print(data)
            # # Extracting first line
            # first_line = data.split('\n')[0]
            
            # url = first_line.split(' ')[1]
            
            # http_pos = url.find("://")
            # if(http_pos == -1):
            #     temp = url
            # else:
            #     temp = url[(http_pos+3):]
            
            # port_pos = temp.find(':')

            # webserver_pos = temp.find("/")
            # if(webserver_pos == -1):
            #     webserver_pos = len(temp)
            # webserver = ''
            # port = -1
            # if(port_pos == -1 or webserver_pos < port_pos):
            #     port = 80
            #     webserver = temp[:webserver_pos]
            # else:
            #     port = int((temp[(port_pos+1):])[:webserver_pos-port_pos-1])
            #     webserver = temp[:port_pos]
        
        ## Add switch logic here ---------------
        proxy_server('172.17.0.2', 443, connection_socket, addr, data)
    except Exception as e:
        pass


## Function to proxy the connection to correct docker container.
def proxy_server(webserver, port, socket_to_proxy, addr, data):
    try:
        
        socket_to_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
        try:
            socket_to_server.connect((webserver, port))
        except Exception as e:
            print(e)

        # print("Sending the hello packet to Server")
        # print(data)
        socket_to_server.send(data)
        count = 0
        while True:
            
            
            reply = socket_to_server.recv(buffer_size)
            count += 1
            # print('Reply received -----------------', count)
            # print(reply)
            if(len(reply) > 0):
                
                socket_to_proxy.send(reply)

                dar = float(float(len(reply))/1024)
                dar = "%.3s" % (str(dar))
                dar = "%s KB" % (dar)

                print("--- Request done: %s => %s <=" % (str(addr[0]), str(dar)))
            else:
                break
        # Close socket towards the server
        socket_to_server.close()
        # Close socket towards the proxy
        socket_to_proxy.close()
    
    except socket.error:
        # Close socket towards the server
        socket_to_server.close()
        # Close socket towards the proxy
        socket_to_proxy.close()
        sys.exit()
                

## Replace this with if main code snippet. This is the entry point of code.
start()
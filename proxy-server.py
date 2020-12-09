import socket, sys, logging
from _thread import *
import os
import time
import random
from datetime import datetime

# Setting up logging
dt = (datetime.now()).strftime("%H%M%S_%m%d%Y")
log_filename = "/root/proxy-server/proxy_"+dt+".log"

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(filename=log_filename, filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.NOTSET)

def print_and_log(msg, loglevel="info"):
    """
    This function prints and logs the message. 
    Default loglevel is info.
    """

    # Printing message
    print("\n"+msg)

    # Logging message
    if(loglevel == "info"):
        logging.info(msg)
    elif(loglevel == "debug"):
        logging.debug(msg)
    elif(loglevel == "error"):
        logging.error(msg)
    else:
        print("Logging level not info, debug or error. Please check code. Here's the error message that failed \n\n"+msg+"\n\nHere's the logging level: "+loglevel)

# Make folder to store docker images
try:
    # Running command
    image_dir_cmd_response = os.system("mkdir /root/images")

    # Check if folder exists
    if(image_dir_cmd_response == 0):
        print_and_log("--- [INFO] Checkpoint Image directory created", "info")

    elif(image_dir_cmd_response == 256):
        print_and_log("--- [INFO] image directory exists", "info")

    else:
        print_and_log("--- [ERROR] Something went horribly wrong. "
                    + "Check if folder exists at /root/mkdir. Back it up and re run this script", "error")

except:
    print_and_log("--- [WEIRD ERROR] Some other error occured. Please run this script again", "error")


def get_container_ip(cont_id):
    """ 
    This function gets the IP based on the container ID.
    """
    try:
        ip_address = os.popen("docker inspect "+cont_id+" | grep IPA").read().split(":")[-1].split("\"")[1]
        print_and_log("--- [INFO] IP address of container "+cont_id+" located. Storing it", "info")
    except Exception as e:
        print_and_log("--- [ERROR] IP address of container "+cont_id+" couldn't be found. Error message follows", "error")
    


def create_main_webserver():
    """
    This function creates and runs the main webserver
    """
    
    target_container_name = 'webserver-main'
    target_image_name = 'webserver'

    # Check if the webserver is running
    list_running_containers = os.popen("docker ps --format {{.Names}}").read().split("\n")[:-1]
    
    
    list_all_containers = os.popen("docker ps --format {{.Names}} -a").read().split("\n")[:-1]
    list_all_containers_status = os.popen("docker ps --format {{.Status}} -a").read().split("\n")[:-1]
    list_of_images = os.popen("docker images --format {{.Repository}}").read().split("\n")[:-1]
    # Check the list of containers
    if(target_container_name in list_running_containers):
        print_and_log("--- [INFO] Target Webserver is running. Starting reverse proxy module.", "info")
        return True
    
    # Target webserver not running start it up
    elif(target_container_name in list_all_containers):
        print_and_log("--- [INFO] Target Webserver not running. Attempting to start it.", "info")
        
        # Looking for target webserver location in list.
        index_container = list_all_containers.index(target_container_name)

        # Target web server was stopped
        if('Exited' in list_all_containers_status[index_container]):
            print_and_log("--- [INFO] Target Webserver was stopped. Starting container again.", "info")
            
            # Checking for successful start
            start_wbserver_status = os.popen("docker start "+target_container_name).read().split("\n")[:-1]
            if('webserver-main' == start_wbserver_status[0]):
                print_and_log("--- [INFO] Target Webserver is now running. Starting reverse proxy module.", "info")
                return True
            else:
                status_docker_all = os.popen("docker ps -a").read()
                print_and_log("--- [ERROR] Error occured. Check your docker containers.\nDocker status follows", "error")
                print_and_log(status_docker_all, "info")
                return False
        else:
            status_docker_all = os.popen("docker ps -a").read()
            print_and_log("--- [ERROR] Error occured. Check your docker containers.\nDocker status follows", "error")
            print_and_log(status_docker_all, "info")
            return False
    
    # Check if target image exists
    elif('webserver' in list_of_images):            
        print_and_log("--- [INFO] Target Webserver docker image found. Starting it.", "info")
        run_target_webserver = os.popen("docker run -d --name webserver-main --expose 80 webserver").read().split("\n")[:-1]
        container_id = run_target_webserver[0][:12]

        # Check if container started successfully
        list_running_containers_temp = os.popen("docker ps --format {{.ID}}_{{.Names}}").read().split("\n")[:-1]
        container_uid = container_id+"_webserver-main"
        if(container_uid in list_running_containers_temp):
            print_and_log("--- [INFO] Target webserver container has been started. Container_ID: "+container_id, "info")
            return True
        else:
            print_and_log("--- [ERROR] Couldn't start Target webserver. Please check images and running container list", "error")
            return False

    elif(('webserver' not in list_of_images) or (list_of_images == [])):
        print_and_log("--- [INFO] Target Webserver image not found. Building and deploying it.", "info")
        build_image = os.popen("docker build -t webserver /root/webserver/.").read().split("\n")[:-1][-1]
        
        # Check if build was success
        if(build_image.split(" ")[0] == "Successfully"):
        
            # Get image ID and images ID out
            temp_uid = build_image.split(" ")[-1]
            temp_image_ids = os.popen("docker images --format {{.ID}}").read().split("\n")[:-1]
        
            # Check if the IDs match and then start the container
            if(temp_uid in temp_image_ids):
                print_and_log("--- [INFO] Docker container built. Running it now.", "info")
                run_target_webserver_from_image = os.popen("docker run -d --name webserver-main --expose 80 webserver").read().split("\n")[:-1]
                
                # Getting container's uid out
                container_temp_uid = run_target_webserver_from_image[0][:12]
                # Getting all container's UIDs out
                list_running_containers_1 = os.popen("docker ps --format {{.ID}}").read().split("\n")[:-1]
                
                # Check if container runs
                if(container_temp_uid in list_running_containers_1):
                    print_and_log("--- [INFO] Webserver image created and container running. Starting proxy server", "info")
                    return True
                # Container won't run.
                else:
                    print_and_log("--- [ERROR] Webserver image created but container not running. Check if container can be run. Error follows", "error")
                    print_and_log(str(os.popen("docker run -d --name webserver-main --expose 80 webserver").read()), "error")
                    return False
            else:
                print_and_log("--- [ERROR] Webserver image IDs don't match. Check docker status.", "error")
                return False
        else:
            print_and_log("--- [ERROR] Image building failed. Error follows", "error")
            print_and_log(str(os.popen("docker build -t webserver /root/webserver/.").read()), "error")
    
    else:
        print_and_log("--- [ERROR] Honestly no clue what happened. Running diagnostics", "error")
        # Print all docker images
        list_of_docker_images = os.popen("docker images").read().split("\n")[-1]
        for line in list_of_docker_images:
            print(line)
        # Print all containers stopped and running
        list_of_docker_containers = os.popen("docker ps -a").read().split("\n")[-1]
        for line in list_of_docker_containers:
            print(line)

        print_and_log("--- [ERROR] And terminating function", "error")
        return False
        


# Run the target webserver
target_webserver_running = create_main_webserver()

def get_new_port(old_port):
    new_listening_port = int(input("--- "+str(old_port)+"didn't work. Enter another port number."))
    return new_listening_port

# Start the proxy server
try:
    listening_port = int(input("#-------------------\n\t Enter a port number to listen on: "))
    
except KeyboardInterrupt:
    print("\n#-------------------\nProxy shutdown command received...")
    print("Shutting down proxy server...Goodbye!\n\n")
    sys.exit()


max_connections = 100
buffer_size = 81920000

## This is the listener socket code
def start():
    try:
        # Set up the socket
        world_facing_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print_and_log("--- [INFO] Initializing socket", "info")
        print

        try:
            world_facing_socket.bind(('', listening_port))
            print_and_log("--- [INFO] Listening on port :"+str(listening_port), "info")
        except Exception as e:
            print_and_log("--- [ERROR] Binding to port: "+str(listening_port)+" failed.")
            new_port = get_new_port(listening_port)
            world_facing_socket.bind(("", new_port))
        
        world_facing_socket.listen(max_connections)
        print_and_log("--- [INFO] Proxy server started")

    except Exception as e:
        print_and_log("--- ERROR Socket Initialization failed. Server could not be started. Error message follows.")
        print_and_log(e, "error")
        sys.exit(2)


    try:
        # Get data from socket
        connection_socket, addr = world_facing_socket.accept()

        # Collect data
        data = connection_socket.recv(buffer_size)
        
        ## Start new thread for the connection, and send con
        ## Check for malicious connection.
        temp = data.decode("utf-8")
        temp = temp.split(" ")[1]

        # Malicious connection ----------------
        if(temp == "/malicious"):

            ### ALL REDIRECT SOCKET CODE HERE -------------------------------------------
            print_and_log("--- [ATTACK] Malicious attack attempt. Redirecting connection to decoy container.", "info")
            print_and_log("--- [INFO] Starting docker checkpoint and restore script", "info")

            decoy_uid = str(round(random.uniform(1, 100000), 0))[:-2]
            decoy_checkpoint_name = decoy_uid+"_decoy"


            # Take checkpoint of main_webserver
            checkpoint_cmd = "docker checkpoint create --checkpoint-dir=/root/images webserver-main "+decoy_checkpoint_name+" --leave-running=true"
            checkpoint_created = os.popen(checkpoint_cmd).read().split("\n")[-1]

            if(checkpoint_created == decoy_checkpoint_name):
                print_and_log("--- [INFO] Checkpoint created successfully "+checkpoint_created, "info")
                print_and_log("--- [INFO] Starting decoy container", "info")

                create_clone = os.popen("docker create --name webserver_"+decoy_uid+" webserver")

            

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
import sys
import socket
import time

# Check command line arguments
if len(sys.argv) != 2:
    print("Usage: python udpLoadBalancer.py <load balancer port>")
    sys.exit()

# Create a UDP socket for load balancer
loadBalancerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
loadBalancerSocket.bind(('localhost', int(sys.argv[1])))

# List of server addresses
serverAddresses = [('localhost', 2526), ('localhost', 2527), ('localhost', 2528)]
current_server_index = 0

while True:
    # Receive request from client
    request, client_address = loadBalancerSocket.recvfrom(1024)

    # Send request to the current server in a round-robin manner
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSocket.sendto(request, serverAddresses[current_server_index])
    serverSocket.settimeout(1)

    try:
        # Receive response from the server
        response, _ = serverSocket.recvfrom(1024)
        current_time = time.strftime("%H:%M:%S")
        print(f"b'{response.decode()} (This message came from load balancer!!!) The port of this server is {serverAddresses[current_server_index][1]}'")
    except socket.timeout:
        print('REQUEST TIMED OUT')

    # Close the server socket
    serverSocket.close()

    # Update the current server index for the next request
    current_server_index = (current_server_index + 1) % len(serverAddresses)
1.Introduction and Problem Statement
In this assignment, the focus is on understanding the functionality of a UDP load balancer. A UDP load balancer operates at the transport layer in the OSI model, utilizing the User Datagram Protocol (UDP). This assignment explores the intermediary role of UDP in communication between an application program and the Internet Protocol. The fundamental concept demonstrated here is how a UDP load balancer efficiently distributes incoming requests to various local servers. Initially, the assignment involves examining sample Internet ping servers and a corresponding client implemented in Python.	


2.Assignment Objectives 
The features that the project should have are as follows: 
• Implement the udpLoadBalancer class to facilitate the distribution of client requests among the three servers in a cyclic order.
• Guarantee continuity in the distribution sequence, so that if the client requests again, the distribution resumes from the point where it left off.
• Ensure that the ping distribution adheres to a specific sequence, where the first incoming ping is directed to Server1, followed by Server2, Server3, and so on in a cyclical pattern.


3.Assignment Design, Methods and Procedures
In this assignment, communication was provided through the terminal. In the terminal, questions and options appear in front of the client, and the answers given by the server are displayed.
udpLoadBalancer.py:The necessary libraries for the code are imported in this part, which marks the beginning of the code. It checks if the script is executed with the correct number of command line arguments. A UDP socket is created and assigned to the specified port on the local machine. In the final part, server addresses are stored in an array as IP and port numbers.
The processes are executed in a loop within the while loop. The operations can be explained in the following sequence:
•	It creates a new socket (serverSocket) and sends the received request to the current server defined by the 'current_server_index.'
•	It waits for a response from the server. If a response is received, it is stored in the variable 'response.'
•	It prints the response received from the server along with additional information, such as the origin of the message from the load balancer, the port of the server that processed the request, and the timestamp.
•	The index is incremented to point to the next server in a round-robin fashion. This ensures that subsequent requests are distributed among the three servers in order.
•	The script continues to run indefinitely, handling incoming requests, sending them to servers, receiving responses, and printing the relevant information.

<img width="480" alt="image" src="https://github.com/ymerta/udp-loader/assets/107405633/64740fd1-03b6-46fa-904f-57e7c60b3560">
(1)
We start our servers in separate terminals with the command 'python server.py' and keep them ready to receive incoming messages. 

<img width="481" alt="image" src="https://github.com/ymerta/udp-loader/assets/107405633/000270d1-e8aa-47b0-9dd4-7df9cd3e9a64">
(2)
Then, we run our UDP load balancer in the terminal with the command 'python udpLoadBalancer.py 8888'.

<img width="478" alt="image" src="https://github.com/ymerta/udp-loader/assets/107405633/961d8cbf-293b-4345-8b16-7e519636ddb9">
(3)
Finally, we activate our client side by running the command 'python UDPPingerClient.py localhost 8888', initiating the transferring process.

<img width="478" alt="image" src="https://github.com/ymerta/udp-loader/assets/107405633/c37fe3a1-dabf-4ebb-a4eb-353888f3d073">
(4)

After activating the client, we can observe the incoming pings from the load balancer in the server terminals.
<img width="477" alt="image" src="https://github.com/ymerta/udp-loader/assets/107405633/b535081b-7301-4574-aa8e-434ec3e8d84e">
(5)

We activate the client for the second time with the command 'python UDPPingerClient.py localhost 8888'.
<img width="478" alt="image" src="https://github.com/ymerta/udp-loader/assets/107405633/14b448b7-2224-4e8b-a4c9-a1d45d470687">
(6)
After activating the client for the second time, the terminals of the servers look like the (6).

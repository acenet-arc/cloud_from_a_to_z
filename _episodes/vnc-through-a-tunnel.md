---
layout: episode
title: "VNC through a tunnel"
teaching: 20
exercises: 15
questions:
- "What is an SSH tunnel?"
- "What problems are solved by using a tunnel?"
objectives:
- "We'll set up a good approach to VNC"
keypoints:
- "We can set up a secure VNC connection with an SSH tunnel"
- "All of our SSH traffic goes through port 22"
- "Traffic to our VNC server is encrypted"
- "Our VNC server only accepts connections from localhost"
---

```
ssh -L 5901:localhost:5901 <IP for VM>
```

This is actually shorthand for:

```
ssh -L localhost:5901:localhost:5901 <IP for VM>
```

From the man page for ssh:

```
     -L [bind_address:]port:host:hostport
     -L [bind_address:]port:remote_socket
     -L local_socket:host:hostport
     -L local_socket:remote_socket
             Specifies that connections to the given TCP port or Unix socket
             on the local (client) host are to be forwarded to the given host
             and port, or Unix socket, on the remote side.  This works by al‐
             locating a socket to listen to either a TCP port on the local
             side, optionally bound to the specified bind_address, or to a
             Unix socket.  Whenever a connection is made to the local port or
             socket, the connection is forwarded over the secure channel, and
             a connection is made to either host port hostport, or the Unix
             socket remote_socket, from the remote machine.

```

Translation: 'When we send/recieve data to/from port 5901 on our local machine, send it to our cloud VM through the SSH port (22), and send/recieve the data to/from port 5901 there (to localhost on the cloud VM).'


Example trick:

```ssh ubuntu@206.167.180.170 -L 5908:localhost:5901```

Then ```vncviewer :8```

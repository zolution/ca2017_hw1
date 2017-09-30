import socket

if __name__ == '__main__':
    IRCSocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    IRCSocket.connect( ('irc.freenode.net', 6667) )
    NICK = 'robot_077'
    USER = 'zolution testing testing Jason'
    Msg = 'NICK ' + NICK + '\r\nUSER ' + USER + '\r\nJOIN #CN_DEMO \r\nILoveTA\r\n'
    IRCSocket.send(bytes(Msg))

    while True:
        IRCMsg = IRCSocket.recv(4096)
        print IRCMsg


import socket



def sendMsg(Socket, Msg, channel):
    Comd = "PRIVMSG " + channel + " :" + Msg + "\r\n"
    print "--------------" + Comd
    Socket.send(bytes(Comd))

    
if __name__ == '__main__':
    IRCSocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    IRCSocket.connect( ('irc.freenode.net', 6667) )
    NICK = 'robot_077'
    USER = 'zolution testing testing Jason'
    CHANNEL = '#CN_DEMO'
    Msg = 'NICK ' + NICK + '\r\nUSER ' + USER + '\r\nJOIN ' + CHANNEL + '\r\n'
    IRCSocket.send(bytes(Msg))
    sendMsg(IRCSocket, "Hello! I am robot.",CHANNEL)

    while True:
        IRCMsg = IRCSocket.recv(4096)
        print IRCMsg
        if IRCMsg.find(":@repeat") != -1:
            sendMsg(IRCSocket, IRCMsg[IRCMsg.find(":@repeat")+9:], CHANNEL)


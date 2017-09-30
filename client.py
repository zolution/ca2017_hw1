import socket



def sendMsg(Socket, Msg, channel):
    Comd = "PRIVMSG " + channel + " :" + Msg + "\r\n"
    print "--------------" + Comd
    Socket.send(bytes(Comd))

def Convert(Socket, Msg, channel):
    try:
        if Msg[:2] == '0x':
            sendMsg(Socket, str(int(Msg,16)), channel)
        else:
            sendMsg(Socket, hex(int(Msg,0)), channel)
    except:
        sendMsg(Socket, "Invalid Input "+ Msg, channel)

    
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
        for Msg in IRCMsg.split('\r\n'):
            if Msg.find(":@repeat") != -1:
                sendMsg(IRCSocket, IRCMsg[IRCMsg.find(":@repeat")+9:], CHANNEL)
            elif Msg.find(":@convert") != -1:
                Convert(IRCSocket, IRCMsg[IRCMsg.find(":@convert")+10:], CHANNEL)
            elif Msg.find(":@ip") != -1:
                IP(IRCSocket, IRCMsg[IRCMsg.find(":@ip")+5:], CHANNEL)


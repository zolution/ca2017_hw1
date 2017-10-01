import socket
from time import sleep


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
        sendMsg(Socket, "Invalid CONVERT Input "+ Msg, channel)

def IP(Socket, Msg, channel):
    print Msg
    if not Msg.isdigit():
        sendMsg(Socket, "Invalid IP Input "+ Msg, channel)
    else:
        ans = []
        length = len(Msg)
        for i in range(1,length):
            for j in range(i+1,length):
                for k in range(j+1,length):
                    if all(int(elem) >= 0 and int(elem) <= 255 for elem in [Msg[0:i],Msg[i:j],Msg[j:k],Msg[k:length]]):
                        ans.append('.'.join([Msg[0:i],Msg[i:j],Msg[j:k],Msg[k:length]]))
        sendMsg(Socket, str(len(ans)), channel)
        for m in ans:
            sendMsg(Socket, m, channel)
            sleep(0.75)

def Help(Socket, channel):
    sendMsg(Socket, "@repeat <Message>", channel)
    sendMsg(Socket, "@convert <Number>", channel)
    sendMsg(Socket, "@ip <String>", channel)

    
if __name__ == '__main__':
    IRCSocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    IRCSocket.connect( ('irc.freenode.net', 6667) )
    NICK = 'robot_077'
    USER = 'zolution testing testing Jason'
    conf = open('config','r')
    content = conf.read()
    CHANNEL = (content.split('\n'))[0].split('=')[1][1:-1]
    Msg = 'NICK ' + NICK + '\r\nUSER ' + USER + '\r\nJOIN ' + CHANNEL + '\r\n'
    IRCSocket.send(bytes(Msg))
    sendMsg(IRCSocket, "Hello! I am robot.",CHANNEL)

    while True:
        IRCMsg = IRCSocket.recv(4096)
        print IRCMsg
        for Msg in IRCMsg.split('\r\n'):
            if Msg.find(":@repeat") != -1:
                sendMsg(IRCSocket, Msg[Msg.find(":@repeat")+9:], CHANNEL)
            elif Msg.find(":@convert") != -1:
                Convert(IRCSocket, Msg[Msg.find(":@convert")+10:], CHANNEL)
            elif Msg.find(":@ip") != -1:
                IP(IRCSocket, Msg[Msg.find(":@ip")+5:], CHANNEL)
            elif Msg.find(":@help") != -1:
                Help(IRCSocket, CHANNEL)


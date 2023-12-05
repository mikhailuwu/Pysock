def cprint(string):
    print(string)

try: # Import required modules
    import socket
    import sys
    import os

except ImportError as IE: # If import of modules fail, display this message and return/exit with 1 (indicating that execution was a failure).
    cprint(f"Unable to import module(s).\nError: {IE}")
    exit(1)

class sockcli():
    def __init__(self): # Initiates HOST and PORT
        # Use the class-global self.PORT and self.HOST to save memory.
        self.HOST = None
        self.PORT = None
        self.ApplicationProtocols = {
                "HTTP":[],
                }

    def Help(self): # GUESS WHAT?
        cprint("\n")
        cprint(f"Usage: python {sys.argv[0]}\n")
        cprint(" 'connect' or 'c' <address> <port> to connect to specified host")
        cprint("                   or specify address with HOST <address> PORT <integer port>.")
        cprint(" 'close' to close the socket/connection.")
        cprint(" 'send'  or 's' <data> to send specified data via established connection.")
        cprint(" 'recv'  or 'r' <size> to receive data from connection (size is optional).")
        cprint(" 'clear' or 'cls' to clear the console-content.")
        cprint(" 'help' GUESS WHAT?")
        cprint("\n")

    def Connect(self):
        try:
            self.SOCK = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.SOCK.connect((self.HOST, self.PORT))
            cprint("Connected!")
        except ConnectionError as error:
            cprint(f"Failed to connect!\nError: {error}")
        except TimeoutError as error:
            cprint(f"Failed to connect!\nError: {error}")
        except KeyboardInterrupt:
            cprint("ABORT")
        return
    def Send(self, Data=None):
        try:
            self.SOCK.send(f"{Data}".encode('utf-8'))
        except ConnectionError as error:
            cprint(f"Failed to send!\nError: {error}")
        except TimeoutError as error:
            cprint(f"Failed to connect!\nError: {error}")
        except KeyboardInterrupt:
            cprint("ABORT")
        return

    def Recv(self, Size=1024):
        data = None
        try:
            data = self.SOCK.recv(Size)
            return data
        except ConnectionError as error:
            cprint(f"Failed to receive!\nError: {error}")
        except TimeoutError as error:
            cprint(f"Failed to connect!\nError: {error}")
        except KeyboardInterrupt:
            cprint("ABORT")
        return

    def ClearConsole(self):
        os.system("cls")
        return

if(__name__ == "__main__"):
    s = sockcli()
    while(True):
        try:
            COMMAND = input("\n: ").split(" ")
        except KeyboardInterrupt:
            try:
                s.SOCK.close()
            except:
                pass
            exit(0)

        if(COMMAND[0] == "send" or COMMAND[0] == "s"):
            data = None
            if(len(COMMAND) == 0):
                cprint("You need to enter what you want to send (e.g 'Hi' or 10100101).")
                continue
            else:
                for x in range(len(COMMAND)):
                    data = f"{data}{COMMAND[x]}<'"
                try:
                    cprint("Sending ... ")
                    s.Send(Data=data)
                    cprint("Sent!")
                except Exception as error:
                    cprint(f"Unable to send data!\nError: {error}.")
        
        if(COMMAND[0] == "recv" or COMMAND[0] == "r"):
            try:
                if(len(COMMAND) >= 2):
                    cprint("Receiving ... ")
                    cprint(s.Recv(Size=int(COMMAND[1])))
                else:
                    cprint("Receiving ... ")
                    cprint(s.Recv())
            except Exception as error:
                print(f"Unable to receive data!\nError: {error}.")
            except KeyboardInterrupt:
                cprint("STOP RECEIVING!")
                continue

        if(COMMAND[0] == "connect" or COMMAND[0] == "c"):
            if(len(COMMAND) <= 1):
                if(s.HOST == None or s.PORT == None):
                    cprint("You need to specify a HOST and PORT (e.g connect example.com 80),\nor specify HOST,PORT with 'HOST <address>' and 'PORT <integer port>'.")
                    continue
            else:
                s.HOST = COMMAND[1]
                s.PORT = int(COMMAND[2])
            cprint(f"Connecting to {s.HOST}:{s.PORT} ... ")
            try:
                s.Connect()
            except ConnectionError:
                cprint(f"Failed to connect to {s.HOST}:{s.PORT}!")
        
        if(COMMAND[0] == "host" or COMMAND[0] == "h"):
            if(len(COMMAND) < 2):
                if(s.HOST == None):
                    cprint("You need to specify a value for HOST <address>.")
                else:
                    cprint(s.HOST)
            else:
                s.HOST = COMMAND[1]
                cprint(f"HOST -> '{s.HOST}'")
                
        if(COMMAND[0] == "port" or COMMAND[0] == "p"):
            if(len(COMMAND) < 2):
                if(s.PORT == None):
                    cprint("You need to specify a value for PORT <port number>.")
                else:
                    cprint(s.PORT)
            else:
                s.PORT = int(COMMAND[1])
                cprint(f"PORT -> '{s.PORT}'")
                
        if(COMMAND[0] == "close"):
            try:
                s.SOCK.close()
                cprint("Closed!")
            except:
                cprint("Socket was already closed.")
                
        if(COMMAND[0] == "help"):
            s.Help()
            
        if(COMMAND[0] == "exit" or COMMAND[0] == "e"):
            try:
                s.SOCK.close()
            except:
                pass
            exit(0)

        if(COMMAND[0] == "clear" or COMMAND[0] == "cls"):
            s.ClearConsole()

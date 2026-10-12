import threading

import socket

target ="127.0.0.1"

def first_half():

    for ports in range(1,500):

        scan = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        scan.settimeout(0.02)

        try :
            
            
            status = scan.connect_ex((target,ports))

            if(status == 0):

                print(f"port{ports}:OPEN")
        except OSError as error:
            pass
        finally :
            scan.close()
            
def second_half():

    for ports in range(501,1000):
        scan = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        scan.settimeout(0.02)

        try :

            status = scan.connect_ex((target,ports))
            

            if status==0:

                print(f"port{ports}:OPEN")
        except OSError as error:
            pass
        finally :
            scan.close()
def third_half():

    for ports in range(1001,1500):
        scan = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        scan.settimeout(0.02)

        try :

            status = scan.connect_ex((target,ports))
            

            if status==0:

                print(f"port{ports}:OPEN") 
        except OSError as error:
            pass
        finally :
            scan.close()




t1 = threading.Thread(target=first_half)

t2 =threading.Thread(target=second_half)

t3 =threading.Thread(target=third_half)

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()

print("program close")

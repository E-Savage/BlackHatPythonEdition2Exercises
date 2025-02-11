import argparse 
import socket 
import shlex
import subprocess
import sys
import textwrap
import threading 



def execute(cmd):
    ''' 
        this is to check the command and execute it
    '''
    cmd = cmd.strip()
    if not cmd:
        return
    output = subprocess.chek_output(shlex.split(cmd), stderr=subprocess.STDOUT)
    return output.decode()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="BHP Net Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''Example:
            netcat.py -t 192.168.1 -p 5555 -l -c # command shell
            netcat.py -t 192.168.1 -p 5555 -l -u=mytest.txt # upload to file
            netcat.py -t 192.168.1 -p 5555 -l -d # download file
            echo 'ABC' | ./netcat.py -t 192.168.1 -p 135
            netcat.py -t 192.168.1 -p 5555 # connect to server'''))
    
    parser.add_argument("-c", "--command", action="store_true", help="command shell")
    parser.add_argument("-e", "--execute", help="execute specified command")
    parser.add_argument("-l", "--listen", action="store_true", help="listen")
    parser.add_argument("-p", "--port", type=int, default=5555, help="specified port")
    parser.add_argument("-t", "--target", default='192.168.1.203', help="specified IPs")
    parser.add_argument("-u", "--upload", help="upload file")

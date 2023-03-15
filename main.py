# Abi
# Automation project
# Ping

from Server import Server

def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Abi Diop")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    server_ip = "3.15.21.27"
    rsa_key = r"C:\Users\AbyDiop\Downloads\abi_keypair.ppk"
    username = 'ubuntu'
    # run upgrade and update command
    upgrade = 'sudo apt update && sudo apt upgrade -y'
    my_serv = Server(server_ip, rsa_key, username, upgrade)
    # TODO - Call Ping method and print the results
    print(my_serv.ping())
    print("Updating server...")
    ssh_result = my_serv.upgrade
    print(ssh_result)

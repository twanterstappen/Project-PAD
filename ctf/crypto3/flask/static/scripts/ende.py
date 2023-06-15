# Import necessary modules
import sys       # for system-specific parameters and functions
import base64    # for base64 encoding and decoding
from cryptography.fernet import Fernet   # for encryption and decryption

# Set usage and help messages for the script
usage_msg = "Usage: " + sys.argv[0] + " (-e/-d) [file]"
help_msg = usage_msg + "\n" +\
        "Examples:\n" +\
        "  To decrypt a file named 'pole.txt', do: " +\
        "'$ python " + sys.argv[0] + " -d pole.txt'\n"

# Check that the script was run with the correct number of arguments
if len(sys.argv) < 2 or len(sys.argv) > 4:
    print(usage_msg)
    sys.exit(1)

# If the first argument is "-e", encrypt the file
if sys.argv[1] == "-e":
    # If the password is not provided as an argument, prompt the user for it
    if len(sys.argv) < 4:
        sim_sala_bim = input("Private_key:")
    # Otherwise, use the password provided as an argument
    else:
        sim_sala_bim = sys.argv[3]

    # Encode the password in base64 format
    ssb_b64 = base64.b64encode(sim_sala_bim.encode())
    # Create a Fernet cipher using the encoded password
    c = Fernet(ssb_b64)

    # Open the file to be encrypted and encrypt its contents
    with open(sys.argv[2], "rb") as f:
        data = f.read()
        data_c = c.encrypt(data)
        sys.stdout.write(data_c.decode())

# If the first argument is "-d", decrypt the file
elif sys.argv[1] == "-d":
    # If the password is not provided as an argument, prompt the user for it
    if len(sys.argv) < 4:
        sim_sala_bim = input("Private_key:")
    # Otherwise, use the password provided as an argument
    else:
        sim_sala_bim = sys.argv[3]

    # Encode the password in base64 format
    ssb_b64 = base64.b64encode(sim_sala_bim.encode())
    # Create a Fernet cipher using the encoded password
    c = Fernet(ssb_b64)

    # Open the file to be decrypted and decrypt its contents
    with open(sys.argv[2], "r") as f:
        data = f.read()
        data_c = c.decrypt(data.encode())
        sys.stdout.buffer.write(data_c)

# If the first argument is "-h" or "--help", print the help message
elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
    print(help_msg)
    sys.exit(1)

# If the first argument is not recognized, print an error message and exit
else:
    print("Unrecognized first argument: "+ sys.argv[1])
    print("Please use '-e', '-d', or '-h'.")
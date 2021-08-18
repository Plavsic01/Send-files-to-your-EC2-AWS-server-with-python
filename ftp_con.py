import pysftp,time,os

HOST = "ec2-18-184-169-150.eu-central-1.compute.amazonaws.com"
USERNAME = "ubuntu"
PATH = input("Enter path of your private key...\n")

# chmod 400 my_private_key.pem -> run command to ensure that key is private

server = pysftp.Connection(host=HOST,username=USERNAME,private_key=PATH)

def send_file(path,filename):
    try:
        server.chdir(path)
        server.put(filename)   
        print("successful transfer...")
    except:
        print("error accurred")

def send_files(path,list_filenames):
    try:
        server.chdir(path)
        for file in list_filenames:
            server.put(file)
            print("successful transfer...")

    except:
        print("error occurred")

def receive_file(filename_path,local_path):
    try:
        os.chdir(local_path)
        server.get(filename_path)
        print("successful transfer...")
    except:
        print("error accurred")

def main():
    while True:
        print("Choose options:")
        print("1 -> sending file to server...")
        print("2 -> receiving file from server...")
        print("3 -> Exit...")
        usr_input = int(input())

        if(usr_input == 1):
            print("If you want to send 1 file press 1, if you want more then 1 files to send press 2...")
            how_many_files = int(input())
            if(how_many_files == 1):
                print("Enter path where you want to store file on server...")
                send_file_path = input()
                print("Enter filename ('filename.txt') path:")
                send_file_filename = input()
                time.sleep(0.5)
                send_file(send_file_path,send_file_filename)
            elif(how_many_files == 2):
                print("Enter path where you want to store files on server...")
                send_file_path = input()
                print("Enter filenames ('filename.txt') paths separated with ',':")
                send_file_filenames = input().split(",")
                time.sleep(0.5)
                send_files(send_file_path,send_file_filenames)

        elif(usr_input == 2):
            print("Enter path from the server file:")
            receive_file_path = input()
            print("Enter local path file where you want your server file to come:")
            receive_local_path = input()
            time.sleep(0.5)
            receive_file(receive_file_path,receive_local_path)

        elif(usr_input == 3):
            server.close()
            break

if __name__ == "__main__":
    main()


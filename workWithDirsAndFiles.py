import sys
import os


#chek os 
check_os = sys.platform
print('Platform is :',check_os)

#create a folders if os is linux
if check_os == 'linux':
    
    check_dir = os.listdir('/home/')
    print('User name is : ' + str(check_dir))
    
    
    path_to_home_user = os.path.abspath('/home/' + check_dir[0] )
    print('full path to home user folder : ' + str(path_to_home_user))
    
    #create dir if it does't exist
    try:
        if not os.path.exists('AntiSlacker'):
            create_dir = os.mkdir(path_to_home_user + '/AntiSlacker')
            print('Dir was created successfuly')
    except(FileExistsError):
        print('Folder already exist')   
    
    #go to /AntiSlacker dir and create logs folder
    cd = os.chdir(path_to_home_user + '/AntiSlacker')
    print('You are in ' + path_to_home_user + '/AntiSlacker')
    
    try:
        if not os.path.exists('AntiSlacker/logs'):
            create_dir = os.mkdir(path_to_home_user  + '/AntiSlacker/logs')
            print('Dir was created successfuly')
    except(FileExistsError):
        print('Folder already exist')
elif check_os == 'win32':
    goTo_C_dir = os.chdir('C:/Program Files')  
    check_dir = os.listdir('C:/Program Files')
    print('You are in : C:/Program Files')

    #create dir if it does't exist
    try:
        if not os.path.exists('AntiSlacker'):
            create_dir = os.mkdir('C:/Program Files/AntiSlacker')
            print('Dir was created successfuly')
    except(FileExistsError):
        print('Folder already exist')   
    
    #go to /AntiSlacker dir and create logs folder
    cd = os.chdir('C:/Program Files/AntiSlacker')
    print('You are in C:/Program Files/AntiSlacker')
    
    try:
        if not os.path.exists('AntiSlacker/logs'):
            create_dir = os.mkdir('C:/Program Files/AntiSlacker/logs')
            print('Dir was created successfuly')
    except(FileExistsError):
        print('Folder already exist')        


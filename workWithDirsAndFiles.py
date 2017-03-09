import sys
import os


check_os = sys.platform

print('Platform is :',check_os)

if check_os == 'linux':
    check_dir = os.listdir('/home/')
    print(check_dir)
    path_to_home_user = os.path.abspath('/home/' + check_dir[0] + '/')
    #check_user_dir = os.listdir('/home/' + check_dir[0])

    #print(check_user_dir)
    print(path_to_home_user)
    
#     if not os.path.exists('AntiSlacker'):
#         create_dir = os.mkdir(path_to_home_user  + 'AntiSlacker')
#         print('Dir was created successfuly')
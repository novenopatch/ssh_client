import getpass
from fabric import  Connection,Config,task

server_address = "82.163.176.124" #input("Enter server address")
password = 'rRkYGS54Xg5y9Qq' #getpass.getpass("Enter your root password: ")
user = 'sanamgro' # input("Enter your username")
port = 1394
#config = Config(overrides={'sudo':{'password':password}})

        
        
    
php = 'php'
composer = 'composer'
symfony_console =  'symfony console'
www = 'cd www'
run = 'run'
end = 'end'
message_start = "Enter Command :"
message_rest ="Enter the rest or " + run +' :'
alias = {
    php : "/opt/alt/php80/usr/bin/php" ,
    composer :   " /home/sanamgro/composer.phar",   
    symfony_console :"/home/sanamgro/www/bin/console" ,
    www : "www"
}
def return_command(run:str,alias:dict)->str:
    command =""
    if run in [i for i in alias]:
        return run.replace(run,alias[run])
    elif run!=command:
        return run
    else: return command
        
    
def deploy():
    with Connection(
        server_address,
        user =user,
        port=port,
        connect_kwargs={"password":password},
    ) as c:
        with  c.cd(alias[www]):
        
            command = ""
            while True:
                if command=="":
                    message = message_start
                else: message = message_rest
                new = return_command(input(message) ,alias)
                
                if new =="":
                    break
                else: 
                    command = f"{command} {new}" 
                    print(f"Your command:- {command} -")  
            #print(f"Your command:- {command} -")     
            resut =c.run(command)
            
                
                
            
           
            
deploy()

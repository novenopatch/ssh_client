import getpass
from fabric import  Connection,Config,task
from save import Save
from Enumeration import SaveData
save = Save()
server_address = save.get_data(SaveData.SERVER_ADDRESS) 
password = save.get_data(SaveData.PASSWORD)
user = save.get_data(SaveData.USER)
port = save.get_data(SaveData.PORT)
#config = Config(overrides={'sudo':{'password':password}})

php = 'php'
composer = 'composer'
symfony_console =  'symfony console'
www = 'cd www'
run = 'run'
end = 'end'
message_start = "Enter Command :"
message_rest ="Enter the rest or " + "Enter to end" +' :'
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
        
    
def launch():
    with Connection(
        server_address,
        user =user,
        port=port,
        connect_kwargs={"password":password},
    ) as c:
        print(c)
        with  c.cd(alias[www]):
        
            command = ""
            while True:
                if command=="":
                    message = message_start
                else: message = message_rest
                new = return_command(input(message) ,alias)
                
                if new =="":
                    break
                elif new =="cls":
                    command = ""
                else: 
                    command = f"{command} {new}" 
                    print(f"Your command:- {command} -")  
            #print(f"Your command:- {command} -")   
            try:  
                resut =c.run(command)
                print(resut)
            except Exception as e:
                print(e)
            
launch()
save.save_data()

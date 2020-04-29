import os
import glob
import shutil
from datetime import datetime

os.chdir( os.path.dirname(os.path.abspath(__file__)) )
data_hora = datetime.now()

text_file_name = "Restore_organizer-" +  str(data_hora.year) + "-" + str(data_hora.month) + "-" + str(data_hora.day) + "-" + str(data_hora.hour) + "-" + str(data_hora.minute) + "-" + str(data_hora.second) + "-" +".sh"

path_remove_folders = ""
lista_anos = []

try:

        for _file in  glob.glob ('*', recursive=False):

                filename, file_extension = os.path.splitext(_file)

                if str(_file) not in 'organizer.py' and str(_file.split("-")[0]) not in 'Restore_organizer' and str(file_extension) != "":

                        if str( path_remove_folders ) == "":
                                text_file = open(text_file_name, "w")
                                text_file.write("#!/bin/bash \n")

                        created = os.stat(_file).st_mtime
                        getdate = (datetime.fromtimestamp(created))
                        mon = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
                        path =  str (getdate.year) + "/" + str (getdate.day ) +"_"+ str (mon[getdate.month]) + "/" + str( file_extension.replace(".","") )
                        os.makedirs( path, exist_ok=True ) 
                        shutil.move (_file, path)
  
                        text_file.write('mv "' + os.getcwd()  + '/' + path + '/' + _file + '" "' + os.getcwd() + '/' + _file + '" && \n' )
                        
                        if str(getdate.year) not in lista_anos:
                                lista_anos.append( str (getdate.year) )
                                path_remove_folders = path_remove_folders + 'rm -R "' + os.getcwd()  + '/' +  str (getdate.year)  + '/" && \n'
                 
except:
        text_file.close()

if str( path_remove_folders ) != "":
        path_remove_folders = path_remove_folders + 'rm -R "' + os.getcwd() + '/' + text_file_name + '" \n' 
        text_file.write(path_remove_folders)
        text_file.close()
        os.system(' chmod +x ' + text_file_name)
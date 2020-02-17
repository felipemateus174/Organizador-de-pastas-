import os
import glob
import shutil
from datetime import datetime
for folders in glob.glob ('*.txt'):
        created = os.stat(folders).st_mtime
        getdate = (datetime.fromtimestamp(created))
        mon = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
        path =  str (getdate.year) + "/" + str (getdate.day ) +"_"+ str (mon[getdate.month])
        print ( path )
        os.makedirs( path )
        shutil.move (folders, path)
        

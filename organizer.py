import os
import glob
import shutil
from datetime import datetime
for folders in glob.glob ('*.pdf'):
        created = os.stat(folders).st_mtime
        getdate = (datetime.fromtimestamp(created))
        mon = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
        path =  str (getdate.year) + "/" + str (getdate.day ) +"_"+ str (mon[getdate.month]) + "/" + str (folders[path.glob])
        print ( path )
        os.makedirs( path, exist_ok=True )
        shutil.move (folders, path)
        
from subprocess import Popen, PIPE
import Directorio,os,sys
 
def cmd_exec(str_cmd,flag_print):
  proc = Popen(str_cmd , shell=True, stdout=PIPE, stderr=PIPE)
  out, err = proc.communicate()
  if flag_print:
      print(out)
  if err != '':
      print(err)
  print("return code -> "+str(proc.returncode))
##  txt_resp =""
##  if proc.returncode == 0:
##    if flag_print:
##      for resp in out.rstrip():
##        print(resp)
##        if resp != 13 and resp != 10:
##          txt_resp += chr(resp)
##        else:
##          if resp == 10:
##            print(txt_resp)
##            txt_resp =""
##  else:
##    print (err.rstrip())
  return proc.returncode
 
if __name__ == "__main__":
    path_python = os.path.split(sys.executable)
    path = path_python[0]+'\Scripts' ## aponta para a pasta \Scripts do python para executar comandos pip
    Directorio.change_dir(path)
    print(Directorio.act_dir())
## 
####    if cmd_exec("pip show pillow",False) == 1: ## não existe o módulo instalado
####        cmd = "pip install --no-cache-dir pillow"
####        print("Comando -> "+str(cmd))
####        cmd_exec(cmd,True)
#### 
####    if cmd_exec("pip show pytesseract",False) == 1:  ## não existe o módulo instalado
####        cmd = "pip install --no-cache-dir pytesseract"
####        print("Comando -> "+str(cmd))
####        cmd_exec(cmd,True)
#### 
####    if cmd_exec("pip show opencv-python",False) == 1:  ## não existe o módulo instalado
####        cmd = "pip install --no-cache-dir opencv-python"
####        print("Comando -> "+str(cmd))
####        cmd_exec(cmd,True)
####
####
##    if cmd_exec("pip show tesserocr",False) == 1:  ## não existe o módulo instalado
##        cmd = "pip install --no-cache-dir tesserocr"
##        print("Comando -> "+str(cmd))
##        cmd_exec(cmd,True)


    cmd = "pip install https://pypi.python.org/packages/92/7e/b308cc3d94065a7491582d50343920f10ad441cab5f79ef9602f022d479f/Appium-Python-Client-0.26.tar.gz#md5=4ab2c2763ba524f29671920c8562e99d"
    print("Comando -> "+str(cmd))
    if cmd_exec(cmd,True) == 0:
      cmd = "pip install -r requirements.txt"
      print("Comando -> "+str(cmd))
      cmd_exec(cmd,True)
      cmd_exec("pip list",True)

##    
##    cmd_exec("pip list",True)

##    Directorio.change_dir('C:\Applics\Python\Lib\site-packages\pytesseract')
##    print(Directorio.act_dir())
##    cmd_exec("pytesseract.py -l fra test-european.jpg",True)
    

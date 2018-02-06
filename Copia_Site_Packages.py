import sys,os,re
 
 
if __name__ == "__main__":
    path_site_packages = None
    
    for path in sys.path:
     if re.search("site-packages" , path):
       path_site_packages = path
       break
      
    if path_site_packages:
      src = "C:\Users\i051284\Python_meu\utilitarios\Utilitarios.py"
      dest = path_site_packages+"\Utilitarios.py"
      cmd_copy = "copy "+src+" "+dest
      x = os.popen(cmd_copy)
      print(str(x))


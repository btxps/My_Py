import Utilitarios,Directorio

if __name__ == "__main__":

  while True:
    rc = 0
    rep_loc = str(Utilitarios.get_input("Indicar caminho para repositorio Local : "))
    rep_rem = ""
    out_scan=[]
    project = ""
    
    if rc == 0:
      Directorio.change_dir(rep_loc)
      print("-------------------------------------------")
    if rc == 0:
      rep_rem = str(Utilitarios.get_input("Indicar caminho para repositorio Remoto : "))
      cmd = "git clone "+rep_rem
      print("\nComando >> "+cmd+'\n')
      rc = Utilitarios.cmd_exec(cmd, True)
      print("-------------------------------------------")
    if rc == 0:
      out = Directorio.scan_dir(rep_loc)
      if out[0]:
        out_scan = out[1]
      print("-------------------------------------------")
    if rc == 0:
      project = str(Utilitarios.get_input("Nome Projecto : "))
      for memb in out_scan:
        if memb[0] == "F":
          cmd = "copy "+str(memb[1])+" "+rep_loc+"\\"+project
          print("\nComando >> "+cmd+'\n')
          rc = Utilitarios.cmd_exec(cmd, True)
          if rc != 0:
            break
        print("-------------------------------------------")
    if rc == 0:
      cmd = "cd "+rep_loc+"\\"+project
      Directorio.change_dir(rep_loc+"\\"+project)
      print("\nComando >> "+cmd+'\n')
      rc = Utilitarios.cmd_exec(cmd, True)
      print("-------------------------------------------")
    if rc == 0:
      cmd = "git add -A"
      print("\nComando >> "+cmd+'\n')
      rc = Utilitarios.cmd_exec(cmd, True)
      print("-------------------------------------------")      
    if rc == 0:
      msg = str(Utilitarios.get_input("Mensagem para commit : "))
      cmd = "git commit -m "+'"'+msg+'"'
      print("\nComando >> "+cmd+'\n')
      rc = Utilitarios.cmd_exec(cmd, True)
      print("-------------------------------------------")
    if rc == 0:
      cmd = "git push"
      print("\nComando >> "+cmd+'\n')
      rc = Utilitarios.cmd_exec(cmd, False)
      print("-------------------------------------------")
    if rc == 0:
      cmd = "cd "+rep_loc
      Directorio.change_dir(rep_loc)
      print("\nComando >> "+cmd+'\n')
      print("-------------------------------------------")
    if rc == 0:
      cmd = "rmdir /s /q "+rep_loc+"\\"+project
      print("\nComando >> "+cmd+'\n')
      rc = Utilitarios.cmd_exec(cmd, True)
      print("-------------------------------------------")

    if str(Utilitarios.get_input("Pretende Sair (S/N)")).upper() == "S":
      break

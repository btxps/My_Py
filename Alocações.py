import calendar, Utilitarios,datetime,sys,os,math,codecs,Directorio

percent_aloc = []
sum_p_aloc = 0
acerto = 0
t_h_p = 0
feriados=[]
local_dir = ""

##
##da_fim = Utilitarios.get_input("Indicar data Fim : ")
##
##print("Data Inicio - "+str(dt_ini) + " | Data Fim - "+str(da_fim))

def date(datestr="", format="%d-%m-%Y"):
    if not datestr:
        return datetime.datetime.today().date()
    return datetime.datetime.strptime(datestr, format).date()

def verifica_se_dia_util(data):
    return (data.weekday() < 5)

def carrega_feriados():
    fr = codecs.open("Feriados.txt", 'r', encoding='utf-8')
    for linha in fr:
        words = linha.split(';')
        feriados.append([date(words[0]),words[1]])
    fr.close()

def is_feriado(feriado_srt):
    for fer in feriados:
        if (fer[0] == feriado_srt):
            return True
    return False

def init_vars():
    global percent_aloc,sum_p_aloc,acerto,p_aloc,t_h_p
    percent_aloc = []
    sum_p_aloc = 0
    acerto = 0
    p_aloc = 0
    t_h_p = 0

def instala_modulos():
    if Utilitarios.cmd_exec("pip show colorama",False) == 1:
        print("Instalacao do colorama em curso ...")
        cmd = "pip install --no-cache-dir colorama"
        Utilitarios.cmd_exec(cmd,True)
        
    if Utilitarios.cmd_exec("pip show termcolor",False) == 1:
        print("Instalacao do termcolor em curso ...")
        cmd = "pip install --no-cache-dir termcolor"
        Utilitarios.cmd_exec(cmd,True)
    



if __name__ == "__main__":
    local_dir = Directorio.act_dir()
    ## Instala dependencias (módulos importados) 
    instala_modulos()
    ############################################
    Directorio.change_dir(local_dir)

    import colorama
    from termcolor import *

    colorama.init()
    carrega_feriados()
        
    while True:
        init_vars()
        os.system('cls')
        while True:
            dt_ini = date(Utilitarios.get_input("Data Inicio (dd-mm-yyyy) : "))
            dt_aux = dt_ini
            print(dt_aux)
            dt_fim = date(Utilitarios.get_input("Data Fim (dd-mm-yyyy)    : "))
            if dt_fim < dt_ini:
                text = colored("\nData de Fim deve ser igual ou superior Data Inicio ...\n","red","on_white")
                print(text)
            else:
                break

        ausencias = int(Utilitarios.get_input("Ausencias (Num. Dias) : "))
        
        input_ok = True
        while input_ok:
            os.system('cls')
            input_ok = False
            print colored("\nIndicar percentagens de Alocacao separadas por ","white"),colored(";","red")
            str_p_aloc=Utilitarios.get_input("Percentagem ( deve ser superior a zeros ) - ")
            percent_aloc = str_p_aloc.split(';')

            for per in percent_aloc:
                if not per.isdigit() or per == '0':
                    input_ok = True
                    break
        #############################################################################################################    
            
        os.system('cls')
        
        num_dias = 0
        num_dias_util = 0
        horas_dias_uteis = 0
    
        while dt_aux <= dt_fim:
            if verifica_se_dia_util(dt_aux) and not is_feriado(dt_aux):
                num_dias_util += 1
            num_dias += 1
            dt_aux = dt_aux + datetime.timedelta(days=1)
                
        num_dias_util -= ausencias
        horas_dias_uteis = num_dias_util * 8
        
        
        print colored("Data Inicio   > ","white"), \
              colored(str(dt_ini),"yellow"), \
              colored("\nData Fim      > ","white"), \
              colored(str(dt_fim),"yellow"), \
              colored("\nAusencia Dias > ","white"), \
              colored(str(ausencias),"yellow"), \
              colored("\nDias          > ","white"), \
              colored(str(num_dias),"yellow"), \
              colored("\nDias Uteis    > ","white"), \
              colored(str(num_dias_util),"yellow"), \
              colored("\nHoras         > ","white"), \
              colored(str(horas_dias_uteis),"yellow"), \
              colored('\n',"white")

        x_aux = 0
        for p in percent_aloc:
            x = math.modf(horas_dias_uteis * (Utilitarios.division(p,100)))
            h_p = x[1]
            t_h_p += h_p
            if t_h_p < horas_dias_uteis:
                h_p += x_aux
                t_h_p += x_aux
            else:
                h_p -= (t_h_p - horas_dias_uteis)
            
            if x[0] > 0:
                x_aux = 1
            else:
                x_aux = 0

            y = math.modf(h_p/8)
            d_oito = h_p - (int(y[1])*8)     
            print colored(" >> "+ str(p).rjust(3,' ') + "% = ","white"), \
                  colored(str(h_p).rjust(5,' '),"yellow"), \
                  colored(" horas ( ","white"), \
                  colored(str(y[1]).rjust(4,' '),"yellow"), \
                  colored(" dias e ","white"), \
                  colored(str(d_oito),"yellow"), \
                  colored(" horas )","white")

        print colored("\n\n By: thosakpy@gmail.com","white")
            
        if Utilitarios.get_input("\nSair (N,S) - ").upper() == 'S':
            break
    

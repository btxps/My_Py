import Utilitarios,os

def help_modulo(modulo):
    cmd_import = "import " + modulo
    cmd_help  = "help(" + modulo + ")"
    exec cmd_import
    exec cmd_help

if __name__ == "__main__":
    while True:
        os.system('cls')
        
        modulo_name = Utilitarios.get_input("Indicar Nome Modulo : ")
        help_modulo(modulo_name)
        
        if Utilitarios.get_input("\nSair (N,S) - ").upper() == 'S':
            break

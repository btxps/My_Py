#!/usr/bin/python
# -*- coding: latin-1 -*-

"""Módulo com funções genéricas:
      > Obter dados do Standard Input;
      > Executar comandos PIP;
      > Divisão matemática
"""

import platform, getpass, Directorio, os, sys
from subprocess import Popen, PIPE

def get_input(txt_input):
    """ Função que obtem dados do Standard Input de forma visivel.
        Valida a versão do Python 
    """
    if platform.python_version()[:3] > '3.1':
        return str(input(txt_input))
    else:
        return str(raw_input(txt_input))

def get_input_pass(txt_input):
    """ Função que obtem dados do Standard Input de forma invisivel.
        Usar no caso de Password's , etc 
    """
    
    return getpass.getpass(txt_input)

def division(numerador,denominador):
    """ Efectual calculo da Divisão em função da Versão do Python.
        Recebe 2 parametros:
           > numerador;
           > denominador
    """
    
    if platform.python_version()[:1] >= '3':
        return numerador/denominador
    else:
        return float(numerador)/float(denominador)

def cmd_exec(str_cmd,flag_print):
    
    """ Executa comandos PIP. Recebe 2 parametros:
           > str_cmd    - Comando a ser executado;
           > flag_print - Flag que controla impressão do resultado da execução do comando
    """
    
    path_python = os.path.split(sys.executable)
    path = path_python[0]+'\Scripts' ## aponta para a pasta \Scripts do python para executar comandos pip
    Directorio.change_dir(path)
    
    proc = Popen(str_cmd , shell=True, stdout=PIPE, stderr=PIPE)
    out, err = proc.communicate()
    if flag_print:
        print(out)
    if err != '':
        print(err)
    return proc.returncode

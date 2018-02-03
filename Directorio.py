#!/usr/bin/python
# -*- coding: latin-1 -*-

"""Módulo com funções para manipular Directorios e arquivos:
      > Permite gerir Directorios(Criação, Eliminação, etc);
      > Consulta existencia de Arquivo;
      > Remove Arquivo
"""

import os,sys


def change_dir(path):
  """ Altera directorio
  """
  change_dir_o = True
  try:
    os.chdir(path) 
  except: # catch *all* exceptions
    print(sys.exc_info()[0] ," - ",sys.exc_info()[1])
    change_dir_o = False 
  return change_dir_o


def cria_dir(path):
  """ Cria directorio
  """
  cria_dir_o = True
  try:
    os.mkdir(path) 
  except: # catch *all* exceptions
    print(sys.exc_info()[0] ," - ",sys.exc_info()[1])
    cria_dir_o = False 
  return cria_dir_o


def remove_dir(path):
  """ Remove directorio
  """
  remove_dir_o = True
  try:
    os.rmdir(path) 
  except: # catch *all* exceptions
    print(sys.exc_info()[0] ," - ",sys.exc_info()[1])
    remove_dir_o = False
  return remove_dir_o


def cria_arvore_dir(path):
  """ Cria arvore de directorios
  """ 
  cria_arvore_dir_o = True
  try:
    os.makedirs(path,True) 
  except: # catch *all* exceptions
    print(sys.exc_info()[0] ," - ",sys.exc_info()[1])
    cria_arvore_dir_o = False
  return cria_arvore_dir_o


def remove_arvore_dir(path):
  """ Remove arvore de directorios
  """
  remove_arvore_dir_o = True
  try:
    os.removedirs(path) 
  except: # catch *all* exceptions
    print(sys.exc_info()[0] ," - ",sys.exc_info()[1])
    remove_arvore_dir_o = False
  return remove_arvore_dir_o


def remove_file(path):
  """ Remove ficheiro
  """
  remove_file_o = True
  try:
    os.remove(path) 
  except: # catch *all* exceptions
    print(sys.exc_info()[0] ," - ",sys.exc_info()[1])
    remove_file_o = False
  return remove_file_o


def act_dir():
  """ Retorna directorio actual
  """
  return os.getcwd()


def file_exists(file_path):
  """ Retorna True ou False caso exista ou nao o ficheiro
  """
  return os.path.exists(file_path)


def scan_dir(path):
  list_dir=[]
  scan_dir_o = False
  if change_dir(path):
    scan_dir_o = True
    try:
      with os.scandir(path) as it:
        for entry in it:
          str_scan=""
          if entry.is_dir():
            list_dir.append(["D",entry.name])
            str_scan +=" Type - D"
          if entry.is_file():
            list_dir.append(["F",entry.name])
            str_scan +=" Type - F"
          str_scan += " | Name - "+entry.name
          print(str_scan)
    except: # catch *all* exceptions
      print(sys.exc_info()[0] ," - ",sys.exc_info()[1])
      scan_dir_o = False 
  return scan_dir_o,list_dir

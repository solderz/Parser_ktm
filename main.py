# Version 1
import sys
import re
import datetime
k=' '
file=''
file_n=''
file_t=''
k1=''
list_proverok=[]
my_list=(' '.join(sys.argv))
if "-f" in my_list: # proveryaem  est li parametr -f
  str=my_list[my_list.find("-f")+3:] 
  if str.find(" ")==-1: # proveryaem  posledni li pararmetr -f
    file=str
  else:
    file=str[:str.find(" ")] 
if "-t" in my_list: # proveryaem  est li parametr -t
  str=my_list[my_list.find("-t")+3:] 
  if str.find(" ")==-1: # proveryaem  posledni li pararmetr -t
    file_t=str
  else:
    file_t=str[:str.find(" ")]    
if "-n" in my_list: # proveryaem  est li parametr -n
  str=my_list[my_list.find("-n")+3:] 
  if str.find(" ")==-1: # proveryaem  posledni li pararmetr -n
    file_n=str
  else:
    file_n=str[:str.find(" ")]
if "-h" in my_list: # proveryaem  est li parametr -h
  print ("-h:-HELP; -f:-input_file; -n:-hash_extract; -f:-input_template;" )
  file=''
  file_n=''
  file_t=''   
if file!='':
  with open(file, 'r') as fh: # OTKROEM FAIL s IP  PEREBER POSTROCHNO 
    for line in fh:
      result=re.findall(r'\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}',line)
      if (len(result))!=0:
        if k!=result:
          k=result
          k1=''.join(k)+'\n'
      else:
        k1=''     
      if file_t!='':
        with open(file_t, 'r') as ft: # OTKROEM FAIL s shablonami  PEREBER POSTROCHNO 
          for line_t in ft:
            line_t=re.sub('[\t\r\n]', '', line_t)
            line_=re.sub('[\t\r\n]', '', line)
            regex=r"^"+line_t+r""
            if (len(re.findall( regex,line)))!=0:
              k=''.join(k)
              lin=re.sub(r'[^\w_. -]', '_', line_t)
              current_dat=datetime.datetime.now()
              file_w=open(lin+'_'+current_dat.strftime('%d:%m:%Y-%H:%M:%S'),"a")
              file_w.write(k+'\n')
              file_w.close()
      else:
        current_dat=datetime.datetime.now()
        file_w=open('ALL_'+current_dat.strftime('%d:%m:%Y-%H:%M:%S'),"a")
        file_w.write(k1)
        file_w.close()
if file_n!='':
  current_dat=datetime.datetime.now()
  file_wl=open('logins_'+current_dat.strftime('%d:%m:%Y-%H:%M:%S'),"a")
  file_wh=open('hash_'+current_dat.strftime('%d:%m:%Y-%H:%M:%S'),"a")
  
  with open(file_n, 'r') as fn: # OTKROEM FAIL s HASH  PEREBER POSTROCHNO 
    for line_n in fn:
      result=re.findall(r'^.+[:].+[:].+[:].{30,33}[:]',line_n)
      if (len(result))!=0:
        result=''.join(result)
        has=''.join(re.findall(r'[:].{31,32}[:].{31,32}[:]',result))
        has=has[34:]
        has=has.replace(':', '')
        log=result[:result.find(":")]
        if log not in list_proverok:
          file_wl.write(log+'\n')
          list_proverok.append(log)
        if has not in list_proverok:
          file_wh.write(has+'\n')
          list_proverok.append(has)
  file_wl.close()
  file_wh.close()        
        
        





               

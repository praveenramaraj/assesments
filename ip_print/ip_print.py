#!/usr/bin/python3

#
#  Main Comments
#
#


import sys
import argparse
import pathlib
import json



class ip_print:

  def read_file(self,filename):
    try:
      with open(filename, 'rb') as _:
        return json.load(_)
    except FileNotFoundError as e:
      print('This file doesn\'t exist')
      sys.exit(1)
    except:
      print("JSON not loaded")
      sys.exit(1)

  def get_access_ip(self,hostname,dict_):
    if 'network' in dict_:
      try:
        for j in dict_['network']['vms']:
          if hostname in j['attributes'].values():
            return j['attributes']['access_ip_v4']
      except:
        print("Failed finding matching access ip")
        sys.exit(1)
    else:
     return ""


  def parse_json(self,dict_):
    
    for hostname in dict_['vm_private_ips']['value']:
      private_ip = dict_['vm_private_ips']['value'][hostname]
      access_ip  = self.get_access_ip(hostname,dict_)
      print("%s %s" %(private_ip, access_ip))
      


def main():
  
  try:
    
    description = "IP parser"
    parser =  argparse.ArgumentParser(description=description)
    parser.add_argument("--json")
    

    if len(sys.argv) == 1:
      parser.print_help(sys.stderr)
      sys.exit(1)


    args = parser.parse_args()

    ip_  = ip_print()
    file_ = pathlib.Path(__file__).parent / args.json
    json_dict = ip_.read_file(file_)

 
    ip_.parse_json(json_dict)

  except KeyboardInterrupt:
    print("Shutdown requested...exiting")

  sys.exit(0)


if __name__ == '__main__':
  main()

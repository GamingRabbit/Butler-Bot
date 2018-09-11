import discord
from discord.ext import commands
import sys
    
def mtt():
  try:
    d = open("m.txt")
  except:
    Print("error")
  l = d.readlines()
  d.close
        
  code = {}
  for m in l:
    w = m.split()
    code[w[0]] = w[1]
        
  for i in range(97,123):
    code[chr(i)] = code[chr(i - 32)]
      
  return code
    
    
    


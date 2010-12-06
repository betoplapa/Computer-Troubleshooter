'''
Created on Nov 20, 2010

@author: ramdac
'''

from pyke import knowledge_engine
from GUI import ask_wx

engine = knowledge_engine.engine(__file__)

def run():
    
    engine.ask_module = ask_wx
    engine.activate('off_state_rules')

def reset():
    engine.reset()
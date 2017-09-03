#!-*- coding:utf-8 -*-
import os
import subprocess

home_path = os.environ['HOME']
bashrc_path = "{0}/.bashrc".format(home_path)

#def bash_command(cmd):
#    subprocess.Popen(cmd, shell=True, executable='/bin/bash')

os.system("sudo apt-get update")
os.system("sudo apt-get install vim tmux git virtualenv python-pip libxml2-dev libxslt-dev ssh")
os.system("sudo pip install -U pip")
os.system('virtualenv {0}/pyenv'.format(home_path))

#bash_command('source {0}/pyenv/bin/activate'.format(home_path))
#bash_command('pip install flask lxml html5lib selenium pymongo beautifulsoup4 requests paho-mqtt line-bot-sdk')

os.system("git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim")
os.system('cp ./.vimrc ~/')
os.system('cp -rf ./colors ~/.vim/')

f = open(bashrc_path,'a') 
f.write("alias tmux='tmux -2u'\n") #加入tmux 的顏色設定 
f.write("alias pyenv='source {0}/pyenv/bin/activate'\n".format(home_path)) #加入virtualenv環境
f.close()
os.system('vim +PluginInstall +qall') #安裝vim套件 

#!/bin/bash
# Easily extract all compressed file types
#krishna 18/12/2015
if [ -f "$1" ] ; then
  case $1 in
     *.tar.bz2)   tar xvjf "$1" -C "$2"    ;;
     *.tar.gz)    tar xvzf "$1" -C "$2"    ;;
     *.bz2)       bunzip2 "$1" -C "$2"     ;;
     *.rar)       unrar x "$1" -C "$2"     ;;
     *.gz)        gunzip "$1" -C "$2"      ;;
     *.tar)       tar xvf "$1" -C "$2"     ;;
     *.tbz2)      tar xvjf "$1" -C "$2"    ;;
     *.tgz)       tar xvzf "$1" -C "$2"    ;;
     *.zip)       unzip "$1" -C "$2"       ;;
     *.Z)         uncompress "$1" -C "$2"  ;;
     *.7z)        7z x "$1" -C "$2"        ;;
     *)           echo "don't know how to extract '$1'..." ;;
  esac
  echo 'exit'
else
   echo "'$1' is not a valid file"
fi


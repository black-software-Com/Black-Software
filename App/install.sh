#!/bin/sh
# Black-Software v1.0

if [[ "$(id -u)" -ne 0 ]];
then
  echo "Please, Run This Program as Root!"
  exit
fi
function main() {
    printf '\033]2;Black-Software\a'
    clear
    echo "Installing..."
    chmod +x install.py
    sleep 2
    apt install python
    apt install python3
    apt install python3-pip
    echo "
Finish...
"
    python3 install.py
}
main
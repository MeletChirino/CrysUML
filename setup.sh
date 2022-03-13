#!/bin/bash
# Insrall python dependencies
python3 scripts/milk.py stimpy "Comenzando la\ninstalacion"
sleep 5
sudo apt install python3 python3-pip plantuml

# Install python dependecies
pip3 install -r requirements.txt

# copy aliases
CRYSUML_PATH=`pwd`
al="alias crys-render=\"python3 ${CRYSUML_PATH}/scripts/milk.py\""
echo $al >> ~/.bashrc

python3 scripts/milk.py milk "Instalacion\nCompleta"

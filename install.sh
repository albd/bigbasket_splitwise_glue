sudo apt-add-repository ppa:cdekter/ppa
sudo apt-get update
sudo apt-get install autokey-gtk python-tk python-lxml
sudo patch -N /usr/lib/python2.7/dist-packages/autokey/scripting.py autokey.patch
autokey &
cp glue.py .glue.json ~/.config/autokey/data/Sample\ Scripts

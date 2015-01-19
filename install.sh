sudo apt-get install autokey-gtk python-tk
sudo patch /usr/lib/python2.7/dist-packages/autokey/scripting.py autokey.patch
cp glue.py .glue.json '/home/albert/.config/autokey/data/Sample Scripts'

# First deployment

sudo apt install git

sudo git clone

cd shell

sudo chmod u+x deployment.sh

sudo pip install passlib
python -c "from passlib.hash import sha512_crypt; import getpass; print(sha512_crypt.using(rounds=5000).hash(getpass.getpass()))"

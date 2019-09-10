# Web3.py on Linux

## Developer Setup

1. Install all of the package dependencies

```sh
# Ubuntu
sudo update
sudo apt-get -y install libssl-dev libffi-dev autoconf automake libtool
```

## Install and configure Python

### Ubuntu 16.04

```sh
sudo apt-get update
sudo apt-get -y upgrade

sudo apt-get -y install build-essential
sudo apt-get -y install python3-dev
sudo apt-get -y install python3-venv


git clone https://github.com/Nicemanss/web3.py
cd web3.py
python3 -m venv venv
. venv/bin/activate
pip install --upgrade pip
pip install -e .[dev]

```

## Test
To test the installation, run the following command:

```sh
python3 example.py
```

It should output something similar to:
```
root@local:~# python3 example.py
Is connected to https://node.myhpbwallet.com ? True
Current Block Number: 3679511
Account: 0xb0617bf785b4ce32a00bdffc7e093ad82c2e0925
Balance: 8135.9512525
```

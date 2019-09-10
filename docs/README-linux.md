# Web3.py on Linux

## Developer Setup

1. Install all of the package dependencies

```sh
# Ubuntu
sudo update
sudo apt-get -y install libssl-dev libffi-dev autoconf automake libtool

# ArchLinux
sudo pacman -Sy libsecp256k1

# Fedora
sudo dnf install openssl-devel libffi-devel autoconf automake libtool
```

## Install and configure Python

### Ubuntu 16.04

```sh
sudo apt-get update
sudo apt-get -y upgrade

sudo apt-get -y install build-essential
sudo apt-get -y install python3-dev
sudo apt-get -y install python3-venv

cd ~
git clone https://github.com/ethereum/web3.py.git
cd web3.py
python3 -m venv venv
. venv/bin/activate
pip install --upgrade pip
pip install -e .[dev]

```


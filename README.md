# Web3.py

A Python implementation of [web3.js](https://github.com/ethereum/web3.js)

* Python 3.6+ support

Read more in the [documentation on ReadTheDocs](http://web3py.readthedocs.io/). [View the change log on Github](docs/releases.rst).

## Developer Setup

```sh
git clone git@github.com:Nicemanss/web3.py.git
cd web3.py
```

Please see OS-specific instructions for:

- [Linux](docs/README-linux.md#Developer-Setup)
- [Mac](docs/README-osx.md#Developer-Setup)
- [Windows](docs/README-windows.md#Developer-Setup)
- [FreeBSD](docs/README-freebsd.md#Developer-Setup)

Then run these install commands:

```sh
virtualenv venv
. venv/bin/activate
pip install -e .[dev]
```

To test the installation, you can run the following command inside this directory:

```python3 example.py
```

It should output something similar to:
```root@local:~# python3 example.py
Is connected to https://node.myhpbwallet.com ? True
Current Block Number: 3679511
Account: 0xb0617bf785b4ce32a00bdffc7e093ad82c2e0925
Balance: 8135.9512525
```

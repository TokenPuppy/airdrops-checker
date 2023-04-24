import re
import csv
import requests
from web3_auto.from_key import from_key
from web3_auto.from_mnemonic import from_mnemonic
from web3_auto.to_checksum_address import to_checksum_address
from const import airdrops
from const import hop, across, op1, arbitrum


def check_private_key(private_key):
    account = from_key(private_key=private_key)
    account_address = to_checksum_address(account=account)
    with open('addresses.txt', 'r') as addresses_file_r:
        if account_address in addresses_file_r.read():
            pass
        else:
            with open('addresses.txt', 'a') as addresses_file_w:
                addresses_file_w.writelines(f'{account_address}\n')


def check_mnemonic_phrase(mnemonic):
    account = from_mnemonic(mnemonic=mnemonic)
    account_address = to_checksum_address(account=account)
    with open('addresses.txt', 'r') as addresses_file_r:
        if account_address in addresses_file_r.read():
            pass
        else:
            with open('addresses.txt', 'a') as addresses_file_w:
                addresses_file_w.writelines(f'{account_address}\n')


def check_accounts():
    addresses = []
    for addr in re.findall(r'0x\w{40}', open('addresses.txt').read()):
        addresses.append(addr.lower())
    for airdrop, url in airdrops.items():
        print(airdrop)
        for address, amount, *_ in csv.reader(requests.get(url).text.splitlines()):
            if address in addresses:
                print(address, amount)

    print("Hop")
    for address, _, _, _, _, amount in csv.reader(requests.get(hop).text.splitlines()):
        if address in addresses:
            print(address, amount)

    print("Optimism #1")
    for address, _, _, _, _, _, _, _, _, amount in csv.reader(requests.get(op1).text.splitlines()):
        if address in addresses:
            print(address, amount)

    print("Across")
    data = requests.get(across).json()
    for key in list(data.keys()):
        if key.lower() in addresses:
            print(key, data[key]['total'])

    print("Arbitrum")
    data = requests.get(arbitrum).json()
    for key in list(data.keys()):
        if key.lower() in addresses:
            print(key, data[key])

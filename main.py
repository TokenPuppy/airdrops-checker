from utils.account import check_private_key, check_mnemonic_phrase, check_accounts
import time
from tqdm import tqdm

with open('private-keys.txt') as file:
    private_keys_file = [row.strip() for row in file]

with open('mnemonics.txt') as file:
    mnemonics_file = [row.strip() for row in file]


def check_private_keys():
    try:
        print('---')
        print(f'- loaded {len(private_keys_file)} private keys...')
        print('- checking private keys & generating account addresses...')
        for key in tqdm(private_keys_file, colour='GREEN'):
            check_private_key(key)
            time.sleep(0.0001)
        print('---')
        print('- checking account addresses for airdrops...')
        print('---')
        check_accounts()
        print('---')
    except Exception as e:
        print(e)
        pass


def check_mnemonic_phrases():
    try:
        print('---')
        print(f'- loaded {len(mnemonics_file)} mnemonic phrases...')
        print('- checking private keys & generating account addresses...')
        for mnemonic in tqdm(mnemonics_file, colour='GREEN'):
            check_mnemonic_phrase(mnemonic)
            time.sleep(0.0001)
        print('---')
        print('- checking account addresses for airdrops...')
        print('---')
        check_accounts()
        print('---')
    except Exception as e:
        print(e)
        pass


if __name__ == '__main__':
    print('---')
    user_action = int(input('- 1. check private keys for airdrops\n'
                            '- 2. check mnemonic phrases for airdrops\n'
                            '--- Chose method: '))
    print('')

    if user_action == 1:
        check_private_keys()
    elif user_action == 2:
        check_mnemonic_phrases()
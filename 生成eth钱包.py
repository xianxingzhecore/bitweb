import os 
from eth_account import Account
from tool import *

if __name__ == "__main__":
    wallet_list = []
    n = int(input("输入要创建钱包的数量："))
    for i in range(n):
        Account.enable_unaudited_hdwallet_features()
        ac, mnemonic = Account.create_with_mnemonic()

        line = "{}----{}----{}\n".format(ac.address,mnemonic,ac.key.hex())
        print(line)
        wallet_list.append(line)
    
    write_file(r'output/wallet.txt',wallet_list,'w')


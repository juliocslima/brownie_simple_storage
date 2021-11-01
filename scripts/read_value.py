from brownie import SimpleStorage, accounts, config


def read_contract():
    # -1 means work with the last version deployed
    simple_storage = SimpleStorage[-1]
    print(simple_storage.retrieve())


def main():
    read_contract()

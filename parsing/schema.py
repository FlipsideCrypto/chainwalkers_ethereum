from datetime import datetime
from parsing.utils.decimals import hex_to_decimal
from pprint import pprint

class BlockSchema(object):

    def __init__(self, data):
        self.hash = data['hash']
        self.number = data['number']
        self.blockHeight = data['number']
        self.blockTime = hex_to_decimal(data['timestamp'])
        self.difficulty = hex_to_decimal(data['difficulty'])
        self.author = data['author']
        self.extra_data = data['extraData']
        self.gas_limit = hex_to_decimal(data['gasLimit'])
        self.gas_used = hex_to_decimal(data['gasUsed'])
        self.logs_bloom = data['logsBloom']
        self.miner = data['miner']
        self.mix_hash = data['mixHash']
        self.parent_hash = data['parentHash']
        self.nonce = data['nonce']
        self.receipts_root = data['receiptsRoot']
        self.seal_fields = data['sealFields']
        self.sha3_uncles = data['sha3Uncles']
        self.size = hex_to_decimal(data['size'])
        self.state_root = data['stateRoot']
        self.timestamp = hex_to_decimal(data['timestamp'])
        self.total_difficulty = hex_to_decimal(data['totalDifficulty'])
        self.transactions_root = hex_to_decimal(data['transactionsRoot'])
        self.uncles = data['uncles']
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_transactions(self):
        return self.transactions

    def __repr__(self):
        header = "block height: %d, tx count %d" % (self.blockHeight, len(self.transactions))
        transactions = []
        for tx in self.transactions:
            transactions.append(str(tx))
        return "\n".join([header] + transactions)


class TransactionSchema(object):

    def __init__(self, data):
        self.block_hash = data['blockHash']
        self.block_number = hex_to_decimal(data['blockNumber'])
        self.chain_id = data['chainId']
        self.condition = data['condition']
        self.creates = data['creates']
        self.from_ = data['from']
        self.to = data['to']
        self.gas = hex_to_decimal(data['gas'])
        self.gas_price = hex_to_decimal(data['gasPrice'])
        self.hash = data['hash']
        self.input = data['input']
        self.nonce = data['nonce']
        self.public_key = data['publicKey']
        self.r = data['r']
        self.raw = data['raw']
        self.s = data['s']
        self.standard_v = data['standardV']
        self.transaction_index = hex_to_decimal(data['transactionIndex'])
        self.v = data['v']
        self.value = hex_to_decimal(data['value'])

    def __repr__(self):
        return "tx: {}".format(self.hash)

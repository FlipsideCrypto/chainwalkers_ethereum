import binascii
from parsing.utils.jsonrpc import JsonRpcCaller
from parsing.schema import BlockSchema, TransactionSchema
from datetime import datetime


class Node(object):

    def __init__(self, url, user=None, password=None):
        self.rpcCaller = JsonRpcCaller(url, user=user, password=password, tls=True)

    def __repr__(self):
        return self.rpcCaller.getAddress()

    def get_block_count(self):
        try:
            return int(self.rpcCaller.call("eth_blockNumber"), 16)
        except TypeError:
            return self.rpcCaller.call("eth_blockNumber")

    def get_block(self, height):
        blockDict = self.rpcCaller.call("eth_getBlockByNumber", [hex(height), True])
        block = self.init_block(blockDict)
        txs = self.get_block_transactions(blockDict)
        for txDict in txs:
            block.add_transaction(self.init_transaction(txDict))
        return block

    def get_block_transactions(self, blockDict):
        return [tx for tx in blockDict['transactions']]

    def init_block(self, blockDict):
        return BlockSchema(blockDict)

    def init_transaction(self, txDict):
        return TransactionSchema(txDict)

import argparse
import json
import sys
import os

BASE_DIR = (os.path.abspath(os.path.dirname(__file__))).replace("/parsing/scripts", '')
sys.path.append(BASE_DIR)

from parsing.config import NODE_URL
from parsing.node import Node


def main(block_heights):
    node = Node(NODE_URL)

    results = []
    for height in block_heights:
        block = node.get_block(height)
        block_data = {
            "hash": block.hash,
            "number": block.number,
            "blockHeight": block.blockHeight,
            "blockTime": block.blockTime,
            "difficulty": block.difficulty,
            "author": block.author,
            "extra_data": block.extra_data,
            "gas_limit": block.gas_limit,
            "gas_used": block.gas_used,
            "logs_bloom": block.logs_bloom,
            "miner": block.miner,
            "mix_hash": block.mix_hash,
            "parent_hash": block.parent_hash,
            "nonce": block.nonce,
            "receipts_root": block.receipts_root,
            "seal_fields": block.seal_fields,
            "sha3_uncles": block.sha3_uncles,
            "size": block.size,
            "state_root": block.state_root,
            "timestamp": block.timestamp,
            "total_difficulty": block.total_difficulty,
            "transactions_root": block.transactions_root,
            "uncles": block.uncles,
            "transactions": block.transactions
        }

        transactions = []
        for tx in block.get_transactions():
            transactions.append({
                "block_hash": tx.block_hash,
                "block_number": tx.block_number,
                "chain_id": tx.chain_id,
                "condition": tx.condition,
                "creates": tx.creates,
                "from": tx.from_,
                "to": tx.to,
                "gas": tx.gas,
                "gas_price": tx.gas_price,
                "hash": tx.hash,
                "input": tx.input,
                "nonce": tx.nonce,
                "public_key": tx.public_key,
                "r": tx.r,
                "raw": tx.raw,
                "s": tx.s,
                "standard_v": tx.standard_v,
                "transaction_index": tx.transaction_index,
                "v": tx.v,
                "value": tx.value
            })

        block_data['transactions'] = transactions
        block_data['tx_count'] = len(transactions)
        results.append(block_data)
    
    sys.stdout.write(json.dumps(results))



if __name__ == "__main__":
    argParser = argparse.ArgumentParser()
    argParser.add_argument("--heights", nargs='+', default=None, help="List of block heights to parse.")
    args = argParser.parse_args()
    if not args.heights:
        raise Exception("No block heights provided.")

    block_heights = [int(height) for height in args.heights if height]
    main(block_heights)

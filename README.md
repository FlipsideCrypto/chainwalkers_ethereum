# Chainwalkers Ethereum Parser

This parser communicates with an Ethereum node to extract and decodes blocks & transactions.

## Building

A docker image of the ethereum parser can be built by running:

```shell
bash builder_docker_image.sh
```

This will create an image with the tag `chainwalkers_ethereum:latest`.

## Up and Running

This parser has two entry points, each of which writes a json response to stdout.

1. `get_height.sh`: returns the current height
2. `parse_blocks.sh [int, int, ...]`: returns an array of decoded blocks and each blocks transactions

To get the latest height of the blockchain run:

```shell
> docker run chainwalkers_ethereum:latest bash get_height.sh
{
    "height": 7591808
}
```

To parse a list of blocks run:

```shell
> docker run chainwalkers_ethereum:latest bash parse_blocks.sh 7591805 7591806 7591807 7591808
[
    {
        "hash": "0x88e96d4537bea4d9c05d12549907b32561d3bf31f45aae734cdc119f13406cb6",
        "transactions": [
            {
                "hash": "",
                "from": "",
                "to": "",
                "events": [...],
                "logs": [...]
                ...
            }
        ],
        ...
    },
    ...
]
```

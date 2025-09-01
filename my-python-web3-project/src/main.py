
import argparse
import yaml
from web3 import Web3

def main():
    parser = argparse.ArgumentParser(description="Node monitor configuration")
    parser.add_argument('--config', type=str, default='nodalyth.config', help='Path to the config file (default: nodalyth.config)')
    args = parser.parse_args()

    # Read and parse the YAML config file
    try:
        with open(args.config, 'r') as f:
            config = yaml.safe_load(f)
        url = config.get('url')
        if not isinstance(url, str):
            raise ValueError("Config file must contain a string value for 'url'.")
        print(f"Config file: {args.config}")
        print(f"URL: {url}")

        # Connect to the node using web3.py
        w3 = Web3(Web3.HTTPProvider(url))

        block_number = "latest"  # Replace with the desired block number or use 'latest'
        block = w3.eth.get_block(block_number)

        print(block)

        if w3.is_connected():
            print("Successfully connected to the node.")
            print(f"Node client version: {w3.client_version}")
        else:
            print("Failed to connect to the node.")
    except Exception as e:
        print(f"Failed to read config file or connect to node: {e}")

if __name__ == "__main__":
    main()


import argparse
import yaml

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
	except Exception as e:
		print(f"Failed to read config file: {e}")

if __name__ == "__main__":
	main()

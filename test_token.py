#!/usr/bin/env python3

import requests

def validate_token(token):
	r = requests.get(
		'https://discordapp.com/api/v6/gateway/bot',
		headers={'Authorization': 'Bot ' + token},
	)
	if r.status_code == 200:
		return True
	if r.status_code == 401:
		return False

	raise RuntimeError('token invalid')

def main():
	import sys
	with open('token') as f:
		sys.exit(2 if not validate_token(f.read().strip()) else 0)

if __name__ == '__main__':
	main()

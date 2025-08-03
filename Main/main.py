import os
import time
import truthbrush as tb
from pprint import pprint

# Set credentials
os.environ['TRUTHSOCIAL_USERNAME'] = ''
os.environ['TRUTHSOCIAL_PASSWORD'] = ''

api = tb.Api()

# Sleep to avoid Cloudflare's wrath
time.sleep(3)

# Search for accounts named Donald
search_results = list(api.search(searchtype='accounts', query='Donald'))
accounts = search_results[0].get('accounts', [])

print("Accounts:")
for acc in accounts:
    print(acc.get('username'), acc.get('id'))

# Choose one account ID manually, like:
account_id = accounts[0].get('id')

# Sleep again before requesting statuses
time.sleep(3)

# Pull statuses (no handle, use account_id)
print(f"\nPulling statuses for ID {account_id}...")
statuses = api.pull_statuses(account_id=account_id, limit=5)

for s in statuses:
    print(s.id, s.content, s.created_at)

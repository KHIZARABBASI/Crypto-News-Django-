## Add Default Categories

Use the Django admin panel or the Django shell to add default categories.
Example in the shell:
``bash
`
python manage.py shell
python
Copy code
from website.models import Category
default_categories = [
    "Bitcoin", "Ethereum", "Altcoins", "Market Trends",
    "DeFi", "NFTs", "Blockchain Technology",
    "Crypto Regulations", "Crypto Scams and Hacks", "Mining and Staking"
]
for category in default_categories:
    Category.objects.get_or_create(name=category)`
```
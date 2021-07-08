[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
## URL shorter

This script for shortening links using the service ***[Bitly](https://bitly.com/)***.

If you follow the already shortened link, you will get the number of clicks on the link.

### Install
You need Python3 to run the script!

Clone a repository from GitHub.
```
git clone https://github.com/kutuzov13/Bitly-URL-shorter.git
```

Install Requirements.
```
pip install -r requirements.txt
```

### Libraries
```python
# For requests to API Bitly.
import requests 
# to access environment variables.
from dotenv import load_dotenv 
```
### Environment Variables
The token is taken from environment variables.
- Create a file ```.env``` next to the file ```main.py```.
- Write the token to a file ```.env```: ```BITLINK_TOKEN='YOU_TOKEN'```.

Bitly API Access Token. The token can be obtained in your personal account ***[Bitly](https://bitly.com/)***.

### Start
Run the script by passing the link to shorten:
```
python main.py https://github.com/
```
Run the script, passing the already shortened link to get the number of clicks on the link
```
python main.py https://bit.ly/3bcdiFH 
```

#### Target
The code is written for educational purposes as an online course for web developers ***[dvmn.org](https://dvmn.org/referrals/LKx4rvFOn7SwkzhVrznRuPRs6KUOF6jkJH2oImC2/)***.

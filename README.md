# extract-omments
### Extract all comments from web pages , support all comments format , useful in bughunting

# Description
often times , the comments which found in web pages may be very interested and require you to look into web pages and search on comments to read <br>
this script will extract all comments from all web pages without you open pages and look into src code , may be look into src code all pages harder if you hunting big target <br>
this tool will facilitate everything.

# install
run blow commands
```sh
git clone https://github.com/Abdulrahman-Kamel/extract-omments.git
cd extract-comments && pip3 install -r requirements.txt
chmod +x extract-comments.py && sudo mv extract-comments.py /usr/bin/extract-comments
```

## Usage
```sh
cat urls.txt | extract-comments
```

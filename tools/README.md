# Usage

##### Required as input:
```
$ cat wordlist.txt
> password1
> password3
> password3
```
##### Convert wordlist.txt to bruteforce.json:
```
$ python3 wordlist_to_json.py
```
##### Returns:
```
> Working on wordlist.txt
> Converting to bruteforce.json
> Output written to file(s)
$ cat bruteforce.json
> {"candidates":["password1","password2","password3"]}
```
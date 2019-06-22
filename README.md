# bruteforce.js

A naively simple, probably time consuming and inefficient, approach to running dictionary attacks on client side encrypted pages from https://satoshistreasure.xyz. While it is _festina lente_ level slow, it does have 2 advantages. First, it uses the literal identical code as the Satoshi's Treasure website, so reliability of password checking and decryption technique (e.g. base64 padding technique) is guaranteed. Second, it is easy to use even for a non-technical person (_but I still need to make it easier, so that only the word list file needs to be edited_). 

# Depedencies
- Node.js (https://nodejs.org)
- Python (https://www.python.org/downloads/)

# Usage

- *Step 1)* Create a password list and convert it to a json format

  #### Creating a password:
  
  There are many free tools available for creating txt wordlists that can easily be converted to json format using one of the 2 options below.
  
  _Recommended word list generators:_
  - Crunch (http://manpages.ubuntu.com/manpages/bionic/man1/crunch.1.html)
  - Mentalist (https://github.com/sc0tfree/mentalist)
  - Paw (https://github.com/tehw0lf/paw)

  #### Converting your to json format:

  - ##### Option 1: Using python
    - If python is in your path you can use the python script included in the repo: [a link](https://github.com/drewstaylor/satoshis-treasure-brute-forcer/blob/master/tools/wordlist_to_json.py) just rename your file to `wordslist.txt`, place it in the `tools` folder and run the json conversion script.
    
    Example
    ```
    $ cd tools
    $ python3 wordlist_to_json.py
    > Working on wordlist.txt
    > Converting to bruteforce.json
    > Output written to file(s)
    $ mv bruteforce.json ../bruteforce.json # moves the file back into the root folder
    ```
    
    The above example is run directly from the `/tools` folder, and creates a ready to use `brutefroce.json` from any any file called `wordlist.txt` that is placed in the tools folder

  - ##### Option 2: Raw and dirty cut and paste

    - Take the json array you made in step 1 and use it as the value of the `candidates` array in `./bruteforce.json`. This will become the word list used by the script you will run in the final step. See `./bruteforce.example.json` for a very basic formatting example.

    - *WARNING* The current out of the box `./bruteforce.json` included in this repo is 1.7 million passwords long. Avoid opening it in a text editor or do so at your own risk! (because the editor or your PC could crash). Better to open `./bruteforce.example.json`, paste in your words, and save the edited example file as `./bruteforce.json` :)

- *Step 2)* Open up `./bruteforce.js`

Replace line 11 with the encrypted html string you can get from the bottom of the html document of the encrypted page hosted at https://satoshistreasure.xyz

Example

![View source code of target clue page](https://raw.githubusercontent.com/drewstaylor/satoshis-treasure-brute-forcer/master/assets/viewsource_example.png)

![Extracted encryped html from the encryptedMsg variable](https://raw.githubusercontent.com/drewstaylor/satoshis-treasure-brute-forcer/master/assets/ecryptedhtml_example.png)

```
// Replace the contents of `encryptedClue` with the contents of the Satoshi's Treasure `encryptedMsg` variable
// This variable can be found in the html code of the clue page at the bottom of the document
// Or, simply right click the page from your browser, select "View Source", and perform a text
// search (Ctrl + F) for "encryptedMsg"
let encryptedClue = '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';

```

- *Step 3)* Run the brute forcer script from your terminal, bash or CMD:


Example
```
node bruteforce.js
```

# Benchmarks

*Tested on Intel i7-7700 CPU @ 3.6 GHz:*

![Extracted encryped html from the encryptedMsg variable](https://raw.githubusercontent.com/drewstaylor/satoshis-treasure-brute-forcer/master/assets/benchmark.png)

- Number of password candidates tested by benchmark: `1,754,116`

- Length of *all* passwords used in benchmark: `45 chars`

- Last iteration output from script (including start and end timestamps):
```
FINAL ITERATION!
Process started: Fri Jun 21 2019 10:50:17 GMT-0400 (Eastern Daylight Time)
Final iteration at: Fri Jun 21 2019 11:13:31 GMT-0400 (Eastern Daylight Time)
```

*E.g. The script yields about 76,265 passwords per minute (of char length 45), or about 1,271 passwords (of char length 45) per second when run from a reasonably powered machine*

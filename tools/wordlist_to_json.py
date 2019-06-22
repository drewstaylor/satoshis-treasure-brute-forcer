import json

# Wordlist to be converted (TXT file in)
textFilename = "wordlist.txt"

# JSON output (JSON file out)
jsonFilename = "bruteforce.json"

# File reader output
passwordCandidates = []

# Terminal log
print("Working on ", textFilename)

with open(textFilename) as file:
    for line in file:
        # Append to JSON convertible
        passwordCandidates.append(line)

# Terminal log
print("Converting to ", jsonFilename)

# Convert and output to JSON file
jsonData = {}  
jsonData['candidates'] = passwordCandidates
with open(jsonFilename, 'w') as outfile:  
    json.dump(jsonData, outfile)

# Terminal log
print('Output written to file(s)')
# Automate repetitive keyboard and mouse tasks with python3

### William Lamb
### Created 09/22/18
### Updated 10/06/18

For Mac using python3
On Mac the keylogger portion needs sudo privileges to capture non-special characters.

##### Dependencies:
- pynput

### Disclaimer
This project is not intended for use in any illegal or nefarious way, rather only to provide a simple method of automating recurring, identical tasks. Etc.

### Notes:
- for an alphanumeric key, the `key` variable returns the key in single quotation marks, like `'a'`. For an alphanumeric key using `key.char` the key returns just as is, like `a`.

#### TODO:
- Turn program into something that can be called from command line: "sudo python3 Logger.py -o outputFile"
- Write program that can interpret input file logs and replicate from command line: "sudo python3 Automate.py -i inputFile -rep numberOfRepetitions"
- Logging includes pressing the x key and releasing control at the very beginning, which should be ignored
- Writing characters with combinations like option-c (which outputs ç) and then letting go of option before c doesn't clear the ç character. Should letting go of the option key clear the entire keysPressed list? Should there be a track of how many keypresses before a key is released, and return an array with that many items cut from the end?
- Encapsulate key and mouse loggers into single class?
- Change text log to json log?
- implement saving logs to file to store for later recall
- interpret text file back into actions
- encrypt saved logs based on read-in buffer file sizes? Add (random) filler to end of file/end of line to hit buffer size? Would there ever be a file large enough that the program can't read the whole thing in at once to unencrypt? Does the program need the whole file to unencrypt a section?  Ask for password to encrypt and decrypt
- add data compression option on mouse moves

### Future possibilities:
- add gui/create desktop program to allow users to edit each step individually

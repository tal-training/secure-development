### Integrity Exercises Answers

##### Exercise: Hash Creation
write a script to calculate the hash of a file using a programming language of your choice. 

###### Solution (Python Example)
```python
import hashlib

def calculate_checksum(filename):
    with open(filename, 'rb') as f:
        data = f.read()
        checksum = hashlib.sha256(data).digest()
        return checksum

# Calculate Checksum
filename = 'file.txt'
checksum = calculate_checksum(filename)
print('Checksum:', checksum.hex())
```

##### Exercise: Checksum Verification

Write a script that calculates the checksum for a given file and compares it with a known good value.

###### Solution (Python Example)

```python
import hashlib

file_path = 'file.txt'
known_good_checksum = input("Enter SHA256 hash: ")

# Calculate the file checksum
file_content = open(file_path, 'rb').read()
checksum = hashlib.sha256(file_content).hexdigest()

if checksum == known_good_checksum:
    print('File integrity is maintained')
else:
    print('File integrity has been compromised')
```

##### Exercise: Source Verification

You got an email from your manager with a source file attached, asking you to fix a bug in the code and upload to production. How do you know that the code is authentic?

###### Solution 

Your manager should send you the hash of the file so you can verify it using the method in the above exercise. Note that the hash can be fake as well. The more secure solution is to sign the file, as we will learn later in the course. 


### Confidentiality Exercises

##### Exercise: Simple Data Encryption

1. Use a standard encryption library to encrypt some text and save it in a file.

2. How can you decrypt the data?

3. Write a program to decrypt the encrypted file. You need to store the key or ask the user to store it. 

4. Where should you store the key?


##### Exercise: Secure password storage

1. Create a simple script that asks the user to choose a password and store it in a file. Use a secure method to store the passwords (e.g. hashing).

2. How can you use the hashed password to authenticate the user?

##### Exercise: Secrets in code

Following is the source code for a function that connects to an API using a secret API key. How can you protect the key so it is not stored in cleartext in the source file?

```python
def fetch_weather(API_KEY, city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    weather_data = response.json()
    return weather_data

API_KEY = 'b1b15e88fa797225412429c1c50c122a1'
city = 'New York' 

weather_data = fetch_weather(api_key, city)
```

##### Exercise: Protecting Patient Records in Web App

1. Run the project from the command line terminal: 

```bash
flask run
```

2. Open [Test App](http://127.0.0.1:5000/). 

3. Can you get other patient names?

4. What other information about the patients can you get?

5. What are the reasons for this vulnerability in the following:
- Code 
- Design
- Architecture 

6. What fixes are possible to mitigate the vulnerability?

7. After fixing the problem, can you still get data about other patients?

- If yes, how can you fix those issues?

8. Stop the app (Ctrl+C) and run it on all interfaces so other students can connect:

```bash
flask run -h 0.0.0.0
```

- Ask other students to connect to your IP address and try to break your defenses and get as much data as possible. 




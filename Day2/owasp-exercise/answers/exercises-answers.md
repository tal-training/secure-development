### Confidentiality Exercises


##### Exercise: Simple Data Encryption

1. Use a standard encryption library to encrypt some text and save it in a file.

    ###### Solution (Python Example)

    See [here](encrypt-data.py)

2. How can you decrypt the data?

    ###### Solution (Python Example)

    You need the encryption key, otherwise the data is lost. 

3. Write a program to decrypt the encrypted file. You need to store the key or ask the user to store it. 

    ###### Solution (Python Example)

    See [here](decrypt-data.py)

4. Where should you store the key?

    ###### Solution (Python Example)

    The key should be protected using the "defense in depth" principle will will learn about in the course. 

##### Exercise: Secure password storage

1. Create a simple script that asks the user to choose a password and stores it in a file. Use a secure method to store the passwords (e.g., hashing).

    ###### Solution (Python Example)
    
```python
import hashlib
import pickle

password=input("Hi user, please choose a password: ")

hashed_password = hashlib.sha256(password.encode()).hexdigest()

passwords = {"user", password}

with open("passwords.pkl", "wb") as f:
    pickle.dump(passwords, f)
    print("password saved")
```

2. How can you use the hashed password to authenticate the user?

    You calculate the hash on the password provided during login, and compare the calculated hash to the stored hash. 

###### Solution (Python Example)

```python
def login():
    password=input("enter password for user: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    with open("passwords.pkl", "rb") as f:
        hash=pickle.load(f)["user"]
        print(hash, hashed_password)
        if hash==hashed_password:
            print("login successful")
        else:
            print("unauthorized")
```

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

###### Solution (Python Example)

    The key should be stored securely and loaded at run-time, for example using environment variables:

```python
API_KEY = os.environ.get('OPENWEATHERMAP_API_KEY')
```

##### Exercise: Protecting Patient Records in Web App

###### Solution (Python Example)

1. Run the vulnerable project in the exercises folder (not the answers folder) from the command line terminal: 

```bash
flask run
```

2. Open [Test App](http://127.0.0.1:5000/). 

3. Can you get other patient names?

$Answer$

Yes. If you open the browser developer tools => network and look at the requests to the requests to /api/data, you will see many more patient names in the response JSON. 

4. What other information about the patients can you get?

$Answer$

You can see the date of the next appointment and the name of the doctor.

5. What are the reasons for this vulnerability in the following:
- Code 
- Design
- Architecture 

$Answer$

The reasons are:
- Client side validation: The filtering of the users is done on the client, which the user controls. 
- The SQL query is too open and does not restrict only the name field, so it exposes other columns in the DB. 
- There is no authorization, the SQL query is not restricted to specific user ID.
- There is no user identification, authentication or authorization, so the server cannot identify the client.


6. What fixes are possible to mitigate the vulnerability?

$Answer$

- All filtering has to be done on the server. The client should only get the data that belongs to the user.
- The SQL query should be:
```SQL
SELECT name FROM data WHERE id=<user_id> 
```
- The client should be authenticated. In a REST API microservices architecture, this is done in a stateless way by providing an access token in every request header.
- The access token is obtained via a special endpoint. In the example solution the token is obtained randomly. In the real world this is done via OAUTH and JWT.

7. After fixing the problem, can you still get data about other patients?

$Answer$
- Yes, if the attacker knows the user ID then they can get the name. For example, [like this](http://127.0.0.1:5000/api/data/11). This kind of attack is called enumeration or brute force as we will learn about in the course. 
- The SQL is vulnerable to SQL Injection which is an integrity problem we will learn about in the course. 

- If yes, how can you fix those issues?

$Answer$
- In the real world, the request to /api/data will contain a signed token in a request header. Only after validating the token, the endpoint will execute the query. Otherwise it will return "403 unauthorized".
- SQL Injection can be fixed via prepared statements as we will learn in the course. 


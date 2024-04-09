### A simple full CRUD API in dotnet
 
First, create a new ASP.NET Core Web API project:
```csharp
dotnet new webapi -n SimpleCrudApi
cd SimpleCrudApi
```
Next, add a model for the resource you want to manage. For this example, let's create a simple `Person` model:

**Models/Person.cs:**
```csharp
public class Person
{
    public int Id { get; set; }
    public string Name { get; set; }
    public int Age { get; set; }
}
```
Now, let's create a controller that will handle the CRUD operations for this model. Add a new file called `PeopleController.cs` to the 
`Controllers` folder:

**Controllers/PeopleController.cs:**
```csharp
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using SimpleCrudApi.Models;

namespace SimpleCrudApi.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class PeopleController : ControllerBase
    {
        // Fake data store for demonstration purposes
        private static List<Person> people = new List<Person>
        {
            new Person { Id = 1, Name = "Alice", Age = 30 },
            new Person { Id = 2, Name = "Bob", Age = 40 }
        };

        // GET: api/people
        [HttpGet]
        public ActionResult<IEnumerable<Person>> GetPeople()
        {
            return people;
        }

        // GET: api/people/5
        [HttpGet("{id}")]
        public ActionResult<Person> GetPerson(int id)
        {
            var person = people.Find(p => p.Id == id);

            if (person == null)
            {
                return NotFound();
            }

            return person;
        }

        // POST: api/people
        [HttpPost]
        public ActionResult<Person> PostPerson(Person person)
        {
            people.Add(person);
            return CreatedAtAction("GetPerson", new { id = person.Id }, person);
        }

        // PUT: api/people/5
        [HttpPut("{id}")]
        public IActionResult PutPerson(int id, Person person)
        {
            if (id != person.Id)
            {
                return BadRequest();
            }

            var existingPerson = people.Find(p => p.Id == id);
            if (existingPerson == null)
            {
                return NotFound();
            }

            existingPerson.Name = person.Name;
            existingPerson.Age = person.Age;

            return NoContent();
        }

        // DELETE: api/people/5
        [HttpDelete("{id}")]
        public IActionResult DeletePerson(int id)
        {
            var person = people.Find(p => p.Id == id);
            if (person == null)
            {
                return NotFound();
            }

            people.Remove(person);
            return NoContent();
        }
    }
}
```
In this example, we're using an in-memory list of `Person` objects to simulate a database. In a real-world application, you would replace 
this with actual data storage such as SQL Server or MongoDB.

With this code in place, you now have a simple full CRUD API for managing `Person` objects. You can test the endpoints using tools like 
Postman or Swagger.

#### Here's an example of how you could implement some of the OWASP Top 10 security best practices in code for each endpoint:

**GET:**

* Use parameterized queries to prevent SQL injection attacks.
```csharp
// GET: api/people
[HttpGet]
public ActionResult<IEnumerable<Person>> GetPeople()
{
    using (var connection = new SqlConnection(_connectionString))
    {
        var command = new SqlCommand("SELECT * FROM People", connection);
        connection.Open();
        using (var reader = command.ExecuteReader())
        {
            var people = new List<Person>();
            while (reader.Read())
            {
                people.Add(new Person
                {
                    Id = reader.GetInt32(0),
                    Name = reader.GetString(1),
                    Age = reader.GetInt32(2)
                });
            }
            return Ok(people);
        }
    }
}
```
* Validate input parameters to ensure they match expected types and formats.
```csharp
// GET: api/people/{name}
[HttpGet("{name}")]
public ActionResult<IEnumerable<Person>> GetPeopleByName(string name)
{
    if (!int.TryParse(name, out _))
    {
        return BadRequest();
    }

    using (var connection = new SqlConnection(_connectionString))
    {
        var command = new SqlCommand($"SELECT * FROM People WHERE Name LIKE '%{name}%'", connection);
        connection.Open();
        using (var reader = command.ExecuteReader())
        {
            var people = new List<Person>();
            while (reader.Read())
            {
                people.Add(new Person
                {
                    Id = reader.GetInt32(0),
                    Name = reader.GetString(1),
                    Age = reader.GetInt32(2)
                });
            }
            return Ok(people);
        }
    }
}
```
* Use HTTPS to encrypt data in transit.

Add the following code to the `Startup.cs` file:
```csharp
public void ConfigureServices(IServiceCollection services)
{
    services.AddControllers();
    services.AddHttpsRedirection(options =>
    {
        options.RedirectStatusCode = StatusCodes.Status301MovedPermanently;
    });
}

public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
{
    // ...

    app.UseHttpsRedirection();

    // ...
}
```
* Implement access controls to restrict unauthorized access to sensitive data.

Add the following code to the `Startup.cs` file:
```csharp
public void ConfigureServices(IServiceCollection services)
{
    services.AddControllers();

    services.AddAuthorization(options =>
    {
        options.AddPolicy("AdminOnly", policy =>
            policy.RequireRole("Administrator"));
    });
}

public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
{
    // ...

    app.UseAuthorization();

    // ...
}
```
In the `PeopleController`:
```csharp
// GET: api/people
[HttpGet]
[Authorize(Policy = "AdminOnly")]
public ActionResult<IEnumerable<Person>> GetPeople()
{
    // ...
}
```
* Use rate limiting to prevent denial-of-service (DoS) attacks.

Add the following code to the `Startup.cs` file:
```csharp
public void ConfigureServices(IServiceCollection services)
{
    services.AddControllers();
    services.AddRateLimiting();
}

public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
{
    // ...

    app.UseRateLimiting();

    // ...
}
```
* Enable logging and monitoring to detect suspicious activity.

Add the following code to the `Startup.cs` file:
```csharp
public void ConfigureServices(IServiceCollection services)
{
    services.AddControllers();
    services.AddLogging();
}

public void Configure(IApplicationBuilder app, IWebHostEnvironment env, ILogger<Startup> logger)
{
    // ...

    if (env.IsDevelopment())
    {
        app.UseDeveloperExceptionPage();
        app.UseSwagger();
        app.UseSwaggerUI(c => c.SwaggerEndpoint("/swagger/v1/swagger.json", "My API V1"));
    }
    else
    {
        app.UseHsts();
    }

    app.UseHttpsRedirection();

    app.UseRouting();

    app.UseAuthorization();

    app.UseRateLimiting();

    app.UseEndpoints(endpoints =>
    {
        endpoints.MapControllers();
    });

    logger.LogInformation("Application started.");
}
```
**GET (by ID):**

* Implement input validation for the `id` parameter to ensure it is a valid integer.
```csharp
// GET: api/people/{id}
[HttpGet("{id}")]
public ActionResult<Person> GetPersonById(int id)
{
    if (id <= 0)
    {
        return BadRequest();
    }

    using (var connection = new SqlConnection(_connectionString))
    {
        var command = new SqlCommand($"SELECT * FROM People WHERE Id = {id}", connection);
        connection.Open();
        using (var reader = command.ExecuteReader())
        {
            if (!reader.Read())
            {
                return NotFound();
            }

            return Ok(new Person
            {
                Id = reader.GetInt32(0),
                Name = reader.GetString(1),
                Age = reader.GetInt32(2)
            });
        }
    }
}
```
* Return minimal information in error messages to avoid leaking sensitive data.

See the above example for `GET: api/people`.

* Use HTTP security headers like Content-Security-Policy, X-

 * Use HTTP security headers like Content-Security-Policy, X-Content-Type-Options, and X-Frame-Options to prevent cross-site scripting 
(XSS), content sniffing, and clickjacking attacks.

Add the following code to the `Startup.cs` file:
```csharp
public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
{
    // ...

    app.Use((context, next) =>
    {
        context.Response.OnStarting(() =>
        {
            context.Response.Headers.Add("Content-Security-Policy", "default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval'; 
style-src 'self'; img-src 'self' data:;");
            context.Response.Headers.Add("X-Content-Type-Options", "nosniff");
            context.Response.Headers.Add("X-Frame-Options", "SAMEORIGIN");
            return Task.CompletedTask;
        });

        return next();
    });

    // ...
}
```
* Implement access controls to restrict unauthorized access to sensitive data.

See the example for `GET: api/people`.

* Use parameterized queries or prepared statements to prevent SQL injection attacks.

See the example for `GET: api/people`.

* Enable logging and monitoring to detect suspicious activity.

See the example for `GET: api/people`.

**POST:**

* Validate user input to prevent security vulnerabilities like SQL injection and cross-site scripting (XSS) attacks.

Add the following code to the `PersonController` class:
```csharp
[HttpPost]
public IActionResult AddPerson([FromBody] Person person)
{
    if (!ModelState.IsValid)
    {
        return BadRequest(ModelState);
    }

    // ...
}
```
* Use HTTP security headers like Content-Security-Policy, X-Content-Type-Options, and X-Frame-Options to prevent cross-site scripting (XSS),
content sniffing, and clickjacking attacks.

See the example for `GET: api/people`.

* Implement access controls to restrict unauthorized access to sensitive data.

Add the following code to the `PersonController` class:
```csharp
[Authorize]
[HttpPost]
public IActionResult AddPerson([FromBody] Person person)
{
    if (!ModelState.IsValid)
    {
        return BadRequest(ModelState);
    }

    // ...
}
```
* Use parameterized queries or prepared statements to prevent SQL injection attacks.

See the example for `GET: api/people`.

* Enable logging and monitoring to detect suspicious activity.

See the example for `GET: api/people`.

**PUT:**

* Validate user input to prevent security vulnerabilities like SQL injection and cross-site scripting (XSS) attacks.

Add the following code to the `PersonController` class:
```csharp
[HttpPut("{id}")]
public IActionResult UpdatePerson(int id, [FromBody] Person person)
{
    if (!ModelState.IsValid)
    {
        return BadRequest(ModelState);
    }

    // ...
}
```
* Use HTTP security headers like Content-Security-Policy, X-Content-Type-Options, and X-Frame-Options to prevent cross-site scripting (XSS),
content sniffing, and clickjacking attacks.

See the example for `GET: api/people`.

* Implement access controls to restrict unauthorized access to sensitive data.

Add the following code to the `PersonController` class:
```csharp
[Authorize]
[HttpPut("{id}")]
public IActionResult UpdatePerson(int id, [FromBody] Person person)
{
    if (!ModelState.IsValid)
    {
        return BadRequest(ModelState);
    }

    // ...
}
```
* Use parameterized queries or prepared statements to prevent SQL injection attacks.

See the example for `GET: api/people`.

* Enable logging and monitoring to detect suspicious activity.

See the example for `GET: api/people`.

**DELETE:**

* Validate user input to prevent security vulnerabilities like SQL injection and cross-site scripting (XSS) attacks.

Add the following code to the `PersonController` class:
```csharp
[HttpDelete("{id}")]
public IActionResult DeletePerson(int id)
{
    if (id <= 0)
    {
        return BadRequest();
    }

    // ...
}
```
* Use HTTP security headers like Content-Security-Policy, X-Content-Type-Options, and X-Frame-Options to prevent cross-site scripting (XSS),
content sniffing, and clickjacking attacks.

See the example for `GET: api/people`.

* Implement access controls to restrict unauthorized access to sensitive data.

Add the following code to the `PersonController` class:
```csharp
[Authorize]
[HttpDelete("{id}")]
public IActionResult DeletePerson(int id)
{
    if (id <= 0)
    {
        return BadRequest();
    }

    // ...
}
```
* Use parameterized queries or prepared statements to prevent SQL injection attacks.

See the example for `GET: api/people`.

* Enable logging and monitoring to detect suspicious activity.

See the example for `GET: api/people`.


 ## Here are examples of implementing OWASP Top 10 - 2021 for the GET endpoint with explanations and code snippets:

**A01:2021 – Broken Access Control**

* Implement access controls to restrict unauthorized access to sensitive data.

Add the following code to the `PersonController` class:
```csharp
[Authorize(Roles = "Admin")] // Only users with the 'Admin' role can access this endpoint
[HttpGet]
public IActionResult GetPeople()
{
    var people = _context.People.ToList();
    return Ok(people);
}
```
This will ensure that only users who have been assigned the `Admin` role can access this endpoint and view the list of people. All other 
users will receive a 403 Forbidden response.

**A02:2021 – Cryptographic Failures**

* Use HTTPS to encrypt data in transit.

Add the following code to the `Startup.cs` file:
```csharp
public void ConfigureServices(IServiceCollection services)
{
    // ...

    services.AddControllers();

    services.Configure<MvcOptions>(options =>
    {
        options.Filters.Add(new RequireHttpsAttribute());
    });

    // ...
}
```
This will ensure that all requests to the API are made over HTTPS, encrypting data in transit and preventing man-in-the-middle attacks.

**A03:2021 – Injection**

* Use parameterized queries or prepared statements to prevent SQL injection attacks.

See the example for `GET: api/people` under A07:2017.

**A04:2021 – Insecure Design**

* Implement access controls to restrict unauthorized access to sensitive data.

See the example for A01:2021 above.

* Use HTTPS to encrypt data in transit.

See the example for A02:2021 above.

**A05:2021 – Security Misconfiguration**

* Remove unnecessary middleware and services from the application.

Add the following code to the `Configure` method in the `Startup.cs` file:
```csharp
public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
{
    // ...

    app.UseRouting();

    app.UseEndpoints(endpoints =>
    {
        endpoints.MapControllers();
    });

    app.UseHsts();
    app.UseHttpsRedirection();
}
```
This will ensure that only the necessary middleware and services are added to the application, reducing the attack surface and preventing 
potential security misconfigurations.

**A06:2021 – Vulnerable and Outdated Components**

* Keep all dependencies up-to-date.

Regularly check for updates to all dependencies used in the project and update them as soon as possible to ensure that any known 
vulnerabilities are patched.

**A07:2021 – Identification and Authentication Failures**

* Implement strong authentication and password policies.

Add the following code to the `ConfigureServices` method in the `Startup.cs` file:
```csharp
public void ConfigureServices(IServiceCollection services)
{
    // ...

    services.AddIdentity<ApplicationUser, IdentityRole>(options =>
    {
        options.Password.RequireDigit = true;
        options.Password.RequireLowercase = true;
        options.Password.RequireUppercase = true;
        options.Password.RequireNonAlphanumeric = true;
        options.Password.RequiredLength = 12;
    });

    // ...
}
```
This will ensure that users are required to use strong passwords, reducing the risk of weak or easily guessable passwords being used.

**A08:2021 – Software and Data Integrity Failures**

* Use digital signatures and/or hashes to verify the integrity of software and data.

Regularly verify the integrity of all software and data used in the project using digital signatures or hashes to ensure that they have not 
been tampered with.

**A09:2021 – Security Logging and Monitoring Failures**

* Implement logging and monitoring for security-related events.

Add the following code to the `ConfigureServices` method in the `Startup.cs` file:
```csharp
public void ConfigureServices(IServiceCollection services)
{
    // ...

    services.AddLogging(loggingBuilder =>
    {
        loggingBuilder.AddConsole();
        loggingBuilder.AddDebug();
    });

    // ...
}
```
This will ensure that security-related events are logged and can be monitored for suspicious activity.

**A10:2021 – Server-Side Request Forgery (SSRF)**

* Implement access controls to restrict unauthorized access to sensitive data.

See the example for A01:2021 above.

* Use HTTPS to encrypt data in transit.

See the example for A02:2021 above.

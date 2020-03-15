# C# 

<div style="width:1000px;margin:auto">
<details><summary><b>Input / Output</b></summary>
```csharp
// Reading input from user.
string name = Console.ReadLine();

// Printing the output
Console.WriteLine("Hello " + name);
Console.Write("Hello {0}", name);
```
</details>

<details><summary><b>Data Types</b></summary>
```csharp
int intNumber = 10;
float floatNumber = 10.123f;
double douNumber = 121.234d;
decimal decNumber = 123m;

string name = "Mosaab";
char character = 'M';

bool condition = true;

// Let C# determine the type of data.
// using "var" keyword.
var test = 1000;
```
</details>

<details><summary><b>Casting</b></summary>
```csharp
int intNumber = 10;
float floatNumber = 10.123f;
double douNumber = 121.234d;
string name = "";

# First way.
name = intNumber.ToString();

# Second way: using Convert class.
searialNo = Convert.ToInt32 (anyNo);

# Third way: direct casting.
searialNo = (int)anyNo;
```
</details>
</div>
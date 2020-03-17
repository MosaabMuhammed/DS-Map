# C# 

<div style="width:1000px;margin:auto">
<details><summary><b>Input / Output</b></summary>
```csharp
// Reading input from user.
string name = Console.ReadLine();
int num = int.Parse(Console.ReadLine());   // parse the string into integer.
# Handle if user doesn't provide an integer
int x = 0;
int.TryParse(Console.ReadLine(), out x);

// Printing the output
Console.WriteLine("Hello " + name);
Console.Write("Hello {0}", name);
```
</details>

<details><summary><b>Data Types</b></summary>
```csharp
byte ByteNumber = 123;   // 1 byte (0 --> 255)
sbyte SByteNum  = -12;    // 1 byte (-128 --> 127)


short shortNumber = 2;    // 2 bytes (-32,768 --> 32,768)
ushort UshortNum = 12;   // 2 bytes (0 --> 65,535)

int intNumber = 10;          // 4 bytes (-2,147,483,648 --> 2,147,483,648)
uint UintNum =  120;        // 4 bytes (0 --> 4,294,967,295)

long LongNum = 213;       // 8 bytes (-9,223,372,036,854,775,808 --> +9,223,...)
ulong ULongNum = 12;     // 8 bytes (0 --> 18,446,744,073,709,551,615)

float floatNumber = 10.123f;       // 4 bytes.
double douNumber = 121.234d;	// 8 bytes.
decimal decNumber = 123m;		// 16 bytes.

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

<details><summary><b>DateTime</b></summary>
```csharp
# DateTime
DateTime myDate = new DateTime(2020, 5, 25);
DateTime myDate = DateTime.Today;
DateTime myDate = DateTime.Now;

# Show DateTime 
Console.WriteLine(myDate.ToShortDateString());  // show only the date (short format).
Console.WriteLine(myDate.ToShortTimeString());  // show only the time (short format).
Console.WriteLine(myDate.ToLongDateString());   // (long format)
Console.WriteLine(myDate.ToLongTimeString());   // (long format)

# Formatted datetime.
string formattedDate = string.Format("Date is {0: yyyy MMMM dddd HH mm ss tt}", myDate);
Console.WriteLine(formattedDate);
```
</details>

<details><summary><b>If Condition</b></summary>
```csharp
if (num1 > num2)
{
	Console.WriteLine ("Num1 is larger than Num2");
}
else if (num1 < num2)
{
	Console.WriteLine ("Num1 is less than Num2");
}
else
{
	Console.WriteLine ("Num1 equals Num2");
}
```
</details>

<details><summary><b>Constants</b></summary>
```csharp
const double gravity = 9.8d;
```
</details>

<details><summary><b>String Manipulations</b></summary>
```csharp
string movieName = "       Lord of the RingS      ";

// Indexing
Console.WriteLine (movieName[12]);

// Trim
Console.WriteLine (movieName.Trim());

// Upper Case
Console.WriteLine (movieName.ToUpper ().Trim ());

// Lower Case
Console.WriteLine (movieName.Trim ().ToLower ());

// Length
Console.WriteLine (movieName.Length);

// Replace
Console.WriteLine (movieName.Replace ('l', 'L').Trim ());

// Index of 
Console.WriteLine (movieName.IndexOf ('o'));

// Last Index of
Console.WriteLine (movieName.LastIndexOf ('o')); 

// Substring
Console.WriteLine (movieName.Trim().Substring (5, 2));

// Remove after Index
Console.WriteLine (movieName.Trim().Remove (4));

// Insert
Console.WriteLine (movieName.Trim().Insert (0, "Added "));
```
</details>

<details><summary><b>Escape Characters</b></summary>
```csharp
// Ignore the special characters.
string path = @"C:\nami\tark";

// Don't ignore the special characters.
string path = "C:\\nami\\tark"
```
</details>

<details><summary><b>String Interpolation</b></summary>
```csharp
string name = "Mosaab";

Console.WriteLine("Welcome " + name);
Console.WriteLine("Welcome {0}", name);
Console.WriteLine($"Welcome {name}");
```
</details>

<details><summary><b>Loops</b></summary>
```csharp
// For Loop
for(int i = 0; i <= 10; i++) {
	Console.WriteLine (i);
}

// While Loop
int x = 5;
while (x <= 10) {
	Console.WriteLine (x++);
}
```
</details>

<details><summary><b>Math</b></summary>
```csharp
double x = 4.226d;

// Ceiling
Console.WriteLine($"Ceiling: {Math.Ceiling(x)}");

// Floor
Console.WriteLine($"Floor: {Math.Floor(x)}");

// Round
Console.WriteLine($"Round: {Math.Round(x, 2)}");

// Truncate
Console.WriteLine($"Truncate: {Math.Truncate(x)}");

// Max
Console.WriteLine($"Max: {Math.Max(x, y)}");

// Min
Console.WriteLine($"Min: {Math.Min(x, y)}");

// Sqrt
Console.WriteLine($"Sqrt: {Math.Sqrt(y)}");

// POW
Console.WriteLine($"Pow: {Math.Pow(2, 2)}");
```
</details>

<details><summary><b>Random</b></summary>
```csharp
// Random Integer.
Random rand = new Random();
int x = 0;
x = rand.Next(1, 13);
Console.WriteLine("Month: " + x);

// Random Float
double y = 0;
y = rand.NextDouble() * 10;
Console.WriteLine("Random Double: " + y);
```
</details>

<details><summary><b>Data Structures</b></summary>
<h4>Arrays</h4>
```csharp
// Instansiate an array
int[] nums = new int[5] { 1, 2, 3, 4, 5 };
string[] days = { "Sun", "Mon", "Tue", "Wed", "Thur", "Fri", "Sat" };

// Loop over the arrays. using FOR
for (int i=0; i < nums.Length; i++) {
	Console.WriteLine (nums [i]);
}

// Loop Over the array. using FOREACH.
foreach(var day in days) {
	Console.WriteLine (day);
}
```
</details>

</div>
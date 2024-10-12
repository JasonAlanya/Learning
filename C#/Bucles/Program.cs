//While
using System.Globalization;

int i = 0;
while (i < 10)
{
    Console.WriteLine(i);
    i++;
}

//for
for(int j = 0; j <= 10; j++)
{
    Console.WriteLine(j);
}

//do...while
int k = 0;
do
{
    Console.WriteLine(k);
    k++;
}while(k < 10);

//for each
var names = new List<string> { "names", "names2", "names3" };

foreach (var name in names)
{
    Console.WriteLine(name);
}

//arrays
int[] arr = new int[3];
arr[0] = 1;
arr[1] = 2;
arr[2] = 3;

//también se cuenta con el método arr.Lenght para los otros blucles
foreach (var item in arr)
{
    Console.WriteLine(item);
}

//if
string hoy = "Lunes";

if (hoy == "Lunes")
{
    Console.WriteLine("Happy lunes");
}
else
{
    Console.WriteLine("Wen finde");
}

//switch
switch (hoy)
{
    case "Lunes":
        Console.WriteLine("Es lunes");
        break;
    case "Martes":
        Console.WriteLine("Es martes");
        break;
    default:
        Console.WriteLine("qué dia será");
        break;
}
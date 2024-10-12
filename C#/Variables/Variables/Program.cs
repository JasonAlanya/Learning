//Declaración de variables
int i = 0;
long l = 1;

float f = 1.55555f;
double d = 2.66666666666d;

char c = 'c';
string str = "string";


//los parámetros pasados por readline solo son strings
string edad = Console.ReadLine();

int edadint = Convert.ToInt32(edad);
Console.Write("Tu edad es: " + edadint);

//Declaración de constantes
const int constante = 6;

//Declaración de variables que permitan un valor inicial null
int? nulo=null;
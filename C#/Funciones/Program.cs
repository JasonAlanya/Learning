//funciones
/*int calculo=calcularCuadrado(3);

int calcularCuadrado(int n)
{
    Console.WriteLine(n * n);
    return n*n;
}


CalcularAprobado(10);
void CalcularAprobado(int n)
{
    if (n < 5)
    {
        Console.WriteLine("Desaprobado");
    }
    else
    {
        Console.WriteLine("Aprobado");
    }
}


//métodos

var moto = new motos();

motos.este_arranca();

moto.Arrancar();

class motos
{
    //MÉTODO DE CLASE
    public static void este_arranca()
    {
        Console.WriteLine("Arrancar todas las motos");
    }
    public void Arrancar()
    {
        Console.WriteLine("Ruuuuuun RUUUN");
    }
}*/

//Recursividad

Console.WriteLine(CalcularFactorial(2));
long CalcularFactorial(int n)
{
    if (n == 1)
    {
        return 1;
    }
    return n * CalcularFactorial(n - 1);
}
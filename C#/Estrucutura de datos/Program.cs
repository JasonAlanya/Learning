//La estructuta debe ser llamada antes, sino genera un error
using System.Security.Cryptography.X509Certificates;

Coords misCoordineadas = new Coords(0,0);
Console.WriteLine("x: " + misCoordineadas.X);
Console.WriteLine("y: " + misCoordineadas.Y);

//Duplicación de la estructura
Coords misCoordenadas2 = misCoordineadas with { X = 30};
Console.WriteLine(misCoordenadas2);

public struct Coords
{
    public Coords(double x, double y)
    {
        X = x;
        Y = y;
    }

    public double X { get; set; }

    public double Y { get; set; }

    //Este es el método con el que se imprime en pantalla
    public override string ToString() => $"({X},{Y})";
}
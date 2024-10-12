//Crear archivos TCT y realziar operaciones

using System.IO;//Para txt
using System.Net;//Para json

string texto;

//Escribir en un archivo txt
try
{
    StreamWriter sw = new StreamWriter("miarchivo.txt" , true); //El segundo parámetro que señala si se añade o se sobreescribe
    sw.WriteLine("Escribiendo en el archivo");
    sw.WriteLine("por linea");
    sw.Close();
}
catch (Exception ex)
{
    Console.WriteLine("Ha ocucrrido un error: " + ex.Message);
}


//Lectura de un archivo txt
try
{
    StreamReader sr = new StreamReader("NuevoArchivo.txt");
    var line = sr.ReadLine();

    while(line != null)
    {
        Console.WriteLine(line);
        line= sr.ReadLine();
    }
    sr.Close();
    

}catch(Exception ex)
{
    Console.WriteLine("Ha ocucrrido un error: "+ex.Message);
}
finally
{
    Console.WriteLine("Final del try catch");
}

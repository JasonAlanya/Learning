//LINQ

// Origen de datos
int[] numbers = new int[10] {1,2,3,4,5,6,7,8,9,10};
//Obtener datos con consulta
var consulta=
    from numero in numbers
    where (numero%2==0)
    select numero;
//Ejecutar consulta
foreach(var numero in consulta)
{
    Console.WriteLine(numero);
}

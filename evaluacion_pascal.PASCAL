
program AAD12011;

var A , B, Suma : integer;

begin
   writeln('ingrese a');
   readln( A );
   writeln('introduzca segundo numero entero');
   readln( B );
   Suma := A + B;

   if ( Suma < 0 ) then
      writeln('LA SUMA SI ES MAYOR QUE CERO');
end.

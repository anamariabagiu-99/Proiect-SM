<html>

<head>

<?php
$status="Aplicația nu a fost lansată în execuție!";
    if(isset($_POST['start']))
    {
	$sir = $_POST['npm'] . '\n' . $_POST['npmax'] . '\n' . $_POST['dpm'] . '\n' . $_POST['dpmax'] . '\n' . $_POST['bm'] . '\n' . $_POST['bmax'] . '\n';

	/*verific ca datele introduse de utilizator sunt corecte, adica
	toate campurile au fost completate cu numere*/
	if (!(((is_numeric($_POST['npm']) && is_numeric($_POST['npmax'])) && ((is_numeric($_POST['dpm']) && is_numeric($_POST['dpmax']))) && (is_numeric ($_POST['bm'])) && is_numeric($_POST['bmax']))))
		{
		$status ="Trebuie sa introduceți doar numere!Programul nu va fi lansat în execuție.";
		}
	else
	{
		$status = "Datele introduse sunt corecte!";
        //verfic mai intai daca fisierul meu exista, daca programul a fost lansat in executie
       $exista = 1;
        if(file_exists("date_p.txt"))
        {
            $exista = 0;
        }
        //il deschid sau creez 
        $myfile = fopen("date_p.txt", "w");

        //construiesc sirul pe care vreau sa il scriu in  el 
        $sir = $_POST['npm'] . ' ' . $_POST['npmax'] . ' ' . $_POST['dpm'] . ' ' . $_POST['dpmax'] . ' ' . $_POST['bm'] . ' ' . $_POST['bmax'] . ' ';
        
	//scriu in fisier 
        fwrite($myfile, $sir);
        //pornesc programul

      if($exista == 1)
        {
            exec("sudo python /home/pi/Desktop/SM/Raspberry-SM/proiect/proiect_v1.py");
		$status = "Aplicația a fost lansată în execuție!";
        }
       //in cazul in care fisierul exista deja, datele folosite de aplicatie vor fi actualizate 
	//prin citirea din fisier.
	}		
}
       
    if(isset($_POST['stop']))
    {
        // sterg fisierul creat
        unlink("date_p.txt");
        //opresc toate procesele pornite de python
        exec('sudo killall python');
    }

	$help = "";
	if(isset($_POST['help']))
    {

        $help = "Anul trecut când a început pandemia, numărul de persoane dintr-un spațiu a devenit".
	"limitat, lucru puțin supărător atunci când dorim să intrăm într-o încăpere și suntem dați".
	" afară oarecum. Aplicația noastră vine în sprijinul acestei idei, persoanele care doresc să". 
	" intre într-un magazin să știe câte persoane sunt deja înăuntru și dacă mai pot intra înăuntru. 
	Contorizarea persoanelor este un lucru obositor și pentru angajați care trebui să fie atenți, pe
	lângă lucrurile la care lucrează, la clienți.<br><br>
	Cel care pornește aplicația poate configura:<br>
	numărul mediu de persoane - la care se va trimite un mail de atenționare;<br>
	numărul maximum de persoane - la atingerea acestui prag se va porni un buzzer și 
	se va trimite încă un mail;<br>
	distanța minimă - se referă la cea mai mică înălțime a unei persoane care poate intra în magazin;<br>
	distanța maximă - se referă la cea mai mare înălțime a unei persoane care poate intra în magazin.
<br>
Câmpurile trebuie să conțină doar numere și să fie completate toate, pentru pornirea/oprirea aplicației se folosește 
butonul corespunzător.<br>";
    }

    
   


?>

    <title>Aplicatie</title>
</head>

<body bgcolor="#FFCCFF">
    <font color="navy" face ="arial">
<h1 style="text-align: center;" >Contor pentru clienții dintr-un magazin</h1></font>
<center>
<form method="post">
<table witdh="400" border="1" bgcolor="#FFCCCC" bordercolor="blue">
    
<tr>
    
    <td style="text-align: center;"><b><font face="arial" color="purple" size="3em">Numărul mediu de persoane:</font></b></td>
    <td style="text-align: center;"><input type="text" name="npm"/></td>
</tr>
<tr>
    <td style="text-align: center;"><b><font face="arial" color="purple" size="3em">Numărul maximum de persoane:</font></b></td>
    <td style="text-align: center;"><input type="text" name="npmax"/></td>
</tr>
<tr>
    <td style="text-align: center;"><b><font face="arial" color="purple" size="3em">Distanţa minimă persoană</font></b></td>
    <td style="text-align: center;"><input type="text" name="dpm"/></td>
</tr>

<tr>
    <td style="text-align: center;"><b><font face="arial" color="purple" size="3em">Distanţa maximă persoană:</font></b></td>
    <td style="text-align: center;"><input type="text" name="dpmax"/></td>
</tr>
<tr>
    <td style="text-align: center;"><b><font face="arial" color="purple" size="3em">Frecventa medie buzzer:</font></b></td>
    <td style="text-align: center;"><input type="text" name="bm"/></td>
</tr>

<tr>
    <td style="text-align: center;"><b><font face="arial" color="purple" size="3em">Frecventa maximă buzzer:</font></b></td>
    <td style="text-align: center;"><input type="text" name="bmax"/></td>
</tr>
<tr>
    <td style="text-align: center;"><button name="start"> <font face="impact" color="blue">Pornește aplicația </font></button> </td>
    <td style="text-align: center;"> <button name = "stop"><font face="impact" color="red">Oprește aplicația</font></button></td>
</tr>
<tr>
    <center><td style="text-align: center;"><button name="help"> <font face="impact" color="green">Ajutor </font></button> </td>
  </center>  
</tr>
</font>
</table>
</form>
</center>
<br>

<font face="arial" color="black" size="3em">
	<p>
		<?php echo $status ?>
		<br>
		<?php echo $help ?>
		
	</p>
</font>

<br><br><br>
</body>
<footer>
<font color="blue" face ="arial"><h4> Facultatea de Automatică şi Calculatoare</h4><font>
    <font face="arial" color="navy" size="2em"> &copy; iunie 2021 Bagiu Anamaria Sopcă Ştefania </font>
</footer>

</html>


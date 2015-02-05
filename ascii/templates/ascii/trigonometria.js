function sin() {
    if ((a>=-1) && (a<=1)) {
        if (a==1) {
            x=(90-b)/c;
            document.getElementById("output").innerHTML=x+"°+"+k1+"°k (k∈Ꮓ)";
		}
        else if (a==-1) {
            x=(270-b)/c;
            document.getElementById("output").innerHTML=x+"°+"+k1+"°k (k∈Ꮓ)";
		}
        else if (a==0) {
            x=(0-b)/c;
            document.getElementById("output").innerHTML=x+"°+"+k2+"°k (k∈Ꮓ)";
            
		}
        else {
            x1=(57.3*Math.asin(a)-b)/c;
            x2=((180-57.3*Math.asin(a))-b)/c;
            document.getElementById("output").innerHTML=x1+"°+"+k1+"°k (k∈Ꮓ)<br>"+x2+"°+"+k1+"°k (k∈Ꮓ)";
        }
	}
	else {
		document.getElementById("output").innerHTML="нет корней";
	}
}
//функция вычисления косинуса
function cos() {
     if ((a>=-1) && (a<=1)) {
           if (a==1) {
                x=(0-b)/c;
                document.getElementById("output").innerHTML=x+"°+"+k1+"°k (k∈Ꮓ)";
			        }
            else if (a==-1) {
                x=(180-b)/c;
                document.getElementById("output").innerHTML=x+"°+"+k1+"°k (k∈Ꮓ)";
                }
            else if (a==0) {                
                x=(90-b)/c;
                document.getElementById("output").innerHTML=x+"°+"+k2+"°k (k∈Ꮓ)";
                }
            else {               
                    x1=(57.3*Math.acos(a)-b)/c;
                    x2=(-57.3*Math.acos(a)-b)/c;
                    document.getElementById("output").innerHTML=x1+"°+"+k1+"°k (k∈Ꮓ)<br>"+x2+"°+"+k1+"°k (k∈Ꮓ)";
			    }
            }
	 else {
         document.getElementById("output").innerHTML="нет корней";
     }
}
//функция вычисления тангенса
function tg() {
    x=(57.3*Math.atan(a)-b)/c;
    document.getElementById("output").innerHTML=x+"°+"+k2+"°k (k∈Ꮓ)";
}
////функция вычисления котангенса
function ctg() {
   x=(57.3*((Math.PI/2)-Math.atan(a))-b)/c;
    document.getElementById("output").innerHTML=x+"°+"+k2+"°k (k∈Ꮓ)";
}
function Start() {
		input = document.getElementById("input").value;
		fun_trig=/(.*)\(/.exec(input)[1];
		a=eval(/=(.*)/.exec(input)[1]);
		b=eval(/x(.*)\)/.exec(input)[1]);
        c=eval(/\((.*)x/.exec(input)[1]);
		if (isNaN(b)) b=0;
        if (isNaN(c)) c=1;
		k1=360/c;
        k2=180/c;

        if (fun_trig=='sin') {	 
			sin();
		}
		if (fun_trig=='cos') { //считает косинус
			cos();
		}			
		if (fun_trig=='tg') { //считает тангенс
			tg(); 
		}
		if (fun_trig=='ctg') { //считает котангенс
			ctg();
		}
}

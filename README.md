# DFA-implementation

Am implementat un Automat Finit Determinist care sa verifice daca un cuvant introdus poate fi modelat de un automat dat, despre care se stiu numarul de noduri, numarul de muchii, muchiile (de unde pornesc, unde se termina si litera pe care o gasim pe muchie), nodul de inceput, starile finale.<br />
La final se va afisa 'DA' si traseul parcurs in cazul in care cuvantul este acceptat, sau 'NU' daca acel cuvant nu poate fi modelat de acel automat. <br /><br />
Inputul este introdus de la tastatura, un model fiind:<br/>
&emsp;&emsp;&emsp;5 9<br/>
&emsp;&emsp;&emsp;0 0 1<br/>
&emsp;&emsp;&emsp;0 1 0<br/>
&emsp;&emsp;&emsp;1 0 1<br/>
&emsp;&emsp;&emsp;1 2 0<br/>
&emsp;&emsp;&emsp;2 0 1<br/>
&emsp;&emsp;&emsp;2 3 0<br/>
&emsp;&emsp;&emsp;3 0 1<br/>
&emsp;&emsp;&emsp;3 4 0<br/>
&emsp;&emsp;&emsp;4 4 0<br/>
&emsp;&emsp;&emsp;0<br/>
&emsp;&emsp;&emsp;0<br/>
&emsp;&emsp;&emsp;2<br/>
&emsp;&emsp;&emsp;001<br/>
&emsp;&emsp;&emsp;000100<br/><br/>
Pentru acest input, outputul corespunzator este: <br/>
&emsp;&emsp;&emsp;DA<br/>
&emsp;&emsp;&emsp;Traseu: 0 1 2 0 <br/>
&emsp;&emsp;&emsp;NU<br/><br/>
Structura inputului este: <br />
&emsp;&emsp;&emsp;nr_noduri nr_muchii<br/>
&emsp;&emsp;Pentru fiecare muchie din cele numarate:<br/>
&emsp;&emsp;&emsp;nod_start nod_final valoare_muchie(cod)<br/>
&emsp;&emsp;&emsp;nod_initial<br/>
&emsp;&emsp;&emsp;nod_final_0 nod_final_1 .... (unul sau mai multe)<br/>
&emsp;&emsp;&emsp;nr_stringuri_verificat<br/>
&emsp;&emsp;Pentru fiecare string din cele numarate:<br/>
&emsp;&emsp;&emsp;string<br/>
  

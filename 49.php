<html>
    <head>
            <link rel="stylesheet" type="text/css" href="externalcss/Untitled-1.css">
            <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"> 
            

    </head>
    <body class="head">
            <button id="but" type="button" onclick="window.location.href='./index.html'">HOME</button>
         <form method="POST" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
            <input type="number" class="button1" name="revw" id="in" min="1" max="5" onfocusout="myFunction()" required>
            
        </form>
            <h2 class="h2">GIVE YOUR REVIEW(0-5)</h2>
            
            <p id="p1" class="p3"><b>QUOTE OF THE DAY</b></p>
        
            <br><br><br><br><br>
        
        <h3 id="p1" class="p4">Love yourself for who you are, and trust me, if you are happy from within, you are the most beautiful person, and your smile is your best asset.
</h3>
        
        <div class="p6">
        
        <button id="p2"><a href='61.php' onclick='var x=document.getElementById("in").value;if(x.length==0){window.alert("PLEASE ENTER YOUR REVIEW");return false;}else return true;' >Next Page</a></button>
        <button id="p2"><a href='54.php' onclick='var x=document.getElementById("in").value;if(x.length==0){window.alert("PLEASE ENTER YOUR REVIEW");return false;}else return true;' >Next Page</a></button>
        <button id="p2"><a href='18.php' onclick='var x=document.getElementById("in").value;if(x.length==0){window.alert("PLEASE ENTER YOUR REVIEW");return false;}else return true;' >Next Page</a></button>
        <button id="p2"><a href='69.php' onclick='var x=document.getElementById("in").value;if(x.length==0){window.alert("PLEASE ENTER YOUR REVIEW");return false;}else return true;' >Next Page</a></button>
        <button id="p2"><a href='34.php' onclick='var x=document.getElementById("in").value;if(x.length==0){window.alert("PLEASE ENTER YOUR REVIEW");return false;}else return true;' >Next Page</a></button>
        <button id="p2"><a href='26.php' onclick='var x=document.getElementById("in").value;if(x.length==0){window.alert("PLEASE ENTER YOUR REVIEW");return false;}else return true;' >Next Page</a></button>
        <button id="p2"><a href='23.php' onclick='var x=document.getElementById("in").value;if(x.length==0){window.alert("PLEASE ENTER YOUR REVIEW");return false;}else return true;' >Next Page</a></button>
        <button id="p2"><a href='47.php' onclick='var x=document.getElementById("in").value;if(x.length==0){window.alert("PLEASE ENTER YOUR REVIEW");return false;}else return true;' >Next Page</a></button>
        <button id="p2"><a href='68.php' onclick='var x=document.getElementById("in").value;if(x.length==0){window.alert("PLEASE ENTER YOUR REVIEW");return false;}else return true;' >Next Page</a></button>
        <button id="p2"><a href='1.php' onclick='var x=document.getElementById("in").value;if(x.length==0){window.alert("PLEASE ENTER YOUR REVIEW");return false;}else return true;' >Next Page</a></button>
    
        </div> 
        
        <script>
                function myFunction(){
                    var x=document.getElementById("in").value;  
                    if(x>0 && x<6)
                        document.getElementById("in").disabled=true;
                }
                document.getElementById('in').onkeypress =
                function (e) {
                    var ev = e || window.event;
                    if(ev.charCode < 48 || ev.charCode > 57) {
                    return false; // not a digit
                    } else if(this.value * 10 + ev.charCode - 48 > this.max) {
                    return false;
                    } else {
                    return true;
                    }
                }
         </script>

        <?php
        $url=$_SERVER['REQUEST_URI'];
        $val=(parse_url($url));
        $path=($val['path']);
        $path=substr($path,6);
        $path=substr($path,0,-4);
        //echo($path);    

        $myfile=fopen("req_count.txt","r");
        // echo filesize("req_count.txt") . "\n";
        $read=explode("\n",fread($myfile,filesize("req_count.txt")));
        $read[$path-1]=strval(intval($read[$path-1])+1);
        $read=join("\n",$read);
        // echo $read;
        fclose($myfile);
       // echo("<br>");
        $myfile=fopen("req_count.txt","w");
        //echo("<br>");
        //echo($read);
        fwrite($myfile,$read);
        //echo("<br>");
        //echo($read);
        fclose($myfile);
        ?>  
  
    </body>
</html>
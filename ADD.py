<html>
<head>
	<title> Simple Calci </title>
</head>
<body>
	<div class="container">
		<input type="text" placeholder="first number" id="first" />
		<input type="text" placeholder="first number" id="second" />
		<div class="btns">
			<button onClick="multiply()">Multiply</button>
			<button onClick="add()">ADD</button>
		</div>
		<p> Result : <span id="result"></span></p>
	</div>
	<script type = "text/javascript">
		function multiply(){
        num1 = document.getElementById("first").value;
        num2 = document.getElementById("second").value;			
        if(num1 && num2 && num1 > 0 && num2 > 0){
          document.getElementById("result").innerText = num1 * num2 ;
        }
        else{
          document.getElementById("result").innerHTML = "Please enter a valid positive number" ;	
        }	
      }
		function add(){
			num1 = parseInt(document.getElementById("first").value);
			num2 = parseInt(document.getElementById("second").value);			
			if(num1 && num2 && num1 > 0 && num2 > 0){
				document.getElementById("result").innerText = num1 + num2 ;
			}
			else{
				document.getElementById("result").innerText = "Please enter a valid positive number" ;	
			}
		}	
	</script>
</body>
</html>
              

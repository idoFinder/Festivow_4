var submit = document.querySelector('#submit');

submit.onclick = function(){
	var userName = document.querySelector('#Name');
	var email = document.quetySelector('#email');
	var password = document.querySelector('#pass');
	var jsonObj = ' {"user_info":{ "user_name":userName , "user_email": email, "user_password": password }}';
	var jsonStr = JSON.stringify(jsonObj);
	localStorage.setItem("user_data", jsonStr);

}

function showPassword(){
	var x = document.querySelector('input[name="pass"]');
   	if (x.type === "password") {
      	x.type = "text";
    } else {
        x.type = "password";
    		}
	}

var submit = document.querySelector('button');

submit.onclick = function(){
				
	var userNameElement = document.querySelector('input[name="name"]');
	var userNameValue = userNameElement.value;

	var emailElement = document.querySelector('input[name="email"]');
	var emailValue = emailElement.value;

	var passwordElement = document.querySelector('input[name="pass"]');
	var passwordValue = passwordElement.value;

	if(passwordValue && emailValue && userNameValue){
		var userInfo = new Object();
		userInfo.user_name = userNameValue;
		userInfo.user_email = emailValue;
		userInfo.password = passwordValue;
		var jsonObj = new Object();
			jsonObj.user_info = userInfo; 
			var jsonStr = JSON.stringify(jsonObj);
			createFile(jsonSTR);	
			var serverRequest = new XMLHttpRequest();
			 serverRequest.onreadystatechange = function() {
    		if (this.readyState == 4 && this.status == 200) {
      				alert("hello " +userNameValue+ "! Welcome to our site!");
    			}
  			};
			serverRequest.open(POST, "./userDetails.json", true);

			serverRequest.send();
	}
	else{
			alert("Please Fill All Values!");
	}	
}

function createFile(jsonSTR : String){
		var fs = require("fs");
		fs.writeFile("./userDetails.json", jsonSTR, (err) => {
   	    if (err) {
        		console.error(err);
        		return;
    	};
    	console.log("File has been created");
    	});
} 
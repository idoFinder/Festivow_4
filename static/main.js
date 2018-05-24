
function submitLogin(){
	var email = document.getElementById("user-email").value;
	var password = document.getElementById("user-password").value;

	var userInfo=new Object();
	userInfo.user_password = password;
	userInfo.user_mail = email;
	var userPackage = new Object();
	userPackage.user_info = userInfo;
	var userStr = JSON.stringify(userPackage);
	postData('./', userStr);
}

function postData(url, data) {
  // Default options are marked with *
  console.log(url);
  return fetch(url, {
	method: 'POST', // *GET, POST, PUT, DELETE, etc.
    headers: {
      'Accept': 'application/json, text/plain, */*', 
      'Content-Type': 'application/json',
    },
    
      body: data // must match 'Content-Type' header
  })
  .then(response => response.json()) // parses response to JSON
  .then(data => console.log(data))
  .catch(error => console.error(error))
}
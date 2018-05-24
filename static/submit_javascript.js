// Submit form with id function.
function submit_by_id() {
var name = document.getElementById("name").value;
console.log(name);
var password = document.getElementById("password").value;
console.log(password);
var email = document.getElementById("email").value;
console.log(email);
//if (validation()) // Calling validation function
//{
var userInfo = new Object();
userInfo.user_name = name;
userInfo.user_password = password;
userInfo.user_email = email;
var userPackage = new Object();
userPackage.user_info = userInfo; 
var userStr = JSON.stringify(userPackage);
postData('./register', userStr);
//alert(userStr);
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
  .catch(error => console.error(error));
}

function treatWithJson(data){
  Object status = JSON.parse(data);
  if(status.valid === true){
    alert("Registration is Valid");
  }
  if(status.valid === false){
    alert("Registration is not Valid");
  }
}

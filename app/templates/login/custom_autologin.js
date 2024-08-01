const urlParams = new URLSearchParams(window.location.search);
const login = urlParams.get('login');
const password = urlParams.get('password');
console.log(`login=${login} password=${password}`);
document.querySelector("#loginInput").value = login;
document.querySelector("#inputPassword").value = password;
document.querySelector("#login-button").click();
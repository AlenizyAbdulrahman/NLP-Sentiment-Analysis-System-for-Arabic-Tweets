function checkPassword(){
    let password = document.getElementById("password").value;
    
    let Confirm_password = document.getElementById("Confirm_password").value;
    let username = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    console.log(username,email,password,Confirm_password);

    let message = document.getElementById("message");
    
    if(username.length == 0){
        alert("اسم المستخدم لايمكن ان يكون فارغ!")
        return false;
    }else{
        if(email.length == 0){
            alert("الايميل لايمكن ان يكون فارغ!")
            return false;
        }
    }
    
    if(password.length != 0){
        if(password == Confirm_password){
            window.location = "index.html";
            
        }else{
            message.textContent = "كلمة السر غير متطابقة!";
        }
    }else{
        alert("كلمة المرور لايمكن ان تكون فارغة!")
    }

}
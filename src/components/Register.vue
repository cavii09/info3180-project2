<template>
   <h1 class="page header">Register New User</h1>
    <div class="form">
      <form id="Register"> 

      <div>
       <label class="username" for="username">Username</label>
       <input type="text" id="username" name="username" class="form-control car-form">
       </div> 

       <label class="password" for="password">Password</label>
       <input type="text" id="password" name="password" class="form-control car-form">
       
       <label class="name" for="name">Fullname</label>
       <input type="text" id="name" name="name" class="form-control car-form"><br>

       <label class="email" for="email">Email</label>
       <input type="text" id="email" name="email" placeholder="youremail@gmail.com" class="form-control car-form">

       <label class="location" for="location">Location</label>
       <input type="text" id="location" name="location" class="form-control car-form">

       <label class="biography" for="biography">Biography</label>
       <input type="text" id="biography" name="biography" class="form-control car-form">

        <label class="photo" for="photo">Photo</label>
       <input type="file" id="photo" name="photo" class="form-control car-form">
       
       <button @click="registerUser" class="btn btn-primary mb-2" id="register" name="register">Register</button>
      </form> 
   </div>
      
</template>

<script>
export default {
      data() {
        return {csrf_token: '',
        username:'',
        password: '',
        name: '',
        email: '',
        location: '',
        biography: '',
        photo: '', 
        flashMessage: '',
        displayFlash: false,
        isSuccess: false,
        alertSuccessClass: 'alert-success',
        alertErrorClass: 'alert-danger',}
      },
      
     
      methods: { carRegister(){
      
      let register = document.getElementById('Register');
      let form_data = new FormData(register);
      
        this.displayFlash = true;
        this.isSuccess = true;
        this.flashMessage = 'You are register successfully!'; 

      fetch("/api/register", {
       method:'POST',
       body: form_data,
       headers: {
          'X-CSRFToken': this.csrf_token
       }  
      })
        .then(function (response) {
           return response.json();
        })
        .then(function (data) {
         // display a success message
           console.log(data);
        })
        .catch(function (error) {
           console.log(error);
        })
      }, 
         getCsrfToken() {
         let self = this;
         fetch('/api/csrf-token')
         .then((response) => response.json())
         .then((data) => {
           console.log(data);
           self.csrf_token = data.csrf_token;
          })
         },  
         
      }       
};

</script>
<style> 
.car-form{
   width: 350px;
}
</style>

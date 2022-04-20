<template>
    <form id="CarForm"> 
    <div>
       <label class="username" for="username">Username</label>
       <input type="text" id="username" name="username"><br>

       <label class="password" for="password">Password</label>
       <input type="text" id="password" name="password"><br>
       
       <label class="name" for="name">Fullname</label>
       <input type="text" id="name" name="name"><br>

       <label class="email" for="email">Email</label>
       <input type="text" id="email" name="email"><br>

       <label class="location" for="location">Location</label>
       <input type="text" id="location" name="location"><br>

       <label class="biography" for="biography">Biography</label>
       <input type="text" id="biography" name="biography"><br>

        <label class="photo" for="photo">Photo</label>
       <input type="file" id="photo" name="photo"><br>
       <button class="btn btn-primary mb-2" id="register" name="register">Register</button>
    </div>
        </form>
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
        photo: '', }
      },
      
      created() {
          this.getCsrfToken();
      },
      methods: { carRegister(){
      
      let carForm = document.getElementById('CarForm');
      let form_data = new FormData(carForm);
        
      fetch("/api/upload", {
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

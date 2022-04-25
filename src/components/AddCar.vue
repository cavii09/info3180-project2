<template>
   <h1 class="page header">Add New Car</h1> <br>
    <div class="form">
      <form id="CarForm"> 

      <div>
       <label class="make" for="make">Make</label>
       <input type="text" id="make" name="make" class="form-control car-form">
       </div> 

       <label class="model" for="model">Model</label>
       <input type="text" id="model" name="model" class="form-control car-form">
       
       <label class="colour" for="colour">Colour</label>
       <input type="text" id="colour" name="colour" class="form-control car-form"><br>

       <label class="email" for="year">Year</label>
       <input type="text" id="year" name="year" placeholder="0000" class="form-control car-form">

       <label class="price" for="price">Price</label>
       <input type="text" id="price" name="price" class="form-control car-form">

       <label class="cartype" for="cartype">CarType</label>
       <input type="text" id="cartype" name="cartype" class="form-control car-form">

       <label class="teansmission" for="transmission">Transmission</label>
       <input type="text" id="transmission" name="transmission" class="form-control car-form">
       
       <label class="description" for="description">Description</label>
       <input type="text" id="description" name="description" class="form-control car-form">

        <label class="photo" for="photo">Photo</label>
       <input type="file" id="photo" name="photo" class="form-control car-form">
       
       <button @click="registerUser" class="btn btn-primary mb-2" id="save" name="save">Save</button>
      </form> 
   </div>
      
</template>

<script>
export default {
      data() {
        return {csrf_token: '',
        make:'',
        model: '',
        colour: '',
        year: '',
        price: '',
        type: '',
        transmission: '',
        photo: '', 
        flashMessage: '',
        displayFlash: false,
        isSuccess: false,
        alertSuccessClass: 'alert-success',
        }
      },
      
      methods: { carRegister(){
      
      let addCar = document.getElementById('AddCar');
      let form_data = new FormData(addCar);
      
        this.displayFlash = true;
        this.isSuccess = true;
        this.flashMessage = 'You successfully Added a New Car!'; 

      fetch("/api/addcar", {
       method:'POST',
       body: form_data,
       headers: {
          'X-CSRFToken': this.csrf_token
       }  
      })
        .then(function (response) {
           return response.json();
        })
        .then(() => {
         // display a success message
           console.log("worked success")
           this.$router.push({name: 'home'})
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
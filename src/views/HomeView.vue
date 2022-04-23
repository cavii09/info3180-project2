<script>
import CarForm from '@/components/CarForm.vue';


export default {
    data() {
        return {
            message: "Hello World! This is Lab 7"
        };
    },
}
</script>

<template>
    <div class="container">
      <div class="text-center">
        <div id="text">
          <h1>Buy and Sell <br> Cars Online</h1>
          <p>United Auto Sales provides the fastest easitest friendly way to buy or sell cars online. Find a Great Price on the Vehicle on the Vehicle You want. </p>
        <button class="btn btn-primary mb-2" id="register" name="register">Register</button>
        <button class="btn btn-primary mb-2" id="login" name="login">Login</button>
        <img alt="Vue logo" class="logo" src="uploads/Carimg.png" width="125" height="125" />
      </div>
    </div>
    </div>
</template>

<style>
/* Add any component specific styles here */
h1{
  margin-right: 150px;
  float:left;
  display: flex;
  align-items: center;
  justify-content: center;
}
p{
  margin-right: 150px;
  padding: 50px;
  float:left;
}
 button{
   float: left;
 }

img {
  height: 50%;
  width: 50%;
  padding-bottom: 50%;
  float: right;
}
.text{
  display: flex;
  align-items: center;
  justify-content: center;

}
</style>
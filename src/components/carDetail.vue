<template>
<div class="individual">
    <div class="images">
        <img class = "car-images" src = "{{ url_for('get_images', filename=property.photo) }}" alt ="Property photos"> 
    </div>
    <div class="aside">
        <h2 class="title">{{ car.year}} {{car.make}}</h2>
        <p class="model">{{ car.model }}</p>
      
        <div class="center">
        <p class="description">{{ car.description }}</p>
        <p class="price">{{ car.price }}</p>
        </div>

         
        <div class="cartype">
        <p class="car_type"> {{ car.car_type }} </p>
        <p class="color"> {{ car.color }} </p>
        </div>
      
        <p class="transmission">{{ car.transmission }}</p>

        <button class="btn">Email Owner</button>
        <button :class='{button: button, active:active}' type ="submit" id='heart' @click.prevent="fav"></button>
        
    </div>    
</div>    
</template>
<script>
export default{
    data() {
        return{}
        
    },
}
</script>


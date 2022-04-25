<template>


<section id="exploring">
    <h3>Explore</h3>

    <form @submit.prevent="searchCar" id="searchForm">
            <div class="row">
                <div class="form-group col-md-5">
                    <label for="make">Make</label>
                    <input type="text"  v-model="searchMake" class="form-control" name="make" id="make" >
                </div>
                <div class="form-group col-md-5">
                    <label for="model">Model</label>
                    <input type="text" v-model="searchModel"  class="form-control" id="model" name="model">
                </div>
                <div class="col-auto">
                    <button class="btn btn-success">Search</button>
                </div>
                
            </div>
             <p>You are searching for <b>Make: </b> {{ searchMake }}  <b>Model: </b> {{searchModel}}</p>
    </form>

    <div id="carsCard">
        <div v-for= "car in cars" class="card">
            <img class="card-img-top" v-bind:src= car.photo v-bind:alt=car.car_type>
            <div class="card-body">
                <section class="card-title"> <span>{{ car.year }} {{car.make}}</span> <span id="pricespan"><img src="../assets/price-tag.png" /> {{car.price}}</span></section>
                <p class="card-text">{{car.model}}</p>
                <button class="cardbtn btn-primary" > <RouterLink :to="{path: '/cars/'+ car.id}" class="nav-link ">view more details</RouterLink> </button>
            </div>
        </div>
    </div>

</section>

</template>

<script>
export default {
    data() {
        return {
            cars: [],
            searchMake: '',
            searchModel: ''
        };
    },
    methods: {
        searchCar(){
            let searchForm = document.getElementById('searchForm');
            let self = this;
            fetch('/api/search?searchmake='+self.searchMake + '&searchmodel=' + self.searchModel , {
                method: 'GET',
                headers: {
                    "Accept": "application/json",
                    'Authorization': `Bearer ${sessionStorage.getItem('token')}`
                }
              })
              .then((response)=>{
                  return response.json();
              })
              .then((data)=>{
                console.log(data);
                self.cars = data;
              })
        },
    
    },
    created() {
        let self = this;
        fetch('/api/cars',
        {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
                'Authorization': `Bearer ${sessionStorage.getItem('token')}`
            }
        })
        .then(function(response) {
            return response.json();
        })
        .then(function(data) {
            console.log(data);
            self.cars = data;
        });
    },
};
</script>

<style>
section#exploring{
    width: 70%;
    display: flex;
    flex-flow: column wrap;
    margin: auto;
}
form#searchForm{
    padding:2em;
    margin-top: 2em;
    box-shadow: rgba(0, 0, 0, 0.4) 0px 2px 4px, rgba(0, 0, 0, 0.3) 0px 7px 13px -3px, rgba(0, 0, 0, 0.2) 0px -3px 0px inset;
}
div.row{
    align-items: center;
    justify-content: center;
}
form button{
    margin-top: 1em;
}
div#carsCard{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-column-gap: 2em;
    width: 100%;
    margin-top: 2em;
    justify-content: center;
    justify-items: center;
    align-content: center;
    align-items: center;
}
div.card{
    width: 100%;
}
section.card-title{
    display: flex;
    flex-flow: row wrap;
}
span#pricespan{
    background: #41B883;
    color: #fff;
    margin-left: 1em;
    width: fit-content;
    padding: 0.05em 0.3em 0.05em 0.3em;
    border-radius: 0.5em;
}
span#pricespan img{
    width: 1em;
}
button a{
  color: #fff !important;
  padding:0;
  margin: 0;
}
button.cardbtn{
    padding:.05em;
    border-radius: .5em;
    width: 100%;
    margin-top: 2rem;
}
h3{
    font-weight: bold;
}
</style>
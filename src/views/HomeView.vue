<template>
      <div class="container">
        <div class="row d-flex align-items-center">

          <div class="col text-center">
            <div class="container col-md-6 col-lg-6 col-xl-9 col-xxl-8">

              <h1>{{ message }}</h1>
              <p class="text-muted">
                United Auto Sales provides the  fastest, easiest and most user friendly way
                to buy or sell cars online. Find a great price on the vehicle you want.
              </p>
              <div class="button-group d-flex">
                <div class="pe-3 page-nav">

                  <a href="#" class="btn btn-primary" >Register</a>
                </div>
                
                <div class="page-nav">
                  <a href="#" class="btn btn-success">Login</a>
                </div>
              </div>
            </div>

          </div>
          <div class="col">
            <img src="@/assets/photo-landingPage.jpeg" alt=""  id="landingPageImage" class="d-inline-block">
          </div>
        </div>
      </div>
</template>

<script>
export default {
    data() {
        return {
            message: "Buy and Sell Cars Online"
        };
    },
}
</script>


<style>
#landingPageImage{
  width: 40rem;
  height: 60rem;

}

a{
  width: 100%;
}

.page-nav{
  width: 10rem;
}
</style>

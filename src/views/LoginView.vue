<template>
  <div class="about container">
    <h2>Login to your Account</h2>
    <Login/>
  </div>
</template>
<script>
import Login from "../components/Login.vue";
export default {
    data() {
        return {
            message: "Login!"
        };
    },
    components: { Login }
};
</script>

<style>
</style>

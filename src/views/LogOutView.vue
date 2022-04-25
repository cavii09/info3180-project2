<template>
  <div>
    <Login/>
  </div>
</template>
<script>
import Logout from "../components/Logout.vue";
export default {
    data() {
        return {
            message: "Logout!"
        };
    },
    components: { Logout }
};
</script>

<style>
</style>

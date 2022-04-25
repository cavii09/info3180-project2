<template>
    <form method="POST" id="login">
        <div class="login_name">
            <label for="username">Username</label>
            <input type="text" class="login-control"/>
        </div>

        <div class="login_word">
            <label for="password">Password</label>
            <input type="password" class="login-control"/>
        </div>

        <button @click="registerUser" class="btn btn-primary mb-2" id="user" name="login">Login</button>
    </form>
</template>

<script>
    export default{
        data(){
            return {}
        }
    }
</script>
<style>
</style>

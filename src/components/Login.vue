<template>
    <form method="POST" id="login">
        <h2>Login to your account</h2>
        <div class="login_name">
            <label for="username">Username</label>
            <input type="text" class="login-control"/>
        </div>

        <div class="login_word">
            <label for="password">Password</label>
            <input type="password" class="login-control"/>
        </div>

        <button type="submit" class="btn btn-green btn-lg btn-block">Login</button>
    </form>
</template>

<script>
    export default{
        data(){
            return {}
        }
    }
</script>
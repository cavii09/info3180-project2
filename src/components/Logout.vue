<template>

<div class="container col-md-6">
    <div id="notification">
    </div>

     <div id="notificationFormError" >
        <ul v-for="(error,index) in notifyErrorArray" :key="index" >
            {{error}}
        </ul>
    </div>
</div>
    
</template>
<script>
import router from '../router'
export default {
    data() {
        return{
            csrf_token:'',
            notifySuccess:'',
            notifyErrorArray:[]
        }
        
    },
    created(){
        console.log(this.csrf_token)
        this.getCsrfToken();
        
        fetch('/api/auth/logout',{
                method:"GET",
                headers:{
                    'X-CSRFToken': this.csrf_token
                }  
                
            }).then(async (response) =>{
                let data = await response.json();
                let status = response.status;
                console.log(data)
                switch(status){
                    case 200:
                        localStorage.removeItem('userId');
                        notification.textContent = this.notifySuccess;
                        notification.style.display = 'block';
                        notification.classList.add('bg-success');
                        setTimeout( function(){
                            window.location.href = '/';
                            },1000);
                        break;
                    
                    case 400:
                        if (Array.isArray(data.error)){
                            this.notifyErrorArray = data.error;
                            notificationFormError.style.display = 'block';
                            notificationFormError.classList.add('bg-danger');
                        }
                        break;
                    default:
                        notification.textContent= this.data;
                        notification.style.display = 'block';
                        notification.classList.add('bg-danger');
                }
            })
            .catch((error)=>{
                console.log(error);
                this.notifySuccess = error;
                notification.textContent = this.notifySuccess;
                notification.style.display = 'block';
                notification.classList.add('bg-danger');
            })
    },
    methods:{
               
        getCsrfToken(){
            fetch('/api/csrf-token')
            .then(response => response.json())
            .then(responseData =>{
                this.csrf_token = responseData.csrf_token;
            })
        },
    }
}
</script>

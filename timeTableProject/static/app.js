

new Vue({
    el:'#table_app',
    data: {
    table: []
    },
    created: function(){
        const vm = this;
        axios.get('/api/table/')
        .then(function(response){
        console.log(response.data)
        })
    }
}

)
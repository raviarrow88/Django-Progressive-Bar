$(document).ready(function(){

$('#progress-wrapper').hide();
$('.progress').hide();
$('.msg').hide();
$("#btn").on('click',function(){
var user_count = $('#user_num').val()
var task_url = ''
var bar,barMessage = ''
var url = '/create_users/'
var data = new FormData()
data.set('count', user_count)
fetch(url,{
  method:"POST",
  body:data

})
.then(function(res){return res.json()})
.then(function(response){
  console.log(response['task_id'])

  var task_id = response['task_id']
  task_url = '/state/'+task_id
  taskprogress()

}).catch(err=>{console.log('ERR',err)
})


function taskprogress(){
  fetch(task_url)
  .then(function(resp){return resp.json()})
  .then(function(response){
    console.log(response)

    $('#progress-wrapper').show()
    $('.progress').show()
    $('.msg').show();
    
    bar = document.getElementById('pbar')
    barMessage = document.getElementById("progress-bar-message");



    if (response['state'] != 'SUCCESS'){
      if (response['meta_info'] !== null ){
      bar.style.width = response['meta_info']['percent'] + "%";
      bar.textContent = response['meta_info']['percent'] + '%' + ' Completed! ';
      barMessage.innerHTML = response['meta_info']['done'] + ' of ' + response['meta_info']['total'] + ' processed,' + response['meta_info']['percent'] + '%'   ;

  }

  setTimeout(taskprogress,2000)

  }


  }).catch(err=>{
    console.log('ERR',err)
  })
}

// fetch the api to pause/resume the worker process

})

})

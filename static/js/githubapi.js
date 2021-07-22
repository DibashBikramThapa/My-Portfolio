fetch('https://api.github.com/users/DibashBikramThapa')
  .then(response => response.json())
  .then(function(data){

    document.getElementById('github').textContent='Github link'
    document.getElementById('github').href=data['html_url']
    document.getElementById('list').textContent='My projects:'
    document.getElementById('list').href=data['html_url']

})

fetch('https://api.github.com/users/DibashBikramThapa/repos')
  .then(response => response.json())
  .then(
    function gitclick(data){
      for (let i = 0; i<=data.length; i++){
        document.getElementById(i+1).text=data[i]['name'];
        document.getElementById(i+1).href=data[i]['html_url'];}


    })

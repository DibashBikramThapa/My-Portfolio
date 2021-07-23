fetch('https://api.github.com/users/DibashBikramThapa')
  .then(response => response.json())
  .then(function(data){

    document.getElementById('list').textContent='My github projects!:'
    document.getElementById('list').href=data['html_url']

})

fetch('https://api.github.com/users/DibashBikramThapa/repos')
  .then(response => response.json())
  .then(
    function gitclick(data){
      document.getElementById('1').textContent=data[0]['name']
        document.getElementById('1').href=data[0]['html_url']

        document.getElementById('2').textContent=data[1]['name']
          document.getElementById('2').href=data[1]['html_url']

        document.getElementById('3').textContent=data[2]['name']
        document.getElementById('3').href=data[2]['html_url']

        document.getElementById('4').textContent=data[3]['name']
        document.getElementById('4').href=data[3]['html_url']

        document.getElementById('5').textContent=data[4]['name']
        document.getElementById('5').href=data[4]['html_url']

    })

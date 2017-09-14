
function initialize() {
    if (typeof(Storage) !== "undefined") {
       sessionStorage.facebook_done=false;
       sessionStorage.location_done=false;
      
    } else {
        console.log('localstorage not supported')
    }
     if (localStorage.state){
      // if location has already been set
        sessionStorage.location_done=true
        if (sessionStorage.facebook_done == true && sessionStorage.location_done == true){
              $('.js-votebtn').css('display','inline')
            }
     }
     else{
    
          if (navigator.geolocation) {
              navigator.geolocation.getCurrentPosition(showPosition, showError);
          } else {
              console.log("Geolocation is not supported by this browser.")  ;
          }
        }

}
function showPosition(position) {
    console.log("Latitude: " + position.coords.latitude + 
    "<br>Longitude: " + position.coords.longitude);
    resolveLocation(position.coords.latitude, position.coords.longitude);
    sessionStorage.location_done=true
    if (sessionStorage.facebook_done == true && sessionStorage.location_done == true){
          $('.js-votebtn').css('display','inline')
        }
}

var geoOptions = {
      enableHighAccuracy: true,
      maximumAge: 30000,
      timeout: 27000
      };

function resolveLocation(lat, long){
       var geocoder;
    geocoder = new google.maps.Geocoder();
    var latlng = new google.maps.LatLng(lat, long);

    geocoder.geocode(
        {'latLng': latlng}, 
        function(results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
                //console.log(results)
                if (results[0]) {
                    var add= results[0].formatted_address ;
                    var  value=add.split(",");

                    count=value.length;
                    country=value[count-1];
                    state=value[count-2];
                    city=value[count-3];
                    localStorage.state=state
                }
                else  {
                    console.log ("address not found");
                }
            }
            else {
                console.log( "Geocoder failed due to: " + status);
            }
        }
    );
}   



function showError(error) {
    switch(error.code) {
        case error.PERMISSION_DENIED:
           console.log ( "User denied the request for Geolocation.")
            break;
        case error.POSITION_UNAVAILABLE:
            console.log( "Location information is unavailable.")
            break;
        case error.TIMEOUT:
            console.log( "The request to get user location timed out.")
            break;
        case error.UNKNOWN_ERROR:
            console.log( "An unknown error occurred.")
            break;
    }
}



$('.js-votebtn').click(function(){
	console.log('yes')
	 poll_id=$('#poll_id').val()

	$.get( "/api/vote/", { id: poll_id, choice: $("input[name=choice]:checked").val() , state:localStorage.state} , function(data, status){})
	  .done(function( data ) {
      if (data.login){
    	  if(data.done){

            if (data.has_already_voted){
              alert('User has already voted, you cant vote twice')
            }
            else{
            alert('sucessfull vote')
          }
          }
          else{
            console.log(data)

            if (data.cant_vote){
            alert( "The user is not qualified to vote" );
          }


          }
      }
      else{
        $("#login").modal("show");

      }
	  })
	  .fail(function() {
	    alert( "The server is experiencing some problem, Please try again later" );
	  })

      return false;
})
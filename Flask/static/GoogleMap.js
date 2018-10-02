var geocoder;
var map;
var marker;

/* Init the map and the basics functions: geocode, marker */
function initMap() {
  geocoder = new google.maps.Geocoder();
  map = new google.maps.Map(document.getElementById('map'), {
      center: {lat: 48.8747613, lng: 2.348376}, /* center on Paris, the French's capital */
      zoom: 16,
      mapTypeId: 'terrain'
  });
  marker = new google.maps.Marker({
      map: map,
      draggable: false,
      animation: google.maps.Animation.BOUNCE,
      position: {lat: 48.8747613, lng: 2.348376},
      title: "Marker de Papy"
  });
}

function placeMarker(location) {
    if (marker) {
        /* If marker already was created change positon */
        marker.setPosition(location);
    } else {
        /* Create a marker */
        marker = new google.maps.Marker({
            position: location,
            map: map,
            draggable: false,
            animation: google.maps.Animation.DROP
        });
    }
}

/*  Main function that locate what is entered in the input */
function codeAddress() {
    var address = document.getElementById('research').value;
    geocoder.geocode( { 'address': address}, function(results, status) {
    if (status == 'OK') {
        var audio = new Audio('/static/notif.wav');
        audio.play();
        var here = results[0].formatted_address
        map.setCenter(results[0].geometry.location);
        placeMarker(results[0].geometry.location);
        $("#address").text(here);
        } else {
        $("#know_it").text("Ca m'dit rien tout ça, t'es sûr qu'c'est sur terre mon gamin ?");
        $("#address").text("");
        }
    });
}

/* Run the initMap function once the div '#map' is fully loaded in the browser */
$('#map').ready(function() {
    initMap();
});

//Resize Function
		google.maps.event.addDomListener(window, "resize", function() {
			var center = map.getCenter();
			google.maps.event.trigger(map, "resize");
			map.setCenter(center);
		});
function initMap(){
  map = new google.maps.Map(document.getElementById("map"), {
      center: { lat: 36.605816, lng: 34.310164 },
      zoom: 15,
    });
}

navigator.geolocation.getCurrentPosition(oldu);

function oldu(position){
  var infoWindow = new google.maps.InfoWindow();
  // var marker = google.maps.marker({
  //     position:{lat: konum.coords.latitude, lng: konum.coords.longitude},
  //     map:map
  // });
  const pos = {
      lat: position.coords.latitude,
      lng: position.coords.longitude,
    };
    
  infoWindow.setPosition(pos);
  infoWindow.setContent("Location found.");
  infoWindow.open(map);
  map.setCenter(pos);


}


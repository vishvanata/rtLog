$(document).ready(function() {
    $.ajax({
        url: "http://ravinata.mynetgear.com:70/ListAll"
    }).then(function(data) {
       $('.createdatatime').append(data.createdatatime);
       $('.current_latitude').append(data.current_latitude);
       $('.current_longitude').append(data.current_longitude);
       $('.description').append(data.description);
       $('.lastupdatetime').append(data.lastupdatetime);
    });
});

$("#results").hide();
// Search Address
$("#search_weather").on("click", function(event) {
    event.preventDefault();
    var city_name = $("#city_name").val();
    $.ajax({
        url: "",
        type: "POST",
        data: {
            city_name: $("#city_name").val(),
            csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
        },

        success: function(json) {
            $("#results").html(
                "<div class='card-body'><h3>" +
                city_name +
                "</h3><h5 class='mt-0'>" +
                json.summary +
                "</h5><p><strong>Temperature</strong>: " +
                json.temperature +
                "F</p></div>"
            );

            $("#results").show();
            $("#display-weather").hide();
        },

        error: function(xhr, errmsg, err) {
            $("#results").html(
                "<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " +
                errmsg +
                " <a href='#' class='close'>&times;</a></div>"
            );
            console.log(xhr.status + ": " + xhr.responseText);
        }
    });
});

// Save weather data to the database
$("#saved_to_db").hide();
var city_name = $("#city_name").val();
// Search Address
$("#save_weather").on("click", function(event) {
    event.preventDefault();
    $.ajax({
        url: "save-weather/",
        type: "POST",
        data: {
            city_name: $("#city_name").val(),
            csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
        },

        success: function(json) {
            $("#saved_to_db").show();
            $("#saved_to_db")
                .delay(5000)
                .fadeOut(400);
            console.log("success");
        },

        error: function(xhr, errmsg, err) {
            $("#results").html(
                "<div class='alert-box alert radius' data-alert'>Oops! We have encountered an error: " +
                errmsg +
                "</div>"
            );
            console.log(xhr.status + ": " + xhr.responseText);
        }
    });
});

// Retrieve data from the database
$(document).on("click", "#retrieve_weather", function(event) {
    event.preventDefault();
    var displayWeather = $("#display-weather");

    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:8000/retrieve-weather",

        success: function(result) {
            var output = "<div class='row'>";
            for (var i in result) {
                output +=
                    "<div class='col-md-4'><div class='card mb-4 shadow-sm'><div class='card-body'><h3>" +
                    result[i]["fields"].city_name +
                    "</h3><h5 class='mt-0'>" +
                    result[i]["fields"].summary +
                    "</h5><p><strong>Temperature</strong>: " +
                    result[i]["fields"].temperature +
                    "F</p></div></div></div>";
            }
            output += "</div>";

            displayWeather.html(output);

            $("#display-weather").show();
            $("#results").hide();
        }
    });
});
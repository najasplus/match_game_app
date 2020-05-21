var id_array = [];

var correct_words = 0;
var total_words = document.getElementsByClassName("button_gamefield");  

function register_click(clicked_id) {
    setColor(clicked_id, "darkgreen");
    id_array.push(clicked_id);
    if (id_array.length == 2) {
        check_match(id_array);
        id_array = [];
    }
}

function setColor(clicked_id, color){
    var property = document.getElementById(clicked_id);
    property.style.backgroundColor = color;
}

function correctlyGuessedButton(clicked_id){
    var property = document.getElementById(clicked_id);
    setColor(clicked_id, "orange");
    property.disabled = true;
    correct_words += 1;

    if (correct_words == total_words.length) {
        declareVictory()
    }
}

function revertColor(clicked_id){
    setColor(clicked_id, "darkslategrey");
}

function check_match(id_array) {
    var match = (Math.abs(id_array[0] - id_array[1]) == 1000);
    for (var i = 0; i < 2; i++) {
        if (match == true) {
            correctlyGuessedButton(id_array[i]);
        } else {
            revertColor(id_array[i])
        }
    }
}

function declareVictory() {
    var modal = document.getElementById("myModal");
    modal.style.display = "block";
    // When the user clicks anywhere outside of the modal, close it
  
}

function close_and_restart(id) {
    var modal = document.getElementById("myModal");
    modal.style.display = "none";
    location.reload();
}

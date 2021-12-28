var calendar = document.getElementById("tableContainer");
var gridTable = document.getElementById("tableBody");
var currentDate = new Date();
var selectedDate = currentDate;
var selectedDayBlock = null;

function createCalendar(date, side) {
  var currentDate = date;
  var startDate = new Date(currentDate.getFullYear(), currentDate.getMonth(), 1);

  var yearTitle = document.getElementById("year-name");
  var monthTitle = document.getElementById("month-name");

  var monthName = currentDate.toLocaleString("ita-IT", {
    month: "short"
  });
  var yearNum = currentDate.toLocaleString("ita-IT", {
    year: "numeric"
  });
  yearTitle.innerHTML = `${yearNum}`;
  monthTitle.innerHTML = `${monthName}`;

  if (side == "left") {
    gridTable.className = "animated fadeOutRight";
  } else {
    gridTable.className = "animated fadeOutLeft";
  }

  gridTable.innerHTML = "";

  var newTr = document.createElement("div");
  newTr.className = "row";
  var currentTr = gridTable.appendChild(newTr);

  for (let i = 1; i < startDate.getDay(); i++) {
    let emptyDivCol = document.createElement("div");
    emptyDivCol.className = "col empty-day";
    currentTr.appendChild(emptyDivCol);
  }

  var lastDay = new Date(currentDate.getFullYear(), currentDate.getMonth() + 1, 0);
  lastDay = lastDay.getDate();

  for (let i = 1; i <= lastDay; i++) {
    if (currentTr.getElementsByTagName("div").length >= 7) {
      currentTr = gridTable.appendChild(addNewRow());
    }
    let currentDay = document.createElement("div");
    currentDay.className = "col"; // div giorno della settimana
    if (selectedDayBlock == null && i == currentDate.getDate() || selectedDate.toDateString() == new Date(currentDate.getFullYear(), currentDate.getMonth(), i).toDateString()) {
      selectedDate = new Date(currentDate.getFullYear(), currentDate.getMonth(), i);

      document.getElementById("selectedDay").innerHTML = selectedDate.toLocaleString("it", {
        month: "short",
        day: "numeric",
        year: "numeric"
      });

      selectedDayBlock = currentDay;
      setTimeout(() => {
        currentDay.classList.add("activeDay");
        currentDay.classList.add("dayHover");
      }, 900);
    }
    currentDay.innerHTML = i;
    currentTr.appendChild(currentDay);
  }

  for (let i = currentTr.getElementsByTagName("div").length; i < 7; i++) {
    let emptyDivCol = document.createElement("div");
    emptyDivCol.className = "col empty-day";
    currentTr.appendChild(emptyDivCol);
  }

  setTimeout(() => {
    if (side == "left") {
      gridTable.className = "animated fadeInLeft";
    } else if (side == "right") {
      gridTable.className = "animated fadeInRight";
    } else {
      gridTable.className = "animated fadeIn";
    }
  }, 270);

  function addNewRow() {
    let node = document.createElement("div");
    node.className = "row";
    return node;
  }
}

createCalendar(currentDate);

var prevMonthButton = document.getElementById("prevMonth");
var nextMonthButton = document.getElementById("nextMonth");

var prevYearButton = document.getElementById("prevYear");
var nextYearButton = document.getElementById("nextYear");

prevMonthButton.onclick = changeMonthPrev;
nextMonthButton.onclick = changeMonthNext;

prevYearButton.onclick = changeYearPrev;
nextYearButton.onclick = changeYearNext;

function changeMonthPrev() {
    currentDate = new Date(currentDate.getFullYear(), currentDate.getMonth() - 1);
    createCalendar(currentDate, "left");
}

function changeMonthNext() {
    currentDate = new Date(currentDate.getFullYear(), currentDate.getMonth() + 1);
    createCalendar(currentDate, "right");
}

function changeYearPrev() {
    var year_selected = document.getElementById('year-name').innerText;
    var currentYear  = new Date().getFullYear();
    if (parseInt(year_selected) > currentYear){
        currentDate = new Date(currentDate.getFullYear() - 1, currentDate.getMonth());
        createCalendar(currentDate, "down");
    }
}

function changeYearNext() {
    var year_selected = document.getElementById('year-name').innerText;
    var currentYear  = new Date().getFullYear();
    if (year_selected == currentYear){
        currentDate = new Date(currentDate.getFullYear() + 1, currentDate.getMonth());
        createCalendar(currentDate, "up");
        }
}

gridTable.onclick = function (e) {

  if (!e.target.classList.contains("col") || e.target.classList.contains("empty-day")) {
        return;
  }

  if (selectedDayBlock) {
    if (selectedDayBlock.classList.contains("activeDay") && selectedDayBlock.classList.contains("dayHover")) {
      selectedDayBlock.classList.remove("activeDay");
      selectedDayBlock.classList.remove("dayHover");
    }
  }
  selectedDayBlock = e.target;
  selectedDayBlock.classList.add("activeDay");
  selectedDayBlock.classList.add("dayHover");

  selectedDate = new Date(currentDate.getFullYear(), currentDate.getMonth(), parseInt(e.target.innerHTML));
}

function countUp(){
  var a = document.getElementById("n_adult_passeng").innerHTML
  if (a < 7){
    a = parseInt(a) +1
    document.getElementById("n_adult_passeng").innerHTML = a
    }
}

function countUp2(){
  var a = document.getElementById("n_baby_passeng").innerHTML
  if (a < 6){
    a = parseInt(a) +1
    document.getElementById("n_baby_passeng").innerHTML = a
    }
}

function countDown(){
  var a = document.getElementById("n_adult_passeng").innerHTML;
  if (parseInt(a) > 1 ){
    a = parseInt(a) -1;
    document.getElementById("n_adult_passeng").innerHTML = a;
  }
}

function countDown2(){
  var a = document.getElementById("n_baby_passeng").innerHTML;
  if (parseInt(a) > 0 ){
    a = parseInt(a) -1;
    document.getElementById("n_baby_passeng").innerHTML = a;
  }
}


function postdata() {
  $(".price").remove();
  if (document.getElementById('month-name').innerText == "gen"){var month = "01"};
  if (document.getElementById('month-name').innerText == "feb"){var month = "02"};
  if (document.getElementById('month-name').innerText == "mar"){var month = "03"};
  if (document.getElementById('month-name').innerText == "apr"){var month = "04"};
  if (document.getElementById('month-name').innerText == "mag"){var month = "05"};
  if (document.getElementById('month-name').innerText == "giu"){var month = "06"};
  if (document.getElementById('month-name').innerText == "lug"){var month = "07"};
  if (document.getElementById('month-name').innerText == "ago"){var month = "08"};
  if (document.getElementById('month-name').innerText == "set"){var month = "09"};
  if (document.getElementById('month-name').innerText == "ott"){var month = "10"};
  if (document.getElementById('month-name').innerText == "nov"){var month = "11"};
  if (document.getElementById('month-name').innerText == "dic"){var month = "12"};

  var origin = document.getElementById('origin').value;
  var destination = document.getElementById('destination').value;
  var n_adu = document.getElementById('n_adult_passeng').innerText;
  var n_baby = document.getElementById('n_baby_passeng').innerText;
  var year = document.getElementById('year-name').innerText;
  var atime = document.getElementById('pick_time').value
  var col = document.getElementsByClassName("col");

  let xhttp = new XMLHttpRequest();
  xhttp.onload = function() {
      var json_resp = JSON.parse(xhttp.responseText);

      var items = Object.keys(json_resp).map(function(key) {
              return [key, json_resp[key]];
              });
          items.sort(function(first, second) {
          return second[1] - first[1];
            });
      var green_prices = parseInt(items.pop()[1]);
      for (var i = 0; i < col.length; i++){

          if (col[i].textContent == 1){$(col[i]).append(`<div class="price">${json_resp["01"]}€</div>`)};
          if (col[i].textContent == 2){$(col[i]).append(`<div class="price">${json_resp["02"]}€</div>`)};
          if (col[i].textContent == 3){$(col[i]).append(`<div class="price">${json_resp["03"]}€</div>`)};
          if (col[i].textContent == 4){$(col[i]).append(`<div class="price">${json_resp["04"]}€</div>`)};
          if (col[i].textContent == 5){$(col[i]).append(`<div class="price">${json_resp["05"]}€</div>`)};
          if (col[i].textContent == 6){$(col[i]).append(`<div class="price">${json_resp["06"]}€</div>`)};
          if (col[i].textContent == 7){$(col[i]).append(`<div class="price">${json_resp["07"]}€</div>`)};
          if (col[i].textContent == 8){$(col[i]).append(`<div class="price">${json_resp["08"]}€</div>`)};
          if (col[i].textContent == 9){$(col[i]).append(`<div class="price">${json_resp["09"]}€</div>`)};
          if (col[i].textContent == 10){$(col[i]).append(`<div class="price">${json_resp["10"]}€</div>`)};
          if (col[i].textContent == 11){$(col[i]).append(`<div class="price">${json_resp["11"]}€</div>`)};
          if (col[i].textContent == 12){$(col[i]).append(`<div class="price">${json_resp["12"]}€</div>`)};
          if (col[i].textContent == 13){$(col[i]).append(`<div class="price">${json_resp["13"]}€</div>`)};
          if (col[i].textContent == 14){$(col[i]).append(`<div class="price">${json_resp["14"]}€</div>`)};
          if (col[i].textContent == 15){$(col[i]).append(`<div class="price">${json_resp["15"]}€</div>`)};
          if (col[i].textContent == 16){$(col[i]).append(`<div class="price">${json_resp["16"]}€</div>`)};
          if (col[i].textContent == 17){$(col[i]).append(`<div class="price">${json_resp["17"]}€</div>`)};
          if (col[i].textContent == 18){$(col[i]).append(`<div class="price">${json_resp["18"]}€</div>`)};
          if (col[i].textContent == 19){$(col[i]).append(`<div class="price">${json_resp["19"]}€</div>`)};
          if (col[i].textContent == 20){$(col[i]).append(`<div class="price">${json_resp["20"]}€</div>`)};
          if (col[i].textContent == 21){$(col[i]).append(`<div class="price">${json_resp["21"]}€</div>`)};
          if (col[i].textContent == 22){$(col[i]).append(`<div class="price">${json_resp["22"]}€</div>`)};
          if (col[i].textContent == 23){$(col[i]).append(`<div class="price">${json_resp["23"]}€</div>`)};
          if (col[i].textContent == 24){$(col[i]).append(`<div class="price">${json_resp["24"]}€</div>`)};
          if (col[i].textContent == 25){$(col[i]).append(`<div class="price">${json_resp["25"]}€</div>`)};
          if (col[i].textContent == 26){$(col[i]).append(`<div class="price">${json_resp["26"]}€</div>`)};
          if (col[i].textContent == 27){$(col[i]).append(`<div class="price">${json_resp["27"]}€</div>`)};
          if (col[i].textContent == 28){$(col[i]).append(`<div class="price">${json_resp["28"]}€</div>`)};
          if (col[i].textContent == 29){$(col[i]).append(`<div class="price">${json_resp["29"]}€</div>`)};
          if (col[i].textContent == 30){$(col[i]).append(`<div class="price">${json_resp["30"]}€</div>`)};
          if (col[i].textContent == 31){$(col[i]).append(`<div class="price">${json_resp["31"]}€</div>`)};

      }
      var prices = document.getElementsByClassName('price');
      for (i = 0; i < prices.length; i++) {
        if (prices[i].textContent == `${green_prices}€`){
            prices[i].style.color = '#0aac0a';
            prices[i].style.animation = 'move 4s infinite';
            prices[i].style.position = 'relative';
            prices[i].style.animationDirection = 'alternate'
        }
        if(prices[i].textContent == `999€`){
          prices[i].innerHTML = '/';
        }
      }
  }
  xhttp.open("POST", "/?origin="+origin+"&destination="+destination+"&month="+month+"&year="+year+"&n_adult="+n_adu+"&n_baby="+n_baby+"&atime="+atime, true);
  xhttp.send();
}


function from_stazioni(){
  $("#da_stazioni").remove();
  var letters = document.getElementById('origin').value;
  let xhttp = new XMLHttpRequest();
  xhttp.onload = function() {
     var html = "";
     var j = JSON.parse(xhttp.response);
     for(let n = 0; n < j.length; n++){
         html += `<option value="${j[n].name}">`;
     }
    var dtlst = document.createElement('datalist');
    dtlst.id = "da_stazioni";
    document.getElementById('origin').append(dtlst);
    $('#da_stazioni').append(html);
    }
  if (letters.length > 1){
    xhttp.open("GET", "https://cors-anywhere.herokuapp.com/https://www.lefrecce.it/msite/api/geolocations/locations?name="+letters, true);
    xhttp.send();
  }
}

function to_stazioni(){
    $("#a_stazioni").remove();
    var letters = document.getElementById('destination').value;
    let xhttp = new XMLHttpRequest();
    xhttp.onload = function() {
        var html = "";
        var j = JSON.parse(xhttp.response);
        for(let n = 0; n < j.length; n++){
            html += `<option value="${j[n].name}">`;
        }
    var dtlst = document.createElement('datalist');
    dtlst.id = "a_stazioni";
    document.getElementById('destination').append(dtlst);
    $('#a_stazioni').append(html);
    }
  if (letters.length > 1){
    xhttp.open("GET", "https://cors-anywhere.herokuapp.com/https://www.lefrecce.it/msite/api/geolocations/locations?name="+letters, true);
    xhttp.send();
  }
}

var time_picker = document.getElementById('pick_time');
var clock = document.getElementById('clock');
clock.onclick = function(){
    if (time_picker.style.display == 'none'){
        time_picker.style.display = 'inline-flex';
        }
    }

function bigImg() {
  document.getElementById('clock').style.height = "30px";
  document.getElementById('clock').style.width = "30px";
}

function normalImg() {
  document.getElementById('clock').style.height = "28px";
  document.getElementById('clock').style.width = "28px";
}


var cale = document.getElementById('tableBody')
cale.addEventListener('click', function(){
  var day_sel = document.getElementsByClassName('activeDay')
  var day = day_sel[0].innerText[0]+ day_sel[0].innerText[1]

  var origin = document.getElementById('origin').value;
  var destination = document.getElementById('destination').value;
  var n_adu = document.getElementById('n_adult_passeng').innerText;
  var n_baby = document.getElementById('n_baby_passeng').innerText;
  var year = document.getElementById('year-name').innerText;
  if (document.getElementById('month-name').innerText == "gen"){var month = "01"};
  if (document.getElementById('month-name').innerText == "feb"){var month = "02"};
  if (document.getElementById('month-name').innerText == "mar"){var month = "03"};
  if (document.getElementById('month-name').innerText == "apr"){var month = "04"};
  if (document.getElementById('month-name').innerText == "mag"){var month = "05"};
  if (document.getElementById('month-name').innerText == "giu"){var month = "06"};
  if (document.getElementById('month-name').innerText == "lug"){var month = "07"};
  if (document.getElementById('month-name').innerText == "ago"){var month = "08"};
  if (document.getElementById('month-name').innerText == "set"){var month = "09"};
  if (document.getElementById('month-name').innerText == "ott"){var month = "10"};
  if (document.getElementById('month-name').innerText == "nov"){var month = "11"};
  if (document.getElementById('month-name').innerText == "dic"){var month = "12"};

  var xhttp = new XMLHttpRequest;
  xhttp.onload = function(){

    $(".r").remove();
    var a = JSON.parse(xhttp.response);
    for (var i = 0; i < a.length; i++){
      for( var n = 0; n < a[i].length; n++){
        if (a[i][n].saleable == true && parseInt(moment(a[i][n].departuretime).format("D")) == parseInt(day)){
          var html = `<div class="r"><div class="row">
          <div class="container" style="display: flex; gap: 0.6rem; background: white; border-radius: 10px; border: 1.5px solid blueviolet; width: 100%; flex-wrap: wrap; margin-bottom: 10px; justify-content: space-between; align-items: baseline;">
          <div class="item" style="text-align: center; padding-top: 10px;"><p style="font-weight: 500;">${moment(a[i][n].departuretime).format("H:mm")}</p><p style="font-size: 12.5px; color: grey; ">${a[i][n].origin}</p></div>
          <div class="item" style="color: gray; font-size: 11px; margin-top: 14px; min-width: 30px; ">${a[i][n].duration}h</div>
          <div class="item" style="text-align: center; padding-top: 10px;"><p style="font-weight: 500">${moment(a[i][n].arrivaltime).format("H:mm")}</p><p style="font-size: 12.5px; color: grey; ">${a[i][n].destination}</p></div>
          <div class="item" style="display: contents"><p style="font-size: 10px; color: #494343; margin-left: 8%;">Cambi: ${a[i][n].changesno}</p><p style="font-size: 10px; color: #494343; padding-left: 10px;">${a[i][n].trainlist[0].trainacronym}</p><p style="margin-left: auto; padding-right: 10px; font-weight: 600; ">${a[i][n].originalPrice}€</p></div>
          </div>
          </div></div>`
          $('#resu').append(html)
        }
        
      }
    }
  }
  xhttp.open("POST", "/trains/?origin="+origin+"&destination="+destination+"&day="+day+"&month="+month+"&year="+year+"&n_adult="+n_adu+"&n_baby="+n_baby, true);
  xhttp.send();
  })

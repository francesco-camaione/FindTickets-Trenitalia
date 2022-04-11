function postdata() {
  $(".price").remove();

  if (document.getElementById('month-name').innerText == "Gen") { var month = "01" };
  if (document.getElementById('month-name').innerText == "Feb") { var month = "02" };
  if (document.getElementById('month-name').innerText == "Mar") { var month = "03" };
  if (document.getElementById('month-name').innerText == "Apr") { var month = "04" };
  if (document.getElementById('month-name').innerText == "Mag") { var month = "05" };
  if (document.getElementById('month-name').innerText == "Giu") { var month = "06" };
  if (document.getElementById('month-name').innerText == "Lug") { var month = "07" };
  if (document.getElementById('month-name').innerText == "Ago") { var month = "08" };
  if (document.getElementById('month-name').innerText == "Set") { var month = "09" };
  if (document.getElementById('month-name').innerText == "Ott") { var month = "10" };
  if (document.getElementById('month-name').innerText == "Nov") { var month = "11" };
  if (document.getElementById('month-name').innerText == "Dic") { var month = "12" };

  var origin = document.getElementById('origin').value;
  var destination = document.getElementById('destination').value;
  var n_adu = document.getElementById('n_adult_passeng').innerText;
  var n_baby = document.getElementById('n_baby_passeng').innerText;
  var year = document.getElementById('year-name').innerText;
  var atime = document.getElementById('pick_time').value;
  var frecce = document.getElementById('frecce').value
  var col = document.getElementsByClassName("col");

  if (frecce == 'si') {
    var frecce_bool = 'true'
  } else {
    frecce_bool = 'false'
  }

  let xhttp = new XMLHttpRequest();
  xhttp.onload = function () {
    var json_resp = JSON.parse(xhttp.responseText);
    var items = Object.keys(json_resp).map(function (key) {
      return [key, json_resp[key]];
    });
    items.sort(function (first, second) {
      return second[1] - first[1];
    });
    var green_prices = parseInt(items.pop()[1]);

    for (var i = 0; i < col.length; i++) {
      if (col[i].textContent == 1) { $(col[i]).append(`<div class="price">${json_resp["01"]}€</div>`) };
      if (col[i].textContent == 2) { $(col[i]).append(`<div class="price">${json_resp["02"]}€</div>`) };
      if (col[i].textContent == 3) { $(col[i]).append(`<div class="price">${json_resp["03"]}€</div>`) };
      if (col[i].textContent == 4) { $(col[i]).append(`<div class="price">${json_resp["04"]}€</div>`) };
      if (col[i].textContent == 5) { $(col[i]).append(`<div class="price">${json_resp["05"]}€</div>`) };
      if (col[i].textContent == 6) { $(col[i]).append(`<div class="price">${json_resp["06"]}€</div>`) };
      if (col[i].textContent == 7) { $(col[i]).append(`<div class="price">${json_resp["07"]}€</div>`) };
      if (col[i].textContent == 8) { $(col[i]).append(`<div class="price">${json_resp["08"]}€</div>`) };
      if (col[i].textContent == 9) { $(col[i]).append(`<div class="price">${json_resp["09"]}€</div>`) };
      if (col[i].textContent == 10) { $(col[i]).append(`<div class="price">${json_resp["10"]}€</div>`) };
      if (col[i].textContent == 11) { $(col[i]).append(`<div class="price">${json_resp["11"]}€</div>`) };
      if (col[i].textContent == 12) { $(col[i]).append(`<div class="price">${json_resp["12"]}€</div>`) };
      if (col[i].textContent == 13) { $(col[i]).append(`<div class="price">${json_resp["13"]}€</div>`) };
      if (col[i].textContent == 14) { $(col[i]).append(`<div class="price">${json_resp["14"]}€</div>`) };
      if (col[i].textContent == 15) { $(col[i]).append(`<div class="price">${json_resp["15"]}€</div>`) };
      if (col[i].textContent == 16) { $(col[i]).append(`<div class="price">${json_resp["16"]}€</div>`) };
      if (col[i].textContent == 17) { $(col[i]).append(`<div class="price">${json_resp["17"]}€</div>`) };
      if (col[i].textContent == 18) { $(col[i]).append(`<div class="price">${json_resp["18"]}€</div>`) };
      if (col[i].textContent == 19) { $(col[i]).append(`<div class="price">${json_resp["19"]}€</div>`) };
      if (col[i].textContent == 20) { $(col[i]).append(`<div class="price">${json_resp["20"]}€</div>`) };
      if (col[i].textContent == 21) { $(col[i]).append(`<div class="price">${json_resp["21"]}€</div>`) };
      if (col[i].textContent == 22) { $(col[i]).append(`<div class="price">${json_resp["22"]}€</div>`) };
      if (col[i].textContent == 23) { $(col[i]).append(`<div class="price">${json_resp["23"]}€</div>`) };
      if (col[i].textContent == 24) { $(col[i]).append(`<div class="price">${json_resp["24"]}€</div>`) };
      if (col[i].textContent == 25) { $(col[i]).append(`<div class="price">${json_resp["25"]}€</div>`) };
      if (col[i].textContent == 26) { $(col[i]).append(`<div class="price">${json_resp["26"]}€</div>`) };
      if (col[i].textContent == 27) { $(col[i]).append(`<div class="price">${json_resp["27"]}€</div>`) };
      if (col[i].textContent == 28) { $(col[i]).append(`<div class="price">${json_resp["28"]}€</div>`) };
      if (col[i].textContent == 29) { $(col[i]).append(`<div class="price">${json_resp["29"]}€</div>`) };
      if (col[i].textContent == 30) { $(col[i]).append(`<div class="price">${json_resp["30"]}€</div>`) };
      if (col[i].textContent == 31) { $(col[i]).append(`<div class="price">${json_resp["31"]}€</div>`) };
    }

    var prices = document.getElementsByClassName('price');

    for (i = 0; i < prices.length; i++) {
      if (prices[i].textContent == `${green_prices}€`) {
        prices[i].style.color = '#0aac0a';
      }
      if (prices[i].textContent == `999€`) {
        prices[i].innerHTML = '/';
      }
    }
  }

  if (origin.length > 1 && destination.length > 1) {
    xhttp.open("GET", "/get-calendar?origin=" + origin + "&destination=" + destination + "&month=" + month + "&year=" + year + "&n_adult=" + n_adu + "&n_baby=" + n_baby + "&atime=" + atime + "&frecce=" + frecce_bool, true);
    xhttp.send();
  } else {
    window.scrollTo({ top: document.getElementById('destination') });

    if (origin.length < 1) {
      document.getElementById('origin').style.animation = 'shake .20s 3'
    }
    if (destination.length < 1) {
      document.getElementById('destination').style.animation = 'shake .20s 3'
    }
  }
}


function from_stazioni() {
  $("#da_stazioni").remove();
  var letters = document.getElementById('origin').value;

  let xhttp = new XMLHttpRequest();
  xhttp.onload = function () {
    var html = "";
    var j = JSON.parse(xhttp.response);

    for (let n = 0; n < j.length; n++) {
      html += `<option value="${j[n].name}">`;
    }

    var dtlst = document.createElement('datalist');
    dtlst.id = "da_stazioni";
    document.getElementById('origin').append(dtlst);
    $('#da_stazioni').append(html);
  }
  if (letters.length > 1) {
    xhttp.open("POST", "/stations/?letter=" + letters, true);
    xhttp.send();
  }
}

function to_stazioni() {
  $("#a_stazioni").remove();
  var letters = document.getElementById('destination').value;
  let xhttp = new XMLHttpRequest();
  xhttp.onload = function () {
    var html = "";
    var j = JSON.parse(xhttp.response);
    for (let n = 0; n < j.length; n++) {
      html += `<option value="${j[n].name}">`;
    }
    var dtlst = document.createElement('datalist');
    dtlst.id = "a_stazioni";
    document.getElementById('destination').append(dtlst);
    $('#a_stazioni').append(html);
  }
  if (letters.length > 1) {
    xhttp.open("POST", "/stations/?letter=" + letters, true);
    xhttp.send();
  }
}

var cale = document.getElementById('tableBody')
cale.addEventListener('click', function () {
  var day_sel = document.getElementsByClassName('activeDay')
  var day = parseInt(day_sel[0].innerText[0] + day_sel[0].innerText[1])
  var origin = document.getElementById('origin').value;
  var destination = document.getElementById('destination').value;
  var n_adu = document.getElementById('n_adult_passeng').innerText;
  var n_baby = document.getElementById('n_baby_passeng').innerText;
  var atime = document.getElementById('pick_time').value;
  var frecce = document.getElementById('frecce').value;
  var year = document.getElementById('year-name').innerText;

  if (document.getElementById('month-name').innerText == "Gen") { var month = "01" };
  if (document.getElementById('month-name').innerText == "Feb") { var month = "02" };
  if (document.getElementById('month-name').innerText == "Mar") { var month = "03" };
  if (document.getElementById('month-name').innerText == "Apr") { var month = "04" };
  if (document.getElementById('month-name').innerText == "Mag") { var month = "05" };
  if (document.getElementById('month-name').innerText == "Giu") { var month = "06" };
  if (document.getElementById('month-name').innerText == "Lug") { var month = "07" };
  if (document.getElementById('month-name').innerText == "Ago") { var month = "08" };
  if (document.getElementById('month-name').innerText == "Set") { var month = "09" };
  if (document.getElementById('month-name').innerText == "Ott") { var month = "10" };
  if (document.getElementById('month-name').innerText == "Nov") { var month = "11" };
  if (document.getElementById('month-name').innerText == "Dic") { var month = "12" };

  if (frecce == 'si') {
    var frecce_bool = 'true'
  } else {
    frecce_bool = 'false'
  }

  var xhttp = new XMLHttpRequest;
  xhttp.onload = function () {
    $(".r").remove();
    var resp = JSON.parse(xhttp.response);
    var date_html = `<div class="r"><div class="row" style="justify-content: center;"><div class="col-auto">
                         <p style="font-size: 20px; font-weight: 400;">Treni del ${day}/${month}/${year}</p></div></div></div>`

    $('#resu').append(date_html)
    for (var i = 0; i < resp.length; i++) {
      for (var n = 0; n < resp[i].length; n++) {
        if (resp[i][n].saleable == true && parseInt(moment(resp[i][n].departuretime).format("D")) == parseInt(day)) {
          var html = `<div class="r"><div class="row">
          <div class="container" style="display: flex; gap: 0.6rem; background: white; border-radius: 10px; border: 1.5px solid blueviolet; width: 100%; flex-wrap: wrap; margin-bottom: 10px; justify-content: space-between; align-items: baseline;">
          <div class="item" style="text-align: center; padding-top: 10px; max-width: 72px; min-width: 72px;"><p style="font-weight: 500;">${moment(resp[i][n].departuretime).format("H:mm")}</p><p style="font-size: 12.5px; color: grey; ">${resp[i][n].origin}</p></div>
          <div class="item" style="color: gray; font-size: 11px; margin-top: 14px; min-width: 35px; ">${resp[i][n].duration}h</div>
          <div class="item" style="text-align: center; padding-top: 10px; max-width: 72px; min-width: 72px;"><p style="font-weight: 500">${moment(resp[i][n].arrivaltime).format("H:mm")}</p><p style="font-size: 12.5px; color: grey; ">${resp[i][n].destination}</p></div>
          <div class="item" style="display: contents"><p style="font-size: 10px; color: #494343; margin-left: 8%;">Cambi: ${resp[i][n].changesno}</p><p style="font-size: 10px; color: #494343; padding-left: 10px;">${resp[i][n].trainlist[0].trainacronym}</p>
          <a href="https://www.trenitalia.com/it.html" class="result--prices">${resp[i][n].originalPrice}€</a>
          </div>
          </div>
          </div></div>`
          $('#resu').append(html)
        }
      }
    }
    if (document.getElementsByClassName('r').length < 2) {
      message = `<div class="r"><div class="row">
        <p style="text-align: center;">Oops...pare che non ci siano treni, prova a cambiare l'orario di partenza o data.</p></div></div>`
      $('#resu').append(message)
    }
  }

  if (origin.length > 1 && destination.length > 1) {
    xhttp.open("GET", "/trains/?origin=" + origin + "&destination=" + destination + "&day=" + day + "&month=" + month + "&year=" + year + "&n_adult=" + n_adu + "&n_baby=" + n_baby + "&atime=" + atime + "&frecce=" + frecce_bool, true);
    xhttp.send();
  } else {
    window.scrollTo({ top: document.getElementById('destination') });

    if (origin.length < 1) {
      document.getElementById('origin').style.animation = 'shake .25s 3'
    }
    if (destination.length < 1) {
      document.getElementById('destination').style.animation = 'shake .25s 3'
    }
  }
})

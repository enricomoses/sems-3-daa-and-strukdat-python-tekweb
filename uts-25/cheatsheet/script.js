// CONTOH: #chat, #send, #pesan, #search, #table
$(document).ready(function () {
  // CHAT: SEND, KOSONGKAN INPUT, FOCUS
  $('#send').click(function () {
    var isi = $('#chat').val();
    if (isi != '') {
      var pesan = $('<div></div>').text(isi);
      $('#pesan').append(pesan);
      $('#chat').val('');
      $('#chat').focus();
    }
  });

  // PREPEND = tambah di awal
  $('#pesan').prepend('<div>Pesan pertama</div>');

  // TOGGLE / TOGGLE CLASS
  $('#tombol').click(function () {
    $('#pesan').toggle();
    $('#pesan').toggleClass('aktif');
  });

  // UBAH CSS, GET/SET
  $('#hasil').css('color', 'green');
  $('#hasil').css({ color: 'red', 'font-size': '20px' });
  $('#input').val('Budi');
  $('#hasil').text($('#input').val());

  // FILTER TABEL / LIST
  $('#search').on('keyup', function () {
    var cari = $(this).val().toLowerCase();
    $('#table tr').filter(function () {
      $(this).toggle($(this).text().toLowerCase().indexOf(cari) > -1);
    });
  });
});

// FETCH + PROMISE
fetch('https://jsonplaceholder.typicode.com/todos/1')
  .then((response) => response.json())
  .then((data) => console.log(data))
  .catch((error) => console.log(error))
  .finally(() => console.log('Selesai'));

// ASYNC / AWAIT
async function ambilData() {
  try {
    const response = await fetch(
      'https://jsonplaceholder.typicode.com/users/1',
    );
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.log('Gagal', error);
  }
}
ambilData();

// XMLHttpRequest
const xhr = new XMLHttpRequest();
xhr.open('GET', 'https://jsonplaceholder.typicode.com/todos/1');
xhr.onload = function () {
  if (xhr.status === 200) {
    console.log(JSON.parse(xhr.responseText));
  }
};
xhr.send();

// AJAX PAGINATION (latihan Update List)
// Setiap halaman 10 data
function ambilHalaman(halaman) {
  var mulai = (halaman - 1) * 10;
  $.ajax({
    url: 'https://jsonplaceholder.typicode.com/posts',
    method: 'GET',
    data: { _limit: 10, _start: mulai },
    dataType: 'json',
    success: function (data) {
      $('#list').empty();
      data.forEach(function (item) {
        $('#list').append($('<li></li>').text(item.title));
      });
    },
    error: function () {
      $('#list').text('Gagal memuat data');
    },
  });
}

// FETCH + PROMISE
fetch('https://jsonplaceholder.typicode.com/todos/1')
  .then((response) => response.json())
  .then((data) => console.log(data))
  .catch((error) => console.log(error))
  .finally(() => console.log('Selesai'));

// ASYNC / AWAIT
async function ambilData() {
  try {
    const response = await fetch(
      'https://jsonplaceholder.typicode.com/users/1',
    );
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.log('Gagal', error);
  }
}
ambilData();

// XMLHttpRequest
const xhr = new XMLHttpRequest();
xhr.open('GET', 'https://jsonplaceholder.typicode.com/todos/1');
xhr.onload = function () {
  if (xhr.status === 200) {
    console.log(JSON.parse(xhr.responseText));
  }
};
xhr.send();

// AJAX PAGINATION (latihan Update List)
// Setiap halaman 10 data
function ambilHalaman(halaman) {
  var mulai = (halaman - 1) * 10;
  $.ajax({
    url: 'https://jsonplaceholder.typicode.com/posts',
    method: 'GET',
    data: { _limit: 10, _start: mulai },
    dataType: 'json',
    success: function (data) {
      $('#list').empty();
      data.forEach(function (item) {
        $('#list').append($('<li></li>').text(item.title));
      });
    },
    error: function () {
      $('#list').text('Gagal memuat data');
    },
  });
}

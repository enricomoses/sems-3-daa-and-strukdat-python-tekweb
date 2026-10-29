/* ============================================================
   app.js — TULIS SELURUH JAWABAN ANDA DI BERKAS INI
   Nama  :
   NRP   :
   Kelas :

   Boleh memakai JavaScript murni atau jQuery.

   PENTING: FormData DILARANG di Bagian A, B, dan C.
            Baca tiap elemen satu per satu. FormData hanya
            diizinkan di bonus D1.
   ============================================================ */


/* ------------------------------------------------------------
   Peta nilai -> teks yang dilihat pengguna.
   Dipakai di panel ringkasan (A4). Sudah disediakan agar Anda
   tidak perlu mengetik ulang daftarnya.
   ------------------------------------------------------------ */

const TEKS = {
  level: { junior: "Junior", menengah: "Menengah", senior: "Senior" },
  zona:  { wib: "WIB (Jakarta)", wita: "WITA (Makassar)", wit: "WIT (Jayapura)" },
  minat: { frontend: "Frontend", backend: "Backend", mobile: "Mobile",
           data: "Data", devops: "DevOps" },
  stack: { js: "JavaScript", py: "Python", php: "PHP",
           go: "Go", java: "Java", dart: "Dart" },
};


/* ============================================================
   A1 — MEMBACA SELURUH FORMULIR

   Kembalikan SATU objek berisi kesebelas properti, dengan tipe
   data yang benar. Lihat tabel di lembar soal.

   Pengingat singkat:
     text/password/textarea -> .value           (string)
     range                  -> angka, bukan string
     radio                  -> cari yang :checked, bisa null
     checkbox tunggal       -> .checked         (boolean)
     checkbox grup          -> array of string
     select tunggal         -> .value           (string)
     select multiple        -> array of string, BUKAN .value
   ============================================================ */

function bacaForm() {
  // TODO (A1)
  return {
    nama: null,
    username: null,
    sandi: null,
    sandi2: null,
    pengalaman: null,
    level: null,
    minat: null,
    zona: null,
    stack: null,
    bio: null,
    setuju: null,
  };
}


/* ============================================================
   B1 — VALIDASI

   Terima hasil bacaForm(), kembalikan objek berisi pesan
   kesalahan per kolom. Objek kosong berarti semuanya sah.

   Contoh bentuk kembalian:
     { nama: "Nama minimal 3 karakter.", setuju: "Wajib dicentang." }
   ============================================================ */

function validasi(data) {
  const err = {};
  // TODO (B1) sembilan aturan sesuai tabel di lembar soal
  return err;
}


/* ============================================================
   MENGGAMBAR
   ============================================================ */

// A4 — panel ringkasan yang hidup
function renderRingkasan() {
  // TODO (A4)
  // Kolom kosong ditulis "—"
  // Sandi ditampilkan sebagai titik sebanyak karakternya
  // level, zona, minat, stack memakai TEKS di atas, bukan value-nya
}

// A3 — angka di sebelah slider
function renderNilaiRange() {
  // TODO (A3) tampilkan "7 tahun", dan "20+ tahun" untuk nilai tertinggi
}

// B2 — penghitung karakter bio
function renderHitungBio() {
  // TODO (B2) "47/200", merah kalau lewat 200
}

// B1 — tulis atau bersihkan pesan kesalahan
function renderError(err) {
  // TODO (B1) isi tiap #err-*, dan beri/lepas kelas "salah"
  //           pada kolom yang bermasalah
}


/* ============================================================
   A2 — TOMBOL LIHAT JSON
   ============================================================ */

function tampilkanJSON() {
  // TODO (A2) JSON.stringify(bacaForm(), null, 2) ke #json-output
}


/* ============================================================
   B3 — SAAT FORMULIR DIKIRIM
   ============================================================ */

function kirim(event) {
  // TODO (B3)
  // 1. cegah halaman memuat ulang
  // 2. baca + validasi
  // 3. kalau ada kesalahan: tampilkan semuanya, fokuskan yang paling atas
  // 4. kalau sah: bersihkan pesan, tampilkan #hasil
  //    (kata sandi TIDAK boleh muncul di kartu hasil)
}


/* ============================================================
   C1 — RESET
   ============================================================ */

function resetSemua() {
  // TODO (C1) kosongkan isian DAN seluruh tampilan turunannya:
  //           pesan kesalahan, tanda merah, angka slider,
  //           penghitung bio, ringkasan, JSON, kartu hasil
}


/* ============================================================
   BONUS D1 — VERSI FORMDATA (kerjakan paling akhir)
   ============================================================ */

function bacaFormData() {
  // TODO (D1) baca formulir yang sama memakai new FormData(form).
  // Lalu tulis di komentar bawah ini DUA perbedaan nyata yang
  // Anda temukan dibanding bacaForm():
  //
  // Perbedaan 1:
  // Perbedaan 2:
}


/* ============================================================
   EVENT
   ============================================================ */

function pasangEvent() {
  // TODO (A3, A4, B2) satu listener "input" pada formulir sudah
  //                   cukup untuk menyegarkan seluruh tampilan
  // TODO (A2) klik #btn-json
  // TODO (B3) submit #form-daftar
  // TODO (C1) klik #btn-reset
}


/* ------------------------------------------------------------
   TITIK MULAI
   ------------------------------------------------------------ */

pasangEvent();
renderNilaiRange();
renderHitungBio();
renderRingkasan();

/* ============================================================
   app.js — KUNCI JAWABAN
   Latihan UTS Teknologi Web · Membaca Nilai Formulir

   Ditulis dengan JavaScript murni. Mahasiswa yang memakai jQuery
   dengan hasil yang sama tetap bernilai penuh.

   Peta nomor soal:
     A1 bacaForm()
     A2 tampilkanJSON()
     A3 renderNilaiRange()
     A4 renderRingkasan()
     B1 validasi() + renderError()
     B2 renderHitungBio()
     B3 kirim()
     C1 resetSemua()
     C2 pembagian baca / validasi / gambar di berkas ini
     C3 tidak ada error konsol; kelas Tailwind di index.html
     D1 bacaFormData()
     D2 renderKekuatanSandi()
     D3 aturSisaMinat()
   ============================================================ */


const TEKS = {
  level: { junior: "Junior", menengah: "Menengah", senior: "Senior" },
  zona:  { wib: "WIB (Jakarta)", wita: "WITA (Makassar)", wit: "WIT (Jayapura)" },
  minat: { frontend: "Frontend", backend: "Backend", mobile: "Mobile",
           data: "Data", devops: "DevOps" },
  stack: { js: "JavaScript", py: "Python", php: "PHP",
           go: "Go", java: "Java", dart: "Dart" },
};

const MAKS_BIO = 200;
const MAKS_MINAT = 3;

const form = document.getElementById("form-daftar");

const el = {
  nama:       document.getElementById("f-nama"),
  username:   document.getElementById("f-username"),
  sandi:      document.getElementById("f-sandi"),
  sandi2:     document.getElementById("f-sandi2"),
  pengalaman: document.getElementById("f-pengalaman"),
  zona:       document.getElementById("f-zona"),
  stack:      document.getElementById("f-stack"),
  bio:        document.getElementById("f-bio"),
  setuju:     document.getElementById("f-setuju"),
  nilaiRange: document.getElementById("nilai-pengalaman"),
  hitungBio:  document.getElementById("hitung-bio"),
  ringkasan:  document.getElementById("ringkasan"),
  json:       document.getElementById("json-output"),
  btnJson:    document.getElementById("btn-json"),
  btnReset:   document.getElementById("btn-reset"),
  hasil:      document.getElementById("hasil"),
};

// Kolom yang punya kotak pesan kesalahan, berurutan dari atas ke
// bawah — urutan ini dipakai B3 untuk menentukan fokus pertama.
const KOLOM_ERROR = ["nama", "username", "sandi", "sandi2",
                     "level", "minat", "stack", "bio", "setuju"];

// Elemen yang diberi garis tepi merah saat bermasalah.
// level dan minat tidak punya satu elemen, jadi tidak ada di sini.
const ELEMEN_TANDA = {
  nama: el.nama, username: el.username, sandi: el.sandi,
  sandi2: el.sandi2, stack: el.stack, bio: el.bio,
};


/* ============================================================
   A1 — MEMBACA SELURUH FORMULIR
   ============================================================ */

function bacaForm() {
  // radio: cari anggota yang terpilih. Bisa tidak ada sama sekali,
  // jadi ?. dan ?? wajib — tanpanya TypeError menghentikan script.
  const levelTerpilih = form.querySelector('input[name="level"]:checked');

  // checkbox grup: kumpulkan yang tercentang, ambil value-nya
  const minatTercentang = form.querySelectorAll('input[name="minat"]:checked');

  return {
    // string biasa, dirapikan dari spasi di ujung
    nama: el.nama.value.trim(),
    username: el.username.value.trim(),

    // sandi TIDAK di-trim: spasi adalah karakter sah di dalam sandi
    sandi: el.sandi.value,
    sandi2: el.sandi2.value,

    // range memberi string "7"; valueAsNumber langsung memberi angka 7
    pengalaman: el.pengalaman.valueAsNumber,

    // null kalau pengguna belum memilih apa pun
    level: levelTerpilih?.value ?? null,

    // array, meski hanya satu atau bahkan nol yang tercentang
    minat: [...minatTercentang].map((c) => c.value),

    // select tunggal cukup .value
    zona: el.zona.value,

    // select multiple: .value hanya memberi pilihan PERTAMA,
    // jadi selectedOptions yang dipakai
    stack: [...el.stack.selectedOptions].map((o) => o.value),

    bio: el.bio.value.trim(),

    // checkbox tunggal dibaca lewat .checked, bukan .value
    setuju: el.setuju.checked,
  };
}


/* ============================================================
   B1 — VALIDASI
   ============================================================ */

function validasi(d) {
  const err = {};

  if (d.nama.length < 3) {
    err.nama = "Nama wajib diisi, minimal 3 karakter.";
  }

  if (d.username.length < 3 || d.username.length > 15) {
    err.username = "Username harus 3–15 karakter.";
  } else if (!/^[A-Za-z0-9_]+$/.test(d.username)) {
    err.username = "Username hanya boleh huruf, angka, dan garis bawah.";
  }

  if (d.sandi.length < 8) {
    err.sandi = "Kata sandi minimal 8 karakter.";
  } else if (!/[A-Za-z]/.test(d.sandi) || !/[0-9]/.test(d.sandi)) {
    err.sandi = "Kata sandi harus memuat huruf dan angka.";
  }

  if (d.sandi2 !== d.sandi) {
    err.sandi2 = "Ulangan kata sandi tidak sama.";
  }

  // null, bukan string kosong — inilah bentuk radio yang belum dipilih
  if (d.level === null) {
    err.level = "Pilih salah satu level.";
  }

  if (d.minat.length === 0) {
    err.minat = "Pilih minimal satu bidang minat.";
  } else if (d.minat.length > MAKS_MINAT) {
    err.minat = `Maksimal ${MAKS_MINAT} bidang minat.`;
  }

  if (d.stack.length === 0) {
    err.stack = "Pilih minimal satu teknologi.";
  }

  if (d.bio.length > MAKS_BIO) {
    err.bio = `Bio maksimal ${MAKS_BIO} karakter, sekarang ${d.bio.length}.`;
  }

  // boolean false, bukan string kosong
  if (!d.setuju) {
    err.setuju = "Anda harus menyetujui syarat dan ketentuan.";
  }

  return err;
}


/* ============================================================
   MENGGAMBAR
   ============================================================ */

function baris(label, isi) {
  return `<dt class="text-slate-500">${label}</dt><dd>${isi}</dd>`;
}

// Nilai apa pun yang kosong ditulis sebagai tanda hubung.
function atauStrip(nilai) {
  if (nilai === null || nilai === undefined) return "—";
  if (Array.isArray(nilai)) return nilai.length ? nilai.join(", ") : "—";
  return String(nilai).trim() === "" ? "—" : String(nilai);
}

// A4
function renderRingkasan() {
  const d = bacaForm();

  // Nilai diterjemahkan ke teks yang dilihat pengguna.
  const level = d.level ? TEKS.level[d.level] : null;
  const zona = TEKS.zona[d.zona];
  const minat = d.minat.map((v) => TEKS.minat[v]);
  const stack = d.stack.map((v) => TEKS.stack[v]);

  el.ringkasan.innerHTML = [
    baris("Nama", atauStrip(d.nama)),
    baris("Username", atauStrip(d.username)),
    // sandi tidak pernah ditampilkan apa adanya
    baris("Sandi", d.sandi ? "•".repeat(d.sandi.length) : "—"),
    baris("Pengalaman", d.pengalaman + " tahun"),
    baris("Level", atauStrip(level)),
    baris("Minat", atauStrip(minat)),
    baris("Zona", atauStrip(zona)),
    baris("Stack", atauStrip(stack)),
    baris("Bio", atauStrip(d.bio)),
    baris("Setuju", d.setuju ? "ya" : "belum"),
  ].join("");
}

// A3
function renderNilaiRange() {
  const n = el.pengalaman.valueAsNumber;
  const maks = Number(el.pengalaman.max);
  el.nilaiRange.textContent = n >= maks ? `${maks}+ tahun` : `${n} tahun`;
}

// B2
function renderHitungBio() {
  const panjang = el.bio.value.length;
  el.hitungBio.textContent = `${panjang}/${MAKS_BIO}`;
  el.hitungBio.classList.toggle("text-red-600", panjang > MAKS_BIO);
  el.hitungBio.classList.toggle("text-slate-400", panjang <= MAKS_BIO);
}

// B1
function renderError(err) {
  KOLOM_ERROR.forEach((kolom) => {
    const kotak = document.getElementById("err-" + kolom);
    if (kotak) kotak.textContent = err[kolom] || "";

    const input = ELEMEN_TANDA[kolom];
    if (input) input.classList.toggle("salah", Boolean(err[kolom]));
  });
}


/* ============================================================
   A2 — TOMBOL LIHAT JSON
   ============================================================ */

function tampilkanJSON() {
  el.json.textContent = JSON.stringify(bacaForm(), null, 2);
}


/* ============================================================
   B3 — SAAT FORMULIR DIKIRIM
   ============================================================ */

function kirim(event) {
  event.preventDefault();                 // tanpa ini halaman memuat ulang

  const data = bacaForm();
  const err = validasi(data);

  renderError(err);                        // tampilkan SEMUA pesan sekaligus

  const kolomSalah = KOLOM_ERROR.filter((k) => err[k]);

  if (kolomSalah.length > 0) {
    el.hasil.classList.add("hidden");
    fokuskan(kolomSalah[0]);               // yang paling atas
    return;
  }

  el.hasil.innerHTML = `
    <h3 class="font-bold mb-2">Pendaftaran berhasil</h3>
    <p>Selamat datang, <strong>${data.nama}</strong>.</p>
    <dl class="grid grid-cols-[6rem_1fr] gap-y-1 mt-2 text-xs">
      <dt class="text-slate-500">Username</dt><dd>${data.username}</dd>
      <dt class="text-slate-500">Level</dt><dd>${TEKS.level[data.level]}</dd>
      <dt class="text-slate-500">Minat</dt><dd>${data.minat.length} bidang</dd>
      <dt class="text-slate-500">Teknologi</dt><dd>${data.stack.length} dipilih</dd>
    </dl>
  `;
  el.hasil.classList.remove("hidden");
}

// Radio dan checkbox grup tidak punya id tunggal, jadi anggota
// pertamanya yang difokuskan.
function fokuskan(kolom) {
  const target =
    ELEMEN_TANDA[kolom] ||
    form.querySelector(`[name="${kolom}"]`);
  target?.focus();
}


/* ============================================================
   C1 — RESET
   ============================================================ */

function resetSemua() {
  form.reset();          // hanya mengosongkan isian formulir…

  // …sisanya milik kita sendiri dan harus dibereskan manual.
  renderError({});
  renderNilaiRange();
  renderHitungBio();
  renderRingkasan();
  renderKekuatanSandi();
  aturSisaMinat();
  el.json.textContent = "";
  el.hasil.classList.add("hidden");
  el.hasil.innerHTML = "";
  el.nama.focus();
}


/* ============================================================
   BONUS D1 — VERSI FORMDATA
   ============================================================ */

function bacaFormData() {
  const fd = new FormData(form);

  return {
    nama: (fd.get("nama") || "").trim(),
    username: (fd.get("username") || "").trim(),
    sandi: fd.get("sandi") || "",
    sandi2: fd.get("sandi2") || "",
    pengalaman: Number(fd.get("pengalaman")),   // FormData selalu memberi string
    level: fd.get("level"),                      // null kalau belum dipilih
    minat: fd.getAll("minat"),                   // getAll, bukan get
    zona: fd.get("zona"),
    stack: fd.getAll("stack"),
    bio: (fd.get("bio") || "").trim(),
    setuju: fd.get("setuju") !== null,           // absen = tidak dicentang
  };
}

/* Perbedaan 1: kolom yang tidak tercentang TIDAK ADA di FormData.
   Checkbox "setuju" yang kosong tidak menghasilkan false — ia hilang
   sama sekali, dan fd.get("setuju") mengembalikan null. Begitu pula
   radio "level" yang belum dipilih. Jadi boolean harus disimpulkan
   dari ada-tidaknya kunci, bukan dibaca langsung.

   Perbedaan 2: fd.get() hanya memberi nilai PERTAMA untuk nama yang
   berulang. Memakai fd.get("minat") pada tiga checkbox tercentang
   hanya memberi satu nilai; yang benar adalah fd.getAll("minat").

   Catatan ketiga: FormData hanya membaca elemen yang punya atribut
   name. Elemen yang hanya punya id tidak pernah ikut terbaca. */


/* ============================================================
   BONUS D2 — KEKUATAN SANDI
   ============================================================ */

function renderKekuatanSandi() {
  const bar = document.getElementById("bar-sandi");
  if (!bar) return;                       // elemen opsional

  const s = el.sandi.value;
  let skor = 0;
  if (s.length >= 8) skor++;
  if (s.length >= 12) skor++;
  if (/[A-Z]/.test(s) && /[a-z]/.test(s)) skor++;
  if (/[0-9]/.test(s)) skor++;
  if (/[^A-Za-z0-9]/.test(s)) skor++;

  const warna = ["bg-slate-200", "bg-red-500", "bg-orange-500",
                 "bg-yellow-500", "bg-lime-500", "bg-green-600"];
  bar.className = "h-1.5 rounded transition-all " + warna[skor];
  bar.style.width = (skor / 5 * 100) + "%";
}


/* ============================================================
   BONUS D3 — BATAS PILIHAN MINAT
   ============================================================ */

function aturSisaMinat() {
  const semua = [...form.querySelectorAll('input[name="minat"]')];
  const tercentang = semua.filter((c) => c.checked);
  const penuh = tercentang.length >= MAKS_MINAT;

  semua.forEach((c) => { c.disabled = penuh && !c.checked; });

  const info = document.getElementById("sisa-minat");
  if (info) {
    info.textContent = penuh
      ? "Batas tercapai"
      : `Sisa ${MAKS_MINAT - tercentang.length} pilihan`;
  }
}


/* ============================================================
   EVENT
   ============================================================ */

function segarkan() {
  renderNilaiRange();
  renderHitungBio();
  renderRingkasan();
  renderKekuatanSandi();
  aturSisaMinat();
}

function pasangEvent() {
  // Satu listener pada formulir sudah menangkap SELURUH elemen di
  // dalamnya, karena event "input" menggelembung. Event "input"
  // menyala pada setiap perubahan kecil — termasuk saat slider
  // digeser, bukan setelah dilepas seperti "change".
  form.addEventListener("input", segarkan);

  // "change" tetap dipasang untuk checkbox dan radio di browser lama
  // yang belum menyalakan "input" pada keduanya.
  form.addEventListener("change", segarkan);

  el.btnJson.addEventListener("click", tampilkanJSON);
  form.addEventListener("submit", kirim);
  el.btnReset.addEventListener("click", resetSemua);
}


/* ------------------------------------------------------------
   TITIK MULAI
   ------------------------------------------------------------ */

pasangEvent();
segarkan();

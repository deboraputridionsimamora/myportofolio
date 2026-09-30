let toastTimer;

// fungsi buat munculin toast, dipanggil dari halaman mana aja
function showToast(title, message, type = 'normal', duration = 3000) {
  const toastComponent = document.getElementById('toast-component');
  const toastTitle = document.getElementById('toast-title');
  const toastMessage = document.getElementById('toast-message');

  if (!toastComponent) return;

  // hapus warna yang lama dulu
  toastComponent.classList.remove('toast-success', 'toast-error', 'toast-normal');

  // kasih warna sesuai tipe (hijau = sukses, merah = error)
  if (type === 'success') {
      toastComponent.classList.add('toast-success');
  } else if (type === 'error') {
      toastComponent.classList.add('toast-error');
  } else {
      toastComponent.classList.add('toast-normal');
  }

  // pakai textContent biar isinya dianggap teks biasa, bukan HTML
  toastTitle.textContent = title;
  toastMessage.textContent = message;

  // kalau toast sebelumnya masih nongol, timernya direset
  clearTimeout(toastTimer);

  if (!toastComponent.matches(':popover-open')) {
      toastComponent.showPopover();
      void toastComponent.offsetHeight; // biar animasinya jalan
  }
  toastComponent.classList.remove('toast-hidden');
  toastComponent.classList.add('toast-show');

  // setelah beberapa detik, toast turun lagi terus disembunyiin
  toastTimer = setTimeout(() => {
      toastComponent.classList.remove('toast-show');
      toastComponent.classList.add('toast-hidden');
      toastTimer = setTimeout(() => toastComponent.hidePopover(), 300);
  }, duration);
}
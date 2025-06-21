let tg = Window.Telegram.WebApp;
tg.expand();

function increase(btn) {
  const qtyDiv = btn.parentElement.querySelector('.qty-number');
  let value = parseInt(qtyDiv.innerText);
  qtyDiv.innerText = value + 1;
  updateMainButton();
}

function decrease(btn) {
  const qtyDiv = btn.parentElement.querySelector('.qty-number');
  let value = parseInt(qtyDiv.innerText);
  if (value > 0) {
    qtyDiv.innerText = value - 1;
    updateMainButton();
  }
}

function updateMainButton() {
  const qtyNumbers = document.querySelectorAll('.qty-number');
  let totalItems = 0;

  qtyNumbers.forEach(qty => {
    totalItems += parseInt(qty.innerText);
  });

  if (totalItems > 0) {
    tg.MainButton.show();
  } else {
    tg.MainButton.hide();
  }
}

function filterProducts(category) {
  const cards = document.querySelectorAll('.product-card');

  cards.forEach(card => {
    const cardCategory = card.getAttribute('data-category');
    if (category === 'all') {
      card.style.display = 'block';
    } else if (cardCategory === category) {
      card.style.display = 'block';
    } else {
      card.style.display = 'none';
    }
  });
}

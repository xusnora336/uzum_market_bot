let tg = window.Telegram.WebApp;
tg.expand();

// Функция для проверки общего количества товаров
function getTotalQuantity() {
  const qtyDivs = document.querySelectorAll('.qty-number');
  let total = 0;
  qtyDivs.forEach(div => {
    total += parseInt(div.innerText);
  });
  return total;
}

// Функция для обновления состояния MainButton
function updateMainButton() {
  const totalQuantity = getTotalQuantity();
  if (totalQuantity > 0) {
    tg.MainButton.show();
  } else {
    tg.MainButton.hide();
  }
}

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
  }
  updateMainButton();
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

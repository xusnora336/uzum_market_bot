function increase(btn) {
  const qtyDiv = btn.parentElement.querySelector('.qty-number');
  let value = parseInt(qtyDiv.innerText);
  qtyDiv.innerText = value + 1;
}

function decrease(btn) {
  const qtyDiv = btn.parentElement.querySelector('.qty-number');
  let value = parseInt(qtyDiv.innerText);
  if (value > 0) {
    qtyDiv.innerText = value - 1;
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

<script>
  // Плюс и минус
  document.querySelectorAll('.product').forEach(product => {
  const plusBtn = product.querySelector('.plus');
  const minusBtn = product.querySelector('.minus');
  const countSpan = product.querySelector('.count');
  let count = 0;

  plusBtn.addEventListener('click', () => {
  count++;
  countSpan.textContent = count;
});

  minusBtn.addEventListener('click', () => {
  if (count > 0) {
  count--;
  countSpan.textContent = count;
}
});
});

  // Фильтр по категориям
  function filterCategory(category) {
  const products = document.querySelectorAll('.product');
  let shown = 0;

  products.forEach(product => {
  if (category === 'all') {
  product.style.display = 'block';
} else if (product.dataset.category === category && shown < 6) {
  product.style.display = 'block';
  shown++;
} else {
  product.style.display = 'none';
}
});
}
</script>

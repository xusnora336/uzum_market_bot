let tg = window.Telegram.WebApp;
tg.expand();

tg.MainButton.textColor = "#FFFFFF";
tg.MainButton.color = "#FC3005";

// Продукт 1
let item1 = "";
let n_count1 = 0;
let count1 = document.getElementById("count1");
let rbtn1 = document.getElementById("rbtn1");
let abtn1 = document.getElementById("abtn1");

abtn1.addEventListener("click", function () {
    count1.innerText = n_count1 += 1;
    count1.style.display = "inline-block";
    item1 = "ID_1/" + count1.innerText;
    tg.MainButton.setText("Оплата");
    tg.MainButton.show();
});

rbtn1.addEventListener("click", function () {
    if (n_count1 > 0) {
        count1.innerText = n_count1 -= 1;
    }
    count1.style.display = "inline-block";
    item1 = "ID_1/" + count1.innerText;
    tg.MainButton.setText("Оплата");
    tg.MainButton.show();
});

// Продукт 2
let item2 = "";
let n_count2 = 0;
let count2 = document.getElementById("count2");
let rbtn2 = document.getElementById("rbtn2");
let abtn2 = document.getElementById("abtn2");

abtn2.addEventListener("click", function () {
    count2.innerText = n_count2 += 1;
    count2.style.display = "inline-block";
    item2 = "ID_2/" + count2.innerText;
    tg.MainButton.setText("Оплата");
    tg.MainButton.show();
});

rbtn2.addEventListener("click", function () {
    if (n_count2 > 0) {
        count2.innerText = n_count2 -= 1;
    }
    count2.style.display = "inline-block";
    item2 = "ID_2/" + count2.innerText;
    tg.MainButton.setText("Оплата");
    tg.MainButton.show();
});

// Продукт 3
let item3 = "";
let n_count3 = 0;
let count3 = document.getElementById("count3");
let rbtn3 = document.getElementById("rbtn3");
let abtn3 = document.getElementById("abtn3");

abtn3.addEventListener("click", function () {
    count3.innerText = n_count3 += 1;
    count3.style.display = "inline-block";
    item3 = "ID_3/" + count3.innerText;
    tg.MainButton.setText("Оплата");
    tg.MainButton.show();
});

rbtn3.addEventListener("click", function () {
    if (n_count3 > 0) {
        count3.innerText = n_count3 -= 1;
    }
    count3.style.display = "inline-block";
    item3 = "ID_3/" + count3.innerText;
    tg.MainButton.setText("Оплата");
    tg.MainButton.show();
});

// Продукт 4
let item4 = "";
let n_count4 = 0;
let count4 = document.getElementById("count4");
let rbtn4 = document.getElementById("rbtn4");
let abtn4 = document.getElementById("abtn4");

abtn4.addEventListener("click", function () {
    count4.innerText = n_count4 += 1;
    count4.style.display = "inline-block";
    item4 = "ID_4/" + count4.innerText;
    tg.MainButton.setText("Оплата");
    tg.MainButton.show();
});

rbtn4.addEventListener("click", function () {
    if (n_count4 > 0) {
        count4.innerText = n_count4 -= 1;
    }
    count4.style.display = "inline-block";
    item4 = "ID_4/" + count4.innerText;
    tg.MainButton.setText("Оплата");
    tg.MainButton.show();
});

// Обработка нажатия на MainButton
Telegram.WebApp.onEvent("mainButtonClicked", function () {
    const data = item1 + "|" + item2 + "|" + item3 + "|" + item4;
    tg.sendData(data);
});

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

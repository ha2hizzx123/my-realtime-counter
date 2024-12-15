const countElement = document.getElementById('count');
const imageElement = document.getElementById('image');
const incrementButton = document.getElementById('increment');
const decrementButton = document.getElementById('decrement');

const updateCount = async () => {
  const response = await fetch('http://localhost:8002/count');
  if (response.ok) {
    const data = await response.json();
    countElement.textContent = data.count;
    imageElement.src = `./images/image${data.count % 4}.png`; // 서버에서 이미지 제공
  } else {
    console.error("Failed to fetch count data");
  }
};

incrementButton.addEventListener('click', async () => {
  await fetch('http://localhost:8002/count/increment', { method: 'POST' });
  updateCount();
});

decrementButton.addEventListener('click', async () => {
  await fetch('http://localhost:8002/count/decrement', { method: 'POST' });
  updateCount();
});

// 초기값 업데이트
updateCount();

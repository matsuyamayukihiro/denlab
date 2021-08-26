/* card型レイアウト作成用関数 */
function setCard(title, text, imgurl) {
  let position = document.getElementById('cardlayout-wrap');
  const div = `
  <section class="card-list">
    <a class="card-link" href="http://localhost/tornado6-1.2.html?lib=jquery&ver=3">
      <figure class="card-figure"><img src="` + imgurl + `"></figure>
      <h2 class="card-title">` + title + `</h2>
      <p class="card-text-tax">` + text + `</p>
    </a>
  </section>
    `
  position.insertAdjacentHTML('beforeend', div);
}



document.addEventListener('DOMContentLoaded', (event) => {
  console.log(`DOMContentLoadedイベントが発生しました。`);

  for (let index = 0; index < 12; index++) {
    const title = 'カードレイアウト' + index
    setCard(title, 'Flexboxとcale()を使ってかんたんにレスポンシブ対応カードレイアウトをつくる手順のご紹介', 'images/temple_night.png');
  }

  /* json読み込み */
  const USERS_API = "https://jsonplaceholder.typicode.com/users";

  async function callApi() {
    const res = await window.fetch(USERS_API);
    const users = await res.json();

    //var arr = JSON.parse(users);
    //var arr = JSON.parse(json_text);
    //console.log(users);
    console.log("以下jsonテスト1");
    console.log(users);

    console.log("以下jsonテスト2");
    for (var item in users) {
      console.log(item + ': ' + users[item])
    }

    console.log("以下jsonテスト3");
    for (var item in res) {
      console.log(item + ': ' + res[item])
    }

  }

  callApi();

  /* /json読み込み */

});
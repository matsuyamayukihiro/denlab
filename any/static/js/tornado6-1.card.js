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

/* アイディアのcard型レイアウト作成用関数 */
function setIdeaCard(id, username, tag, title, discription, image, good) {
  /* card配置用 */
  let position1 = document.getElementById('cardlayout-wrap');
  let div1 = ``
  if (image != '') {
    // 何かしらの文字列が入っている場合
    div1 = `
      <section class="card-list">
        <a class="card-link" href="http://localhost/tornado6-1.2.html` + `?id=` + id + `">
          <h2 class="card-title">` + title + `</h2>
          </a>
          <p class="card-text-tax">` + username + `</p>
          <button class="btn" id="clickBtn` + id + `">詳細を見る</button>
          <div id="` + `hide` + id + `" style="display: none;">
            <p class="card-text-tax">` + discription + `</p>
            <figure class="card-figure"><img src="` + image + `"></figure>
          </div>
      </section>
        `
  } else {
    // 文字列が空の場合
    div1 = `
      <section class="card-list">
        <a class="card-link" href="http://localhost/tornado6-1.2.html` + `?id=` + id + `">
          <h2 class="card-title">` + title + `</h2>
        </a>
        <p class="card-text-tax">` + username + `</p>
        <input type="button" value="詳細を読む" onclick="clickBtn` + id + `()" />
        <div id="` + `hide` + id + `">
          <p class="card-text-tax">` + discription + `</p>
        </div>
      </section>
    `
  }
  /**
   * ToDo
   * (済) idでリンクを作成できるようにしておく
   * (2) goodボタンの実装
   * (3) 非表示内容をタグで囲み、idで差別化
   */
  position1.insertAdjacentHTML('beforeend', div1);
  /* /card配置用 */

  /* card内の「詳細」用 */
  let position2 = document.getElementById('innerScript');
  const div2 = `
  <script>
    //初期表示は非表示
    document.getElementById("` + `hide` + id + `").style.display = "none";

    window.clickBtn` + id + ` =function() {
      const p1 = document.getElementById("` + `hide` + id + `");

      if (p1.style.display == "block") {
        // noneで非表示
        p1.style.display = "none";
      } else {
        // blockで表示
        p1.style.display = "block";
      }
    }
  </script>
    `
  /**
   * ToDo
   * (1) getElementByIdをidで判別できるようにする
   * (2) その他idで区別できるようにする
   */
  position2.insertAdjacentHTML('afterend', div2);
  /* /card内の「詳細」用 */
}



document.addEventListener('DOMContentLoaded', (event) => {
  console.log(`DOMContentLoadedイベントが発生しました。`);

  for (let id = 100; id < 112; id++) {
    let username = 'テストユーザー' + id;
    let tag = '';
    let title = 'コラム' + id;
    let discription = '詳細説明文';
    let image = 'images/temple_night.png';
    let good = 0;
    //setCard(title, 'Flexboxとcale()を使ってかんたんにレスポンシブ対応カードレイアウトをつくる手順のご紹介', 'images/temple_night.png');
    setIdeaCard(id, username, tag, title, discription, image, good)
  }

  /* json読み込み */
  //const USERS_API = "https://jsonplaceholder.typicode.com/users";
  const USERS_API = "https://denlab.herokuapp.com/column";

  //ajax送信
  $.ajax({
    //画像処理サーバーに返す場合
    url: 'https://denlab.herokuapp.com/column',
    type: 'POST',
    //data: fData,
    //contentType: false,//サーバーにデータを送信するときに使う
    //processData: false,
    dataType: "json",
    success: function (data, dataType) {
      //非同期で通信成功時に読み出される [200 OK 時]
      console.log('Success', data);

      if (data.ResultSet.ip_type == 'OCR') {
        var res = data.ResultSet.result; // 'hogehoge'
        var prefix = data.ResultSet.prefix; // '201701011200'

      }


    },
    error: function (XMLHttpRequest, textStatus, errorThrown) {
      //非同期で通信失敗時に読み出される
      console.error('ajaxError : ' + errorThrown);
    }
  });

  async function callApi() {
    const res = await window.fetch(USERS_API);
    const users = await res.json();

    var arr = JSON.parse(users);
    //var arr = JSON.parse(json_text);
    //console.log(users);
    console.log("以下jsonテスト1");
    console.log("users" , users);
    console.log("arr" , arr);

    console.log("以下jsonテスト2");
    for (var item in users) {
      console.log(item + ': ' + users[item])
    }

    console.log("以下jsonテスト3");
    for (var item in res) {
      console.log(item + ': ' + res[item])
    }

  }

  console.log("以下callApi");
  callApi();

  //APIからJSONデータを取得する
  fetch(url)
    .then((response) => {
      return response.json(); //ここでBodyからJSONを返す
    })
    .then((result) => {
      Example(result); //取得したJSONデータを関数に渡す
    })
    .catch((e) => {
      console.log(e) //エラーをキャッチし表示
    })

  //JSONデータを引数に受け取ってDOM操作を行う関数を作成
  function Example(jsonObj) {
    const data = jsonObj.results[0]
    name.textContent = data.name;
    age.textContent = data.age;
  }

  console.log("以下fetch");
  fetch(USERS_API);

  /* /json読み込み */

  $('.btn').on('click', function () {
    var id = $(this).attr("id");
    alert(id);
  });

});
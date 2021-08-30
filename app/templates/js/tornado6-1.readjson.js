document.addEventListener('DOMContentLoaded', (event) => {
  console.log(`DOMContentLoadedイベントが発生しました。`);

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
      var column_id = data.ResultSet.column_id; // 'コラムID'
      var  column_username = data.ResultSet. column_username; // '投稿者指名'
      var  column_tag = data.ResultSet.column_tag; '和紙で固定します'
      var  column_title = data.ResultSet.column_title;'コラムタイトル'
      var  column_image1 =data.ResultSet.column_image1;'投稿画像'
      var  column_date = data.ResultSet.column_date;'投稿日時'

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
  console.log(USERS_API);
  fetch(USERS_API);

  /* /json読み込み */

  $('.btn').on('click', function () {
    var id = $(this).attr("id");
    alert(id);
  });

});
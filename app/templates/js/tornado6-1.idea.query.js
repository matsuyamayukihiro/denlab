document.addEventListener('DOMContentLoaded', (event) => {
  console.log(`DOMContentLoadedイベントが発生しました。`);

  // URL が「http://127.0.0.1:5500/idea.html?idea=1&ver=3」の場合

  console.log('idea', getParam('idea')); //「jquery」を出力
  let ideaNo = getParam('idea');
  //console.log('ver', getParam('ver')); // 「3」を出力

  console.log('location.href', location.href);

  let position = document.getElementById('info');
  console.log(position);
  const div = `
    <h2>アイデア` + ideaNo + `</h2>
    <p>11月1日～12月31日まで年末セールを開催！</p>
  `
  position.insertAdjacentHTML('beforeend', div);

  /**
   * Get the URL parameter value
   *
   * @param  name {string} パラメータのキー文字列
   * @return  url {url} 対象のURL文字列（任意）
   */
  function getParam(name, url) {
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
      results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
  }

  //モーダル表示
  $(".modal-open").modaal({
    start_open: true, // ページロード時に表示するか
    overlay_close: true, //モーダル背景クリック時に閉じるか
    before_open: function () { // モーダルが開く前に行う動作
      $('html').css('overflow-y', 'hidden'); /*縦スクロールバーを出さない*/
    },
    after_close: function () { // モーダルが閉じた後に行う動作
      $('html').css('overflow-y', 'scroll'); /*縦スクロールバーを出す*/
    }
  });

});
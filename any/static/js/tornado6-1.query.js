document.addEventListener('DOMContentLoaded', (event) => {
  console.log(`DOMContentLoadedイベントが発生しました。`);

  // URL が「http://www.example.com?lib=jquery&ver=3」の場合

  console.log('lib', getParam('lib')); //「jquery」を出力
  console.log('ver', getParam('ver')); // 「3」を出力

  console.log('location.href', location.href);

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

});
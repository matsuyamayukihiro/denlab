
$(document).on('ready', function () {
  $(".regular").slick({
    autoplay: true,//自動再生する
    autoplaySpeed: 4000,//自動再生のスピード
    speed: 800,//スライドするスピード
    dots: true,//スライドしたときのドット
    arrows: true,//左右の矢印
    Infinity: true,//スライドのループ
    pauseOnHover: true,//マウスホバーした時にスライドを一時停止する
  });
});
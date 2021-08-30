/*
$(document).ready(function () {
  $('.slick02').slick({
    responsive: [{
        breakpoint: 768,
        settings: {
          arrows: false,
        }
      },
      {
        breakpoint: 640,
        settings: {
          arrows: false,
          dots: false,
        }
      },
    ]
  });
});
*/

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

/*
$('.slick01').slick({
  responsive: [{
      breakpoint: 768,
      settings: {
        arrows: false,
      }
    },
    {
      breakpoint: 640,
      settings: {
        arrows: false,
        dots: false,
      }
    },
  ]
});

$('.slick03').slick({
  autoplay:true,
  autoplaySpeed:5000,
  dots:true,
});


$('.fade').slick({
  dots: true,
  infinite: true,
  speed: 500,
  fade: true,
  cssEase: 'linear'
});
*/